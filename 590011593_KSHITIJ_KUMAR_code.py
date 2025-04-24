import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your API key from OpenWeatherMap
API_KEY = "22377c13dbfde871792b1fac8dc6d4a2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def get_weather():
    location = location_entry.get()
    if not location:
        messagebox.showerror("Error", "Please enter a location.")
        return

    try:
        # Make API request
        params = {
            "q": location,
            "appid": API_KEY,
            "units": "metric"  # Use "imperial" for Fahrenheit
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check for errors in the API response
        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"])
            return

        # Extract weather data
        weather = data["weather"][0]["description"].capitalize()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]

        # Display weather data
        result_label.config(text=f"Weather: {weather}\n"
                                 f"Temperature: {temperature}°C\n"
                                 f"Humidity: {humidity}%\n"
                                 f"Wind Speed: {wind_speed} m/s\n"
                                 f"Pressure: {pressure} hPa")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# Location Entry
location_label = tk.Label(root, text="Enter Location:", font=("Arial", 14))
location_label.pack(pady=10)

location_entry = tk.Entry(root, font=("Arial", 14))
location_entry.pack(pady=10)

# Fetch Weather Button
fetch_button = tk.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather)
fetch_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Run the app
root.mainloop()
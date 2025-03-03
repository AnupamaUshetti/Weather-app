import requests
import tkinter as tk
from tkinter import messagebox

# Use your actual API key
API_KEY = "your_actual_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}  # Fetch in Celsius
    response = requests.get(BASE_URL, params=params)
    
    # Debugging: print the response to understand the error
    print(response.json())  # This will show the raw response from the API

    data = response.json()
    
    if response.status_code == 200:
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        result_label.config(text=f"Weather in {city}:\nTemperature: {temp}°C\nCondition: {weather_desc}")
    else:
        messagebox.showerror("Error", f"City not found! Error message: {data.get('message')}")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg="lightblue")

tk.Label(root, text="Enter City:", font=("Arial", 14), bg="lightblue").pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue", justify="left")
result_label.pack(pady=10)

root.mainloop()

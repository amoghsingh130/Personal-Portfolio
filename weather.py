import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk  

def get_weather():
    api_key = 'ff3ff5ddcdf02cdbdf1b6dbb20a27c67'
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = int((data['main']['temp'] - 273.15) * 9/5 + 32)
        desc = data['weather'][0]['description']
        result_label.config(text=f'Temperature: {temp}°F\nDescription: {desc}')
    else:
        result_label.config(text='Error fetching weather data')

root = tk.Tk()
root.title("Weather App")

root.configure(bg="#3498db")

city_label = tk.Label(root, text="Enter City:", bg="#3498db", font=("Arial", 12, "bold"))
city_label.pack()

city_entry = ttk.Entry(root, font=("Arial", 12))
city_entry.pack()

get_weather_button = ttk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

get_weather_button.config(compound="left")

result_label = tk.Label(root, text="", bg="#3498db", font=("Arial", 12))
result_label.pack()

window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.mainloop()

import tkinter as tk
from tkinter import ttk
import threading
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get('API_KEY')

def get_weather(location):
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={API_KEY}&contentType=json&include=current&unitGroup=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def show_weather(data, progress_bar):
    if data:
        city = data['resolvedAddress']
        temperature = data['currentConditions']['temp']
        weather = data['currentConditions']['conditions']
        weather_label.config(text=f'City: {city}\nTemperature: {temperature:.1f}°C\nWeather: {weather}')
    else:
        weather_label.config(text='Error retrieving weather data!')
    input_field.config(state=tk.NORMAL)
    progress_bar.destroy()


def search_weather():
    location = input_field.get()
    if location == '':
        return
    input_field.config(state=tk.DISABLED)
    progress_bar = ttk.Progressbar(root, length=200, mode='indeterminate')
    progress_bar.pack()
    progress_bar.start(10)
    weather_thread = threading.Thread(target=lambda: show_weather(get_weather(location), progress_bar))
    weather_thread.start()


root = tk.Tk()
root.title('Weather App')
root.geometry("300x200")
root.resizable(False, False)

input_field = tk.Entry(root, width=30)
input_field.pack(pady=10)

search_button = tk.Button(root, text='Search Weather', command=search_weather)
search_button.pack()

weather_label = tk.Label(root, text='')
weather_label.pack()

root.mainloop()

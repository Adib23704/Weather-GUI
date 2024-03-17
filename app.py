import tkinter as tk
import threading
import requests

API_KEY = 'a653085cc4744c50b04115958241703'

def get_weather(location):
    url = f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}&aqi=no'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def show_weather(data, loading_popup):
    if data:
        city = f"{data['location']['name']}, {data['location']['country']}"
        temperature = data['current']['temp_c']
        weather = data['current']['condition']['text']
        weather_label.config(text=f'City: {city}\nTemperature: {temperature:.1f}°C\nWeather: {weather}')
    else:
        weather_label.config(text='Error retrieving weather data!')
    loading_popup.destroy()
    input_field.config(state=tk.NORMAL)


def search_weather():
    location = input_field.get()
    input_field.config(state=tk.DISABLED)
    loading_popup = tk.Toplevel(root)
    loading_popup.title('Loading...')
    loading_label = tk.Label(loading_popup, text='Fetching weather data...')
    loading_label.pack()

    weather_thread = threading.Thread(target=lambda: show_weather(get_weather(location), loading_popup))
    weather_thread.start()


root = tk.Tk()
root.title('Weather App')

input_field = tk.Entry(root, width=30)
input_field.pack(pady=10)

search_button = tk.Button(root, text='Search Weather', command=search_weather)
search_button.pack()

weather_label = tk.Label(root, text='')
weather_label.pack()

root.mainloop()

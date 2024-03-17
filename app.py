import tkinter as tk
import threading
import requests
	
root = tk.Tk()
root.title('Weather App')

input_field = tk.Entry(root, width=30)
input_field.pack(pady=10)

search_button = tk.Button(root, text='Search Weather', command=search_weather)
search_button.pack()

weather_label = tk.Label(root, text='')
weather_label.pack()

root.mainloop()

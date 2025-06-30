import tkinter as tk
import requests
from tkintermapview import TkinterMapView
from config import api_key


class Weather:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("weathers")
        self.window.geometry("1000x700")
        self.api_key = api_key

        self.frame = tk.Frame(self.window, height=100)
        self.frame.pack(fill="x", padx=10, pady=5)

        self.label = tk.Label(self.frame, text="enter a city:", font=("Arial", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry = tk.Entry(self.frame, font=("Arial", 12), width=30)
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = tk.Button(self.frame, text="search", font=("Arial", 12), command=self.search_city)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.label_info = tk.Label(self.frame, text="choose a city on the map", font=("Arial", 12))
        self.label_info.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

        self.favorite_button = tk.Button(self.frame, text="add to favorite", font=("Arial", 12), command=print)
        self.favorite_button.grid(row=2, column=0, padx=5, pady=5, columnspan=3)

        self.map = TkinterMapView(self.window, width=950, height=550)
        self.map.pack(fill="both", padx=10, pady=5, expand=True)
        self.map.set_zoom(10)
        self.lat, self.lon = 66.4776882, 25.7253327
        self.map.set_position(self.lat, self.lon)
        self.map.add_left_click_map_command(self.click_on_map)
        self.info = None
        self.favorites = {}

    def search_city(self):
        city = self.entry.get()
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            try:
                response = requests.get(url)
                print(response.status_code)
                data = response.json()
                self.lat, self.lon = data["coord"]["lat"], data["coord"]["lon"]
                self.info = {
                    "name": data['name'],
                    "temp": round(data["main"]['temp']),
                    "description": data["weather"][0]["description"]
                }
                self.label_info.config(text=f"{self.info['name']}: {self.info['temp']}°C, {self.info['description']}")
                self.map.set_position(self.lat, self.lon)
            except:
                self.label_info.config(text="error in getting the info")

    def click_on_map(self, coords):
        self.lat, self.lon = coords
        url = (f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api_key}"
               f"&units=metric")
        try:
            response = requests.get(url)
            print(response.status_code)
            data = response.json()
            self.info = {
                "name": data['name'],
                "temp": round(data["main"]['temp']),
                "description": data["weather"][0]["description"]
            }
            self.label_info.config(text=f"{self.info['name']}: {self.info['temp']}°C, {self.info['description']}")
            self.map.set_position(self.lat, self.lon)
        except:
            self.label_info.config(text="error in getting the info")

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    app = Weather()
    app.run()

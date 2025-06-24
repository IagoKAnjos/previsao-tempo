import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "b4fa44888cd140a273b4f1caf692c33e" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric&lang=pt_br"
    response = requests.get(complete_url)
    return response.json()

def search_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Aviso", "Por favor, digite o nome de uma cidade.")
        return

    weather_data = get_weather(city)

    if weather_data.get("cod") != "404":
        print(weather_data)
        main = weather_data["main"]
        weather = weather_data["weather"][0]

        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]

        result_label.config(text=f"Cidade: {city}\nTemperatura: {temperature}°C\nUmidade: {humidity}%\nDescrição: {description.capitalize()}")
    else:
        messagebox.showerror("Erro", "Cidade não encontrada. Verifique o nome e tente novamente.")

# Configuração da janela principal
app = tk.Tk()
app.title("Previsão do Tempo")

# Campo de entrada para a cidade
city_label = tk.Label(app, text="Digite a cidade:")
city_label.pack(pady=10)

city_entry = tk.Entry(app, width=40)
city_entry.pack(pady=5)

# Botão de busca
search_button = tk.Button(app, text="Buscar Previsão", command=search_weather)
search_button.pack(pady=10)

# Rótulo para exibir os resultados
result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack(pady=20)

app.mainloop()



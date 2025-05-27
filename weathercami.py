import requests
import shutil
import json

class LlamadosInternet:

    def request(self):
        url=''
        r=requests.get(url)
        print(r)
        print(r.content)
        print(r.status_code)

    def descargar_img(self, url, file_name):
        res=requests.get(url,stream=True)
        if res.status_code == 200:
            with open(file_name,'wb')as f:
                shutil.copyfileobj(res.raw,f)
            print('imagen descargada correctamente')
        else:
            print('No se encontro la imagen')

    def get_weather(self,city,api_key):
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        params = {"q": city, "appid": api_key, "units": "metric"}

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()

            weather_data = response.json()

            if weather_data["cod"] == 200:
                print(f"Weather ins {weather_data['name']}:")
                print(f"  Description: {weather_data['weather'][0]['description']}")
                print(f"  Temperature: {weather_data['main']['temp']}°C")
                print(f"  Humidity: {weather_data['main']['humidity']}%")
                print(f"  Viento: {weather_data['wind']['speed']}m/s")
            else:
                    print(f"Error: {weather_data['message']}")

        except:
            print('error')

url =''
res = LlamadosInternet()
res.descargar_img(url,'imagen.jpg')
city = "Zapopan"
api_key = "69ec8ca2037d63a120d31c59efd0f604"
res.get_weather(city,api_key)


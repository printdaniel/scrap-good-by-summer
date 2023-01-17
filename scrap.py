from bs4 import BeautifulSoup
import requests

ACCUWEATHER = 'https://www.accuweather.com/es/ar/federal/9103/daily-weather-forecast/9103?day=1'

class AccuWeather:
    count = 0
    def __init__(self):
        AccuWeather.count += 1
        self.id = AccuWeather.count

    def validator_soup(self,url):
        """ Retorna el HTML parseado"""
        header = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                }

        page = requests.get(url,headers = header)
        try:
            soup = BeautifulSoup(page.content,"html.parser")
        except:
            return None
        return soup


    def temperatura(self):
        """
        Extrae y devuelve la temperatura actual de una página web específica.
    
        Args:
            self (object): Referencia a la instancia de la clase en la que se está ejecutando el método.
        
        Returns:
            (str): La temperatura en grados.
    
        """
        soup = self.validator_soup(ACCUWEATHER)
        self.temp = soup.find('div', class_=['temperature']).text.strip()[:2]
        return self.temp


    def salida_sol(self):
        """
        Extrae y devuelve la hora de salida del sol.
        Args:
            self(objects): Referencia a la instancia de la clas en la que se está ejecutando el método.
        Returns:
            (str): La hora.
        """
        soup = self.validator_soup(ACCUWEATHER)
        result = soup.find('span', class_=['text-value']).text
        self.salida_sol = result
        return self.salida_sol
        

    def entrada_sol(self):
        """
        Extrae y devuelve la hora de salida del sol.
        Args:
            self(objects): Referencia a la instancia de la clase en la que se está ejecutando el método.
        Returns:
            (str): La hora      
        """
        soup = self.validator_soup(ACCUWEATHER)
        result = soup.find_all('span', attrs={'text-value'})[1].text
        self.entrada_sol = result
        return self.entrada_sol


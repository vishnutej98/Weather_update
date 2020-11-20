import requests
from bs4 import BeautifulSoup


def weather(country):
    url = f"https://www.google.com/search?&q=weather in {country}"
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    temperature = s.find("div", class_="BNeawe").text
    return temperature


if __name__ == "__main__":
    country = input('Enter the Country/State/City: ')
    print(f"Current temperature in {country}: {weather(country)}")

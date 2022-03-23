# %%
import os
import re
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

load_dotenv()

apiKey = os.getenv("API_KEY")
flight = os.getenv("FLIGHT")
startAirport = os.getenv("START_AIRPORT")
endAirport = os.getenv("END_AIRPORT")
startDate = os.getenv("START_DATE")

parsedDate = datetime.strptime(
    startDate, "%Y-%m-%dT%H:%M:%S.%f+00:00")
endDate = parsedDate+timedelta(days=1)

flightRegex = re.compile("(?P<airline>\D+)(?P<flightNumber>\d+)")
engineRegex = re.compile("Engines\s+(?P<amount>\d+) x (?P<engines>.+)")

headers = {
    "x-apikey": apiKey,
}


# %%
def getFlight():
    m = flightRegex.match(flight)

    payload = {
        "origin": startAirport,
        "destination": endAirport,
        "airline": m.group("airline"),
    }
    url = f"https://aeroapi.flightaware.com/aeroapi/schedules/{parsedDate.strftime('%Y-%m-%d')}/{endDate.strftime('%Y-%m-%d')}"

    print("Sending request...")
    print("URL:", url)
    print("Payload:", payload)
    r = requests.get(url, params=payload, headers=headers)

    print("Response:", r.text)

    return r.json()["scheduled"][0]["fa_flight_id"]


def getEngine(flightId):
    url = f"https://aeroapi.flightaware.com/aeroapi/flights/{flightId}"

    print("Sending request...")
    print("URL:", url)
    r = requests.get(url, headers=headers)

    return r.json()


# %%
flightId = getFlight()
engine = getEngine(flightId)

# %%


def searchPlane(registration):
    payload = {
        "key": registration,
    }

    header = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
    }

    url = f"https://www.airfleets.net/recherche/"

    print("Sending request...")
    print("URL:", url)
    print("Payload:", payload)
    r = requests.get(url, headers=header, params=payload)

    soup = BeautifulSoup(r.text, "html.parser")
    planeHref = soup.find('main').find_all('table')[2].find_all('tr')[
        1].find_all('td')[0].find('a')['href']
    print("Plane href:", planeHref)

    return url + planeHref


registration = engine['flights'][0]['registration']
planeUrl = searchPlane(registration)
print("Plane URL:", planeUrl)

# %%


def getEngine(url):
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
    }

    r = requests.get(url, headers=header)

    soup = BeautifulSoup(r.text, "html.parser")

    m = engineRegex.match(
        soup.find('main').find_all('table')[6].find('td').text)
    print(m)
    return [m.group("amount"), m.group("engines")]


engineSpec = getEngine(planeUrl)
print("Engine: ", engineSpec[0])
print("Engine amount: ", engineSpec[1])

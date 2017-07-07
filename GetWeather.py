from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = 'http://w1.weather.gov/xml/current_obs/KPWM.xml'
data = ''

with urlopen(url) as response:
	for line in response:
		line = line.decode('utf-8')
		data += line
		
#print(data)
root = ET.fromstring(data)

location = root.find('location').text
time = root.find('observation_time').text
weather = root.find('weather').text
temp = root.find("temperature_string").text
humid = root.find("relative_humidity").text
wind = root.find("wind_string").text

print("The weather at {}\n{} is:\n{} with {}% humidity\n{}\nWind {}".format(location, time, temp, humid, weather, wind))

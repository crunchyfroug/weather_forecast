import requests
import json
import creds


city = input("Type in your city ")

response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={creds.API_KEY}&q={city}&aqi=no")
print(response)

if (response == "<Response [200]>"):
    print("City not found")
elif (response == "<Response [400]>"):
    print("Bad request, try again")
else: 
    print("Something went wrong, try again")

r = response.text
y = json.loads(r)
print(y)
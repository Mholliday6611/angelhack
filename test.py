import requests

url = "https://api.restb.ai/classify"

querystring = {"client_key":"630baac25e972c9f607047fdc7498322b7adca6469de70684eb9b99a6dae9f4c","model_id":"car_make_model","image_url":"http://i2.cdn.turner.com/money/dam/assets/170215105927-lamborghini-venenos-recall-car-1100x619.jpg"}

response = requests.request("GET", url, params=querystring)

print response.text
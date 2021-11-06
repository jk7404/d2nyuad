from supabase import create_client, Client
import time; 
import requests

#Access the DB for data input.
key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoic2VydmljZV9yb2xlIiwiaWF0IjoxNjM2MTc0MzIzLCJleHAiOjE5NTE3NTAzMjN9.M3_cTtMyV5eDLo8QLlyOgpD2YS4uGDz9DLIKQca7Rvs'
header = {
    'apikey': key,
    'Authorization': 'Bearer ' + key
}

header['Content-Type'] = 'application/json'
header['Prefer'] = 'return=representation'

#Count time and write the number of people in D2 for each timestamp.
time = int(time.time())
timecount = 0
num = 3

#Data is overwritten every 5 minutes.
while True:
    data = { "time": time, "num": num }
    response = requests.post(f'https://uxdydupspijujofdyxug.supabase.co/rest/v1/D2NYUAD', headers=header, json=data)
    time = int(time.time())
    timecount += 300
    num += 5
    print(response.text)

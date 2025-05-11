import requests
from datetime import datetime

API_KEY =""
APP_ID = ""

user_exercise = input("Enter exercise and duration\n")
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

exercise_endpoint = ""
sheet_endpoint = ""
# Nutrition API CALL

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


#  Personal data
GENDER = "male"
WEIGHT_KG = 74
HEIGHT_CM = 174
AGE = 31

parameters = {
    "query": user_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
exercise_data = response.json()

#Bearer Token Authentication
bearer_headers = {
"Authorization": "Bearer test123"
}


for exercise in exercise_data["exercises"]:
    sheet_inputs = {
        "arkusz1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    sheety_response.raise_for_status()
    print(sheety_response.text)
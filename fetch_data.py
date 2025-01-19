import requests
import pandas as pd

import json

def fetch_quiz_data():
    current_quiz_url = "https://www.jsonkeeper.com/b/LLQT"
    historical_data_url = "https://api.jsonserve.com/XgAgFJ"

    # Fetch data
    current_quiz_data = requests.get(current_quiz_url, verify=False).json()
    historical_data = requests.get(historical_data_url, verify=False).json()

    # Debugging the structure
    print(json.dumps(current_quiz_data, indent=4))
    print(json.dumps(historical_data, indent=4))

    historical_df = pd.DataFrame(historical_data)
    return current_quiz_data, historical_df

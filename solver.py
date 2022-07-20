import requests
import json

def Solve(username: str, apikey: str, data: str):
    url = "https://api.apitruecaptcha.org/one/gettext"
    payload = json.dumps({
      "userid": username,
      "apikey": apikey,
      "data": data,
      "case": "lower",
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    ret = response.json()
    if 'error' in ret:
      return False, ret['error']
    elif 'result' in ret:
      return True, ret['result']





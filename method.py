import requests

class Method:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send_method(self, metod, headers = {"Content-Type": "application/json", "Accept": "application/json"}, fields = {}):
        try:
            url = f"{self.webhook_url}/{metod}"
            response = requests.post(url, json = fields, headers = headers)
            response.raise_for_status()
            result = response.json()
            return result.get('result', [])  
        except requests.RequestException as e:
            print(f"Error in send_method: {e} \n {response.text}")
            return None
        

#placeholder for while not all methods are implemented
def send_any_method(webhook_url: str, method: str, headers = {"Content-Type": "application/json", "Accept": "application/json"}, fields = {}):
    try:
        url = f"{webhook_url}/{method}"
        response = requests.post(url, json=fields, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result.get('result', [])
    except requests.RequestException as e:
        print(f"Error in send_any_method: {e} \n {response.text}")
        return None
import requests
import time

# Configuration
URL = 'http://your-application-url.com'
CHECK_INTERVAL = 60  # in seconds

def check_application_health():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            return 'up'
        else:
            return 'down'
    except requests.exceptions.RequestException:
        return 'down'

if __name__ == '__main__':
    while True:
        status = check_application_health()
        print(f'Application status: {status}')
        time.sleep(CHECK_INTERVAL)

import pytz
from datetime import datetime

tz = pytz.timezone('Europe/Brussels')

def save_request(phone, line):
    try:
        f = open("requests.txt", "a")
        f.write(str(datetime.now(tz).strftime('%d/%m/%Y %H:%M:%S')) + "#" + phone + "#" + (line or ''))
        f.close()
        _increment_total_requests_()
    except Exception as e:
        print(e)

def get_total_requests():    
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()
    return count + 387 # random shift


def _increment_total_requests_():    
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
def save_request(phone, line):
    print('ok')
    try:
        f = open("requests.txt", "a")
        f.write(phone + "#" + (line or ''))
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
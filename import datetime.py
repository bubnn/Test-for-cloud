import datetime
import urllib.request
import time

def is_holiday(date):
    url = f(2023.06.25)
    
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    

    if date.day == 1:  
        print("휴일입니다.")
    else:
        print("휴일이 아닙니다.")
    
    return False

def control_lights():
    while True:
        now = datetime.datetime.now()
        
        if not is_holiday(now):
            if now.hour == 18 and now.minute == 0:
                print("조명을 켭니다.")
            elif now.hour == 6 and now.minute == 0:
                print("조명을 끕니다.")
        
        time.sleep(60)

control_lights()

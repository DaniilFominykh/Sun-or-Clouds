import random
import time
class Weather():
    def randomize(self):
        return random.randint(0,1)
class Detector():
    def __init__(self):
        self.realtime_weather=Weather()
    def iscloudexist(self):
        return self.realtime_weather.randomize()
class Sender():
    def sendmassage(self,massage):
        print(massage)
class Application():
    def __init__(self):
        self.detect=Detector()
        self.sender=Sender()
    def loopl(self):
        while True:
            if self. detect.iscloudexist()==1:
                time.sleep(1)
                self.sender.sendmassage(f"[{time.ctime()}] - The weather is cloudy")
            else:
                time.sleep(1)
                self.sender.sendmassage(f"[{time.ctime()}] - The weather is not cloudy")
run_app=Application()
run_app.loopl()

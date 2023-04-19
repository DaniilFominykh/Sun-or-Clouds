#Variant_1
import telebot
import time
import cv2
bot = telebot.TeleBot("5600707674:AAEBQlalT-3ip5S16nGPHV3cDa-tX1meaCk")
# Capture videoframes and detect clouds
class Detector():
    def __init__(self):
        pass
    def iscloudexist(self,input_video):
        _,frame=input_video.read()
        cv2.imshow('Video', frame)
        cv2.waitKey(1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        threshold_value = 150
        _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
        num_white_pixels = cv2.countNonZero(binary)
        total_pixels = binary.shape[0] * binary.shape[1]
        white_pixel_percentage = num_white_pixels / total_pixels
        return white_pixel_percentage
# Send messages
class Sender():
    def sendmessage(self,mymes):
        bot.send_message(chat_id='Your chat id', text=mymes)
# Application work with infinitive loop
class Application():
    def __init__(self,input_video):
        self.input_video=input_video
        self.detect=Detector()
        self.sender=Sender()
    def loop2(self):
        while True:
            if self.detect.iscloudexist(self.input_video) > 0.2:
                self.sender.sendmessage(f"[{time.ctime()}] - The weather is cloudy")
            else:
                self.sender.sendmessage(f"[{time.ctime()}] - The weather is not cloudy")


bot = telebot.TeleBot("Your token")
video=cv2.VideoCapture(0)
run_app=Application(video)
run_app.loop2()
bot.polling(none_stop=True)
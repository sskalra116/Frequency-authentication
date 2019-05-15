import RPi.GPIO as GPIO
from time import sleep
import os
import random
from psonic import *
import threading
from your import song

import getopt
import sys
from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
SOUND_PIN = 24
GPIO.setup(SOUND_PIN, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)


LEDPin1 = 26
LEDPin2 = 22
LEDPin3 = 17
LEDPin4 = 13

GPIO.setup(LEDPin1, GPIO.OUT)
GPIO.setup(LEDPin2, GPIO.OUT)
GPIO.setup(LEDPin3, GPIO.OUT)
GPIO.setup(LEDPin4, GPIO.OUT)

pwm1 = GPIO.PWM(LEDPin1,100)
pwm2 = GPIO.PWM(LEDPin2,100)
pwm3 = GPIO.PWM(LEDPin3,100)
pwm4 = GPIO.PWM(LEDPin4,100)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)
pwm1.ChangeDutyCycle(0)
pwm2.ChangeDutyCycle(0)
pwm3.ChangeDutyCycle(0)
pwm4.ChangeDutyCycle(0)

flag = 0

def sync():
    beats = 1
    while True:
        if GPIO.input(SOUND_PIN):
            beats+=1
            if beats%6==0:
                
                GPIO.output(LEDPin2, True)
                GPIO.output(LEDPin3, True)
                sleep(0.110)
                
            elif beats%6==1:
                GPIO.output(LEDPin1, True)
                GPIO.output(LEDPin2, True)
                sleep(0.110)
                
            elif beats%6==2:
                
                GPIO.output(LEDPin3, True)
                GPIO.output(LEDPin4, True)
                sleep(0.110)
                
            elif beats%6==3:
                
                GPIO.output(LEDPin1, True)
                GPIO.output(LEDPin4, True)
                sleep(0.110)
                
            elif beats%6==4:
                
                GPIO.output(LEDPin2, True)
                GPIO.output(LEDPin4, True)
                sleep(0.110)

            elif beats%6==5:
                
                GPIO.output(LEDPin1, True)
                GPIO.output(LEDPin3, True)
                sleep(0.110)
                
                    
            
        else:
            GPIO.output(LEDPin1, False)
            GPIO.output(LEDPin2, False)
            GPIO.output(LEDPin3, False)
            GPIO.output(LEDPin4, False)



def execute():
    count = 0
    while True:

        if GPIO.input(SOUND_PIN):
            count+=1
            GPIO.output(LEDPin2, True)
            GPIO.output(LEDPin3, True)
            print(38-count)
            sleep(0.110)
            if count >= 38:
                print("playing drum track!")
                t1 = threading.Thread(target=sync)
                t2 = threading.Thread(target=song)

                t1.start()
                t2.start()

                t1.join()
                t2.join()
                
        else:
            GPIO.output(LEDPin1, False)
            GPIO.output(LEDPin2, False)
            GPIO.output(LEDPin3, False)
            GPIO.output(LEDPin4, False)
        
        #GPIO.add_event_callback(SOUND_PIN, callback)


class drums(Resource):
    def __init__(self, name="drums", coap_server=None):
        super(drums, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
        self.payload = "Playing drum track \m/"
        

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.payload = "Playing drum track \m/"
        execute()
        return self

    def render_POST(self, request):
        res = HelloWorld()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True

class CoAPServer(CoAP):
    def __init__(self, host, port, multicast=False):
        CoAP.__init__(self, (host, port), multicast)
        self.add_resource('drum track/', drums())
        


def main(argv):  # pragma: no cover
    ip = "149.159.225.134"
    port = 5683
    multicast = False
    try:
        opts, args = getopt.getopt(argv, "hi:p:m", ["ip=", "port=", "multicast"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--ip"):
            ip = arg
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-m", "--multicast"):
            multicast = True

    server = CoAPServer(ip, port, multicast)
    
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])



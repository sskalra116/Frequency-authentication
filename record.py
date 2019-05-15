import pyaudio
import wave
import numpy as np
from psonic import *
from statistics import median
from threading import Thread
import RPi.GPIO as GPIO
from time import sleep
import os


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
SOUND_PIN = 24
GPIO.setup(SOUND_PIN, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
count = 0

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


reply = 0

def bass():
  while True:
        sample(DRUM_BASS_SOFT, amp= 0.125)
        for i in range(2):
          play(C2)
          sleep(0.25)
                  


def synth():
  
  while True:
      play(F4, amp= 0.1, sustain= 2)
      play(F3, amp= 0.1, sustain= 1.5)
      play(F2, amp= 0.1, sustain= 2)
      sleep(1)
      play(As4, amp= 0.1, sustain= 1.5)
      play(As3, amp= 0.1, sustain= 2.5)
      play(As2, amp= 0.1, sustain= 2.5)
      sleep(2)
      play(As4,amp= 0.1, sustain= 1.5)
      play(As3,amp= 0.1, sustain= 1)
      play(As2,amp= 0.1, sustain= 1.5)
      sleep(1)
      play(A4,amp= 0.1, sustain= 2)
      play(A3,amp= 0.1, sustain= 1)
      play(A2,amp= 0.1, sustain= 2)
      sleep(1)
      play(G4,amp= 0.1, sustain= 2)
      play(G3,amp= 0.1, sustain= 1)
      play(G2,amp= 0.1, sustain= 2)
      sleep(1)
      play(A4,amp= 0.1, sustain= 3)
      play(A3,amp= 0.1, sustain= 1)
      play(A2,amp= 0.1, sustain= 3)
      sleep(2)
      play(F4, amp= 0.1, sustain= 2)
      play(F3, amp= 0.1, sustain= 1.5)
      play(F2, amp= 0.1, sustain= 2)
      sleep(1)
      play(As4, amp= 0.1, sustain= 1.5)
      play(As3, amp= 0.1, sustain= 2.5)
      play(As2, amp= 0.1, sustain= 2.5)
      sleep(2)
      play(As4,amp= 0.1, sustain= 1.5)
      play(As3,amp= 0.1, sustain= 1)
      play(As2,amp= 0.1, sustain= 1.5)
      sleep(1)
      play(Gs4,amp= 0.1, sustain= 2)
      play(Gs3,amp= 0.1, sustain= 1)
      play(Gs2,amp= 0.1, sustain= 2)
      sleep(1)
      play(G4,amp= 0.1, sustain= 2)
      play(G3,amp= 0.1, sustain= 2)
      play(G2,amp= 0.1, sustain= 2)
      sleep(1)
      play(Gs4,amp= 0.1, sustain= 3)
      play(Gs3,amp= 0.1, sustain= 1.5)
      play(Gs2,amp= 0.1, sustain= 3)
      sleep(2)
      
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
                
            elif beats%6==0:
                
                GPIO.output(LEDPin2, True)
                GPIO.output(LEDPin4, True)
                sleep(0.110)

            elif beats%6==0:
                
                GPIO.output(LEDPin1, True)
                GPIO.output(LEDPin3, True)
                sleep(0.110)
                
                    
            
        else:
            GPIO.output(LEDPin1, False)
            GPIO.output(LEDPin2, False)
            GPIO.output(LEDPin3, False)
            GPIO.output(LEDPin4, False)


def record():
    sleep(2)
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "output.wav"
    global count
    count = 0
    mode1 = []
    mode2 = []
    global mode11
    global mode22
    
    
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK, exception_on_overflow = False)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    chunk = 2048

    # open up a wave
    wf = wave.open('output.wav', 'rb')
    swidth = wf.getsampwidth()
    RATE = wf.getframerate()
    # use a Blackman window
    window = np.blackman(chunk)
    # open stream
    p = pyaudio.PyAudio()
    stream = p.open(format =
                    p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = RATE,
                    output = True)

    # read some data
    data = wf.readframes(chunk)
    # play stream and find the frequency of each chunk
    while len(data) == chunk*swidth:
        # write data out to the audio stream
        #stream.write(data)
        # unpack the data and times by the hamming window
        indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
                                             data))*window
        # Take the fft and square each value
        fftData=abs(np.fft.rfft(indata))**2
        # find the maximum
        which = fftData[1:].argmax() + 1
        # use quadratic interpolation around the max
        if which != len(fftData)-1:
            y0,y1,y2 = np.log(fftData[which-1:which+2:])
            x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
            # find the frequency and output it
            thefreq = (which+x1)*RATE/chunk
            
            count+= 1
            #print(int(thefreq))
            #print("count", count)
            if count>=5 and count<=30:
                mode1.append(int(thefreq))
                
            if count>30 and count<=85:
                mode2.append(int(thefreq))
                
        else:
            thefreq = which*RATE/chunk
            print("no"%thefreq)
        # read some more data
        data = wf.readframes(chunk)
    #if data:
        #stream.write(data)
    stream.close()
    p.terminate()
    mode11 = median(mode1)
    mode22 = median(mode2)
    print("median1 ", mode11)
    print("median2 ", mode22)
    
record()

if (mode11>330 and mode11<370 and mode22>450 and mode22<486 and reply == 0):
    reply+=1
    play(As4,amp= 0.1, sustain= 1.5)
    play(As3,amp= 0.1, sustain= 1)
    play(As2,amp= 0.1, sustain= 1.5)
    sleep(1)
    play(A4,amp= 0.1, sustain= 2)
    play(A3,amp= 0.1, sustain= 1)
    play(A2,amp= 0.1, sustain= 2)
    sleep(1)
    play(G4,amp= 0.1, sustain= 2)
    play(G3,amp= 0.1, sustain= 1)
    play(G2,amp= 0.1, sustain= 2)
    sleep(1)
    play(A4,amp= 0.1, sustain= 1.5)
    play(A3,amp= 0.1, sustain= 1)
    play(A2,amp= 0.1, sustain= 3)
    sleep(2)
    record()

if (mode11>330 and mode11<370 and mode22>450 and mode22<486 and reply == 1):
    reply+=1
    play(As4,amp= 0.1, sustain= 1.5)
    play(As3,amp= 0.1, sustain= 1)
    play(As2,amp= 0.1, sustain= 1.5)
    sleep(1)
    play(Gs4,amp= 0.1, sustain= 2)
    play(Gs3,amp= 0.1, sustain= 1)
    play(Gs2,amp= 0.1, sustain= 2)
    sleep(1)
    play(G4,amp= 0.1, sustain= 2)
    play(G3,amp= 0.1, sustain= 2)
    play(G2,amp= 0.1, sustain= 2)
    sleep(1)
    play(Gs4,amp= 0.1, sustain= 1.5)
    play(Gs3,amp= 0.1, sustain= 1.5)
    play(Gs2,amp= 0.1, sustain= 3)
    sleep(2)
    record()

if (mode11>330 and mode11<370 and mode22>372 and mode22<412 and reply == 2):
    
    bass_thread = Thread(target=bass)
    synth_thread = Thread(target=synth)
    sync_thread = Thread(target=sync)

    bass_thread.start()
    synth_thread.start()
    sync_thread.start()
    

    bass_thread.join()
    synth_thread.join()
    sync_thread.join()
    

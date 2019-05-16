# Frequency-authentication

The goal was to play a certain music interval and make the raspberry pi respond to that particular
frequency interval in musical notes too thereby, authenticating and making a harmony in real time along with LEDs 
synchronized with the rhythm of the track

Tools & coding environments used:
--------------

Python 3,
Music coding Environment → Sonic Pi,
Sound Sensor,
USB Microphone,
LEDs 

Implementation
------------------
### 1.Record the sound of the played notes
Pyaudio functions allowed to record a 3 second long audio. I divided the audio into 86 equal CHUNKS

### 2.Calculate the frequency of the recorded notes
The **YIN algorithm** simplified this task by computing the fourier transform of each chunk and taking its logarithm thereby,
giving the value of each chunk in Hz. The median of the 1st and 2nd half had to be taken separately to get the frequency
that was closest to the played notes.

### 3. Check the frequency in range

If the frequency fell in range, the program responded by playing back the melody. If the median was less than the given 
lower limit(330), there was no response and no further recording.

**This is a 3-level authentication using music.**

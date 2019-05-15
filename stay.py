
from psonic import *
from threading import Thread

def bass():
  while True:
        sample(DRUM_BASS_SOFT, amp= 0.0625)
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

bass_thread = Thread(target=bass)
synth_thread = Thread(target=synth)

bass_thread.start()
synth_thread.start()

bass_thread.join()
synth_thread.join()



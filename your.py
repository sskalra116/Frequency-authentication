from psonic import *


def song():

  bass_drop = 48


  for i in range(16):
    play(bass_drop, attack=0, release= 0.0625, amp=3)
    sleep(0.0625)
    bass_drop-=1

  sleep(0.125)
  #38-76
  for i in range(2):
    sample(DRUM_CYMBAL_OPEN)
    for i in range(2):
      for i in range(2):
        sample(DRUM_HEAVY_KICK)
        for i in range(4):
          sample(DRUM_SNARE_SOFT)
          play(C2, attack=0, release=0.125, amp=3)
          sleep(0.125)
        
      
      sample(DRUM_HEAVY_KICK)
      sample(DRUM_SNARE_SOFT)
      
      sleep(0.5)
      
      for i in range(2):
        sample(DRUM_HEAVY_KICK)
        for i in range(4):
          sample(DRUM_SNARE_SOFT)
          play(C2, attack=0, release=0.125, amp=3)
          sleep(0.125)
        
        sample(DRUM_HEAVY_KICK)
        sample(DRUM_SNARE_SOFT)
        sleep(0.5)
      
      
      sample(DRUM_HEAVY_KICK)
      sleep(0.5)
    
  #prob
  #114
  for i in range(2):
    for i in range(9):
      sample(DRUM_HEAVY_KICK)
      sample(DRUM_SNARE_SOFT)
      
      sleep(0.125)
    
    sleep(0.375)
    for i in range(5):
      sample(DRUM_HEAVY_KICK)
      sample(DRUM_SNARE_SOFT)
      
      sleep(0.125)
    
    sleep(0.375)
    for i in range(5):
      sample(DRUM_HEAVY_KICK)
      sample(DRUM_SNARE_SOFT)
      
      sleep(0.125)
    
    
    sleep(0.875)



  #152
  for i in range(2):
    for i in range(8):
      sample(DRUM_HEAVY_KICK)
      sample(DRUM_SNARE_SOFT)
      
      sleep(0.125)
    
    sample(DRUM_HEAVY_KICK)
    sample(DRUM_SNARE_SOFT)
    
    
    sleep(0.5)
    
    for i in range(4):
      sample(DRUM_SNARE_SOFT)
      
      sleep(0.125)
    
    sample(DRUM_HEAVY_KICK)
    sample(DRUM_SNARE_SOFT)
    
    sleep(0.5)
    
    for i in range(4):
      sample(DRUM_SNARE_SOFT)
      
      sleep(0.125)
    
    sample(DRUM_HEAVY_KICK)
    sample(DRUM_SNARE_SOFT)
    sleep(0.5)
    
    sleep(0.5)

  #190 - 5
  #picking up
  for i in range(3):
    
    for i in range(2):
      sample(DRUM_SNARE_SOFT)
      sleep(0.125)
      for i in range(5):
        sample(DRUM_HEAVY_KICK)
        sleep(0.125)
      
    
    
    sample(DRUM_SNARE_SOFT)
    sleep(0.125)
    for i in range(3):
      sample(DRUM_HEAVY_KICK)
      sleep(0.125)
    

  #210
  for i in range(2):
    sample(DRUM_SNARE_SOFT)
    sleep(0.125)
    for i in range(4):
      sample(DRUM_SNARE_SOFT)
      sample(DRUM_HEAVY_KICK)
      sleep(0.125)
    
    sample(DRUM_HEAVY_KICK)
    sleep(0.125)



  sample(DRUM_SNARE_SOFT)
  sleep(0.125)
  for i in range(3):
    sample(DRUM_SNARE_SOFT)
    sample(DRUM_HEAVY_KICK)
    sleep(0.125)

  #210+
  # chorus
  for i in range(3):
    for i in range(2):
      sample(DRUM_CYMBAL_OPEN)
      for i in range(4):
        sample(DRUM_HEAVY_KICK)
        
        sleep(0.125)
      
    
    sample(DRUM_CYMBAL_OPEN)
    sample(DRUM_HEAVY_KICK)
    sleep(0.5)
    #gap
    
    for i in range(2):
      sample(DRUM_CYMBAL_OPEN)
      for i in range(4):
        sample(DRUM_HEAVY_KICK)
        
        sleep(0.125)
      
      sample(DRUM_CYMBAL_OPEN)
      sample(DRUM_HEAVY_KICK)
      sleep(0.5)
    
    
    sample(DRUM_CYMBAL_OPEN)
    sample(DRUM_HEAVY_KICK)
    sleep(0.5)


# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:15:15 2021

@author: AVINASH
"""
  # Load the popular external library
from time import sleep
import pygame

pygame.init()
sound = pygame.mixer.Sound("S:\personal projects\cricket bot\sounds\casual.mp3")
pygame.mixer.Sound.play(sound)
import pyttsx3
import time
engine = pyttsx3.init()


rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.3)
pyttsx3.speak("HEllo")
pyttsx3.speak("Avinash")
engine.setProperty('rate', 130)
engine.setProperty('volume', 0.4)
engine.say("full outside off stump. Defended back towards mid on. The umpire clips the bails off")
engine.stop()
engine.say("full outside off stump. Defended back towards mid on. The umpire clips the bails off")

engine.runAndWait()

time.sleep(1)
engine.stop()
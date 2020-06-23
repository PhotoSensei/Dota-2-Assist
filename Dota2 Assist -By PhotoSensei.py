import datetime
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import mixer 
import time
import keyboard
count=0
min = 0
sec = 0
wards=45
power=240
bounty=300
stack=120
state='stoped'
print("when timer reaches 0:00 ingame press Enter for perfect timings of reminders")
mixer.init()
mixer.music.set_volume(1)

def start_func():
    mixer.music.load(r"C:\Users\Mayuresh\Desktop\remind dota\game begun.mp3")
    mixer.music.play()
    state ="start"
    while state=="start":
        
        global count
        global min
        global sec
        global wards
        global power
        global bounty
        global stack
        time.sleep(1)
        sec=sec+1
        count=count+1
        if sec==60:
            min=min+1
            sec=00
        print('{:02d}:{:02d}'.format(min,sec))

        if count==(power-12):
            print("power rune about to spawn")
            mixer.music.load(r"C:\Users\Mayuresh\Desktop\remind dota\power rune.mp3")
            mixer.music.play()
            power=power+120
            
        if count==(bounty-20):
            print("bounty rune about to spawn")
            mixer.music.load(r"C:\Users\Mayuresh\Desktop\remind dota\bounty rune.mp3")
            mixer.music.play()
            bounty=bounty+300
            

        if count==(stack-15) and count<=1200:
            print("stack a jungle camp")
            mixer.music.load(r"C:\Users\Mayuresh\Desktop\remind dota\jungle camp.mp3")
            mixer.music.play()
            stack=stack+60
           

        if count==wards:
            print("Buy Wards")
            mixer.music.load(r"C:\Users\Mayuresh\Desktop\remind dota\buy wards.mp3")
            mixer.music.play()
            wards=wards+135
        
       
        

keyboard.wait('+')
start_func()


    


from tkinter import *
import tkinter.font
from gpiozero import LED 
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

## Hardware 
ledB = LED(4)
ledR = LED(17)
ledG = LED(27)

## GUI DEFINITIONS
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

### EVENT FUNCTIONS
def ledToggleR():
	if ledR.is_lit:
		ledR.off()
		ledG.off()
		ledB.off()
		ledButtonG["text"] = "turn on Green"
		ledButtonR["text"] = "turn on Red"
		ledButtonB["text"] = "turn on Blue"
	else:
		ledR.on()
		ledG.off()
		ledB.off()
		ledButtonR["text"] = "Turn off red"
		ledButtonG["text"] = "turn on Green"
		ledButtonB["text"] = "turn on Blue"
		
def ledToggleB():
	if ledB.is_lit:
		ledR.off()
		ledG.off()
		ledB.off()
		ledButtonG["text"] = "turn on Green"
		ledButtonR["text"] = "turn on Red"
		ledButtonB["text"] = "turn on Blue"
	else:
		ledR.off()
		ledG.off()
		ledB.on()
		ledButtonG["text"] = "turn on Green"
		ledButtonR["text"] = "turn on Red"
		ledButtonB["text"] = "turn off Blue"
		
def ledToggleG():
	if ledG.is_lit:
		ledR.off()
		ledG.off()
		ledB.off()
		ledButtonG["text"] = "turn on Green"
		ledButtonR["text"] = "turn on Red"
		ledButtonB["text"] = "turn on Blue"
	else:
		ledR.off()
		ledG.on()
		ledB.off()
		ledButtonG["text"] = "turn off Green"
		ledButtonR["text"] = "turn on Red"
		ledButtonB["text"] = "turn on Blue"
##Widgets 
ledButtonR = Button(win, text = "turn on Red", font = myFont, command = ledToggleR, bg = 'bisque2', height = 1, width = 24)
ledButtonB = Button(win, text = "turn on Blue", font = myFont, command = ledToggleB, bg = 'bisque2', height = 1, width = 24)
ledButtonG = Button(win, text = "turn on Green", font = myFont, command = ledToggleG, bg = 'bisque2', height = 1, width = 24)

ledButtonR.grid(row=0, column=1)
ledButtonB.grid(row=1, column=1)
ledButtonG.grid(row=2, column=1)

	



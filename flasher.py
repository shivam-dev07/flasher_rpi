from gpiozero import PWMOutputDevice
import time

ringer = PWMOutputDevice(18, initial_value=0.2, frequency =2000) #ringer starts
ringer.on()
time.sleep(0.2)
ringer.off()
time.sleep(1)
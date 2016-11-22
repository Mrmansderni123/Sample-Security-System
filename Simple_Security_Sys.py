##Import all necessary libraries
from Tkinter import *
##from ttk import *
##import Tkinter as tk
import RPi.GPIO as pi


pi.setmode(pi.BCM)##Set up gpio numbering
pi.setup(20,pi.IN,pull_up_down=pi.PUD_UP)## Setup GPIO pull up

def motion_Detect(root):
    
      if pi.input(20)==True:  
           print "Motion Detected"
      
def arm_system():
   global only_Once
   only_Once=0
   if only_Once==0:
          try:
              pi.add_event_detect(20,pi.RISING,motion_Detect)## Turn on interupt
              print 'System armed'
              only_Once=+1
          except Exception :
              sys.exc_clear()
              
def disarm_system():
    pi.remove_event_detect(20)
    print 'System Disarmed'
                  
def button1(root):

    arm_button=Button(root,text='Arm',command=arm_system)
    arm_button.grid(column=0,row=1)
      
def button2(root):

    disarm_button=Button(root,text='Disarm',command=disarm_system)
    disarm_button.grid(column=1,row=1)
    
def main():
    root = Tk()
    root.title("Security System")
    button1(root)
    button2(root)
    root.mainloop()

main()

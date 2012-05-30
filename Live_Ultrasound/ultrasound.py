import serial

port = serial.Serial('/dev/tty.usbserial-A900F6CA')
port.close()
port.open()
port.timeout = 0.25

'''while True:
    print port.readline()
    time.sleep(1)'''


## Add live streaming from ardino in another thread updating the text
## from the main thread. This will be VERY easy to do

## Add and IF into the mix so it displays ERROR rarther than the MAX number


import Tkinter as tk
import time, thread

dist = None
go = None
display = None

def reset():
    
    global dist

    button["text"] = "START"
    lbl1["text"] = "Press to start"
    
    

def threadTest():

    global dist, go, display

    while True: ## add catch

        dist = port.readline()
        

        if dist == "":
            lbl1["text"] = str(display)
            time.sleep(0.2)
            
                
        else:
            display = dist
            lbl1["text"] = str(display)
            time.sleep(0.2)


def timer():

    global dist, go, display

    thread.start_new_thread(threadTest,())

       
root = tk.Tk()


lbl1 = tk.Label(root, text = "Will update...", font=("Calbri",100))
lbl1.pack()

root.title("Timer")

root.geometry("200x200")

button = tk.Button( text="START", width=25, command = timer())
#button.pack()

root.mainloop()

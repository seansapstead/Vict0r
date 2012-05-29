import Tkinter as tk
import time, thread

now = None
go = None

#lbl1["text"] = "HEY!"

def reset():
    
    global now, go

    now = None
    go = None

    button["text"] = "START"
    lbl1["text"] = "Press to start"
    
    

def threadTest():

    global now, go

    while go == 0:

        timer = round(time.time() - now, 1)
        
        lbl1["text"] = timer
        time.sleep(0.1)


def timer():

    global now, go

    
    if button["text"] == "START":

        time.sleep(0.1)

        button["text"] = "STOP"

        go = 0
        thread.start_new_thread(threadTest,())
        
        now = time.time()
        lbl1["text"] = "Press to stop"
               
            
    elif button["text"] == "STOP":
        button["text"] = "START"

        go = 1

        timer = round(time.time() - now, 3)
        
        lbl1["text"] = timer

       
root = tk.Tk()


lbl1 = tk.Label(root, text = "Press to start", font=("Calbri",80))
lbl1.pack()

root.title("Timer")

root.geometry("540x160")

button = tk.Button( text="START", width=25, command = timer)
button2 = tk.Button( text="Reset", width=25, command = reset)

button.pack()
button2.pack()

root.mainloop()

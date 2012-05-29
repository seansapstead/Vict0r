import Tkinter as tk
import time

print time.time()

now = None


#lbl1["text"] = "HEY!"

def timer():

    global now

    
    if button["text"] == "START":

        time.sleep(0.1)

        button["text"] = "STOP"
        
        now = time.time()
        lbl1["text"] = "Press to stop"

        ## start a new thread constently putting the time in...
            
            
    elif button["text"] == "STOP":
        button["text"] = "START"

        timer = round(time.time() - now, 3)
        
        lbl1["text"] = timer

       
root = tk.Tk()


lbl1 = tk.Label(root, text = "Press to start", font=("Calbri",80))
lbl1.pack()

root.title("Timer")

root.geometry("520x125")

button = tk.Button( text="START", width=30, command = timer)

button.pack()

root.mainloop()

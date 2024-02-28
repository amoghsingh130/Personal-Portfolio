from appJar import gui
from PIL import Image, ImageTk
from time import sleep, time, ctime

app = gui()

curr_time = ctime(time()).split()[3]
window_width = 600
window_height = 400

clock_border = ImageTk.PhotoImage(Image.open("C:/Users/amogh/OneDrive/Documents/His exellency Amogh Singh/Alarm Clock Project Files/ClockBorder.png"))

app.setSize(window_width, window_height)

def update_time():
    curr_time = ctime(time()).split()[3]
    if int(curr_time[0:2]) > 12:
        curr_time = str(int(curr_time[0:2])-12) + curr_time[2:len(curr_time)]
    app.setLabel("title", f"Time: {curr_time}")
    app.after(1000, update_time)

def start_timer():
    app.setLabel("timer", )

app.setFont(30)
app.addLabel("title", f"Time: {curr_time}")
update_time()
app.addCanvas("canvas")

# app.addButton("startTimer", )

app.go()


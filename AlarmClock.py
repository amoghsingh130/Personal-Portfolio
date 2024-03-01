from appJar import gui
from time import sleep, time, ctime

app = gui()

curr_time = ctime(time()).split()[3]
window_width = 600
window_height = 400
global timer_running 


app.setSize(window_width, window_height)

def update_time():
  curr_time = ctime(time()).split()[3]
  if int(curr_time[0:2]) > 12:
      curr_time = str(int(curr_time[0:2])-12) + curr_time[2:len(curr_time)]
  app.setLabel("title", f"Time: {curr_time}")
  app.after(1000, update_time)

def stop_timer():
  if timer_running:
    app.setLabel("timer_time", curr_time)
    timer_running = False
  

def start_timer():
  timer_running = True
  while timer_running:
    hours, minutes, seconds = "0", "0", "0"
    if len(seconds) == 1: 
      seconds = "0" + seconds
    elif seconds == "59": 
      seconds = "00"
      minutes = f"{1+int(minutes)}"
    if len(minutes) == 1: 
      minutes = "0" + minutes
    elif minutes == "59": 
      minutes = "00"
      hours = f"{1+int(hours)}"
    seconds = f"{1+int(seconds)}"
    app.setLabel("timer_time", f"{hours}:{minutes}:{seconds}")
    curr_label = app.getLabel("timer_time")
    app.after(1000, start_timer)

app.setFont(30)
app.addLabel("title", f"Time: {curr_time}")
update_time()

app.addCanvas("canvas")

app.addButton("Start Timer", start_timer)
app.addButton("Stop Timer", stop_timer)
app.addLabel("timer_time", "00:00:00")

app.go()


from appJar import gui
from time import sleep, time, ctime

app = gui()

curr_time = ctime(time()).split()[3]
window_width = 600
window_height = 400
end_time = 1000000000000000

app.setSize(window_width, window_height)

def update_time():
  curr_time = ctime(time()).split()[3]
  if int(curr_time[0:2]) > 12:
    curr_time = str(int(curr_time[0:2])-12) + curr_time[2:len(curr_time)]
  app.setLabel("title", curr_time)
  app.setLabelWidth("title", 20)
  app.setLabelHeight("title", 2)
  app.setLabelAnchor("title", "n")
  app.after(1000, update_time)

update_time()

app.addLabel("time", f"Time: {curr_time}")

app.addCanvas("canvas")
app.addCanvasOval("canvas", window_width/2-100, window_height/2-120, 200, 200, fill=None, outline="black", width=3)

app.after(1000, update_time)

app.go()

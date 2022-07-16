from cgitb import text
from email.mime import image
from itertools import count
from tkinter import *
import math
from urllib import response
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- # 
def stop_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    checkmark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    if reps %8 == 0:
        
        count_down(LONG_BREAK_MIN*60)
        label.config(text="Break", fg=RED)
    elif reps %2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label.config(text="Break", fg=PINK)

    else:
        count_down(WORK_MIN*60)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count/60)
    count_seconds = count%60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count>0:
        global timer
        timer =  window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        time = math.floor(reps/2)
        for _ in range(time):
            marks+="✔"
        checkmark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodore")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="TIMER", fg=GREEN , font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)




button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(row=2,column=0)
button_start.config(padx=7, pady=3)

button_reset = Button(text="Reset", highlightthickness=0, command=stop_timer)
button_reset.grid(row=2,column=2)
button_reset.config(padx=7, pady=3)

checkmark = Label( fg=GREEN , font=(FONT_NAME, 20, "bold"), bg=YELLOW)
checkmark.grid(row=3, column=1)

window.mainloop()
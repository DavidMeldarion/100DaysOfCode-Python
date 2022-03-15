from tkinter import *
import math
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
timer = None
mark = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global mark
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")
    reps = 0
    mark = ""
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps == 8:
        count = long_break_seconds
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count = short_break_seconds
        timer_label.config(text="Break", fg=PINK)
    else:
        count = work_seconds
        timer_label.config(text="Work", fg=GREEN)
    count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global mark
        if reps % 2 == 0:
            mark += "✔"
        checkmarks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label()
timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
timer_label.grid(column=1, row=0)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
checkmarks.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_button = Button()
start_button.config(text="Start", font=(FONT_NAME, 12, "normal"), command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button()
reset_button.config(text="Reset", font=(FONT_NAME, 12, "normal"), command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()

import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#0e9630"
YELLOW = "#cfca95"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60      # Duration of work interval in minutes
SHORT_BREAK_MIN = 5 * 60    # Duration of short break interval in minutes
LONG_BREAK_MIN = 20 * 60    # Duration of long break interval in minutes
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1
    print(reps)

    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    countdown_min = math.floor(count / 60)
    countdown_sec = count % 60

    if countdown_sec < 10:
        countdown_sec = f"0{countdown_sec}"

    canvas.itemconfig(timer_text, text=f"{countdown_min}:{countdown_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        check_label.config(text="✔" * int(reps / 2), fg=GREEN, bg=YELLOW)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="Day-28\\tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_count)
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
check_label = Label(text="", fg=GREEN, bg=YELLOW)

timer_label.grid(column=2, row=1)
canvas.grid(column=2, row=2)
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)
check_label.grid(column=2, row=4)

window.mainloop()

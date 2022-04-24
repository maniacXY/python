from tkinter import *
from tkinter import font

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    top_label.config(text="Timer")
    middle_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global REPS
    REPS = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS == 8:
        count_down(long_break_sec)
        top_label.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        top_label.config(text="Short Break", fg=PINK)
    else: 
        count_down(work_sec)
        top_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = count // 60
    count_sec = count % 60
    #PROLEM, CALC start at 5:0 without tht if state
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
       
    else: 
        start_timer()
        marks = ""
        work_sessions = REPS//2
        for _ in range(work_sessions):
            marks += "✔"
        middle_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


top_label = Label(text="Timer", font=(FONT_NAME,35,"bold"), bg=YELLOW)
top_label.config(fg=GREEN)
top_label.grid(column=1, row=0)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102,112, image=tomato_img)
timer_text = canvas.create_text(102,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold") )
canvas.grid(column=1, row=1)

left_button = Button(text="Start", pady=0, padx=0, bg="white", justify="right", command=start_timer )
left_button.grid(column=0, row=2)

middle_label = Label(text="", bg=YELLOW)
middle_label.grid(column=1, row=3)

right_button = Button(text="Reset", padx=0, pady=0, bg="white", justify="left", command=reset_timer)
right_button.grid(column=2, row=2)


window.mainloop()

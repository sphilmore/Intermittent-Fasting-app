import math
from email.mime.text import MIMEText
from tkinter import *
from PIL import ImageTk, Image
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 57600
FAST_HOUR = 16
BREAK_FAST = 8
reps = 0
timer = None
my_email = ""
send_to = ""
import smtplib
#--------------------------Reset Timer-------------------------------------------------
def reset_timer():
    window.after_cancel(1000)
    canvas.itemconfig(timer_text, text="00:00:00")
    timer_label.config(text="Fasting")
#---------------------------Timer-------------------------------------------------------
def start_timer():
    global reps
    reps +=1
    if reps %8==0:
        count_down(BREAK_FAST * 3600)
        timer_label.config(text="Eat Window", fg=RED)
        msg = MIMEText("Your fast is over, you now have a 8 hour window.")
        msg['Subject'] = 'Break Fast'
        msg['From'] = my_email
        msg['To'] = send_to
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, "vecjkbgzfbsufymx")
            connection.sendmail(my_email, send_to, msg.as_string())

    elif reps %2 == 0:
        count_down(BREAK_FAST*3600)
        timer_label.config(text="Eat Window", fg=RED)
        msg = MIMEText("Your fast is over, you now have a 8 hour window.")
        msg['Subject'] = 'Break Fast'
        msg['From'] = my_email
        msg['To'] = send_to
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, "vecjkbgzfbsufymx")
            connection.sendmail(my_email, send_to, msg.as_string())
    else:
        count_down(FAST_HOUR*3600)
#-----------------------------CountDown--------------------------------------------------
def count_down(count):
    count_hour = math.floor(count/3600)
    count_min = math.floor(count/960)
    count_sec = count%60

    if count_sec<10:
     count_sec =f"0{count_sec}"
    if count_min <10:
        count_min =f"0{count_min}"
    if count_hour <10:
        count_hour =f"0{count_hour}"
    canvas.itemconfig(timer_text, text=f"{count_hour}:{count_min}:{count_sec}")
    if count >0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()
#-----------------------------UI-----------------------------------------------------------
window = Tk()
window.title("TechManGenius's Intermittent Fasting Timer")
window.config(padx=100,pady=50,bg=YELLOW)
canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.grid(column=1, row=1)
fasting_img = ImageTk.PhotoImage(Image.open("images/fasting.png"))
canvas.create_image(100, 112, image=fasting_img)
eating_img = ImageTk.PhotoImage(Image.open("images/salad.jpg"))
timer_label = Label(text="Fasting", fg=GREEN, font=("Arial", 15,"bold"), bg=YELLOW, highlightthickness=0 )
timer_label.grid(column=1, row=0)
timer_text=canvas.create_text(100,130, text="00:00:00", fill="orange", font=(FONT_NAME, 25, "bold"))
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command = reset_timer)
reset_button.grid(column=3, row=2)
window.mainloop()
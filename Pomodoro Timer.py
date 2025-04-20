import tkinter as tk

# Simple Pomodoro Timer for beginners with custom colors
work_min = 25  # minutes for work session
break_min = 5  # minutes for break session

timer_id = None
paused = False
stopped = True
remaining = 0

def countdown():
    global remaining, timer_id
    mins = remaining // 60
    secs = remaining % 60
    label.config(text="Work: " + str(mins).zfill(2) + ":" + str(secs).zfill(2))
    if remaining > 0 and not stopped:
        if not paused:
            remaining -= 1
            timer_id = root.after(1000, countdown)
    elif remaining == 0 and not stopped:
        start_break()

def start():
    global remaining, stopped, paused
    if not stopped:
        return  # do nothing if timer is running
    stopped = False
    paused = False
    remaining = work_min * 60
    start_btn.config(state="disabled")
    pause_btn.config(state="normal")
    restart_btn.config(state="normal")
    countdown()

def start_break():
    global remaining
    remaining = break_min * 60
    label.config(text="Break: 00:00")
    countdown_break()

def countdown_break():
    global remaining, timer_id
    mins = remaining // 60
    secs = remaining % 60
    label.config(text="Break: " + str(mins).zfill(2) + ":" + str(secs).zfill(2))
    if remaining > 0 and not stopped:
        if not paused:
            remaining -= 1
            timer_id = root.after(1000, countdown_break)
    elif remaining == 0 and not stopped:
        finish()

def pause_resume():
    global paused, timer_id
    if stopped:
        return
    if not paused:
        paused = True
        if timer_id:
            root.after_cancel(timer_id)
        pause_btn.config(text="Resume")
    else:
        paused = False
        pause_btn.config(text="Pause")
        countdown()

def restart():
    global timer_id, paused, stopped, remaining
    if timer_id:
        root.after_cancel(timer_id)
    paused = False
    stopped = True
    remaining = 0
    label.config(text="Ready to start")
    start_btn.config(state="normal")
    pause_btn.config(state="disabled", text="Pause")
    restart_btn.config(state="disabled")

def finish():
    global stopped
    stopped = True
    label.config(text="Session complete!")
    start_btn.config(state="normal")
    pause_btn.config(state="disabled")
    restart_btn.config(state="normal")

# Setup GUI
root = tk.Tk()
root.title("Pomodoro Timer")
root.resizable(False, False)
root.configure(bg='black')  # background color

label = tk.Label(root, text="Ready to start", font=("Helvetica", 24), fg='yellow', bg='black')
label.pack(pady=20)

frame = tk.Frame(root, bg='black')
frame.pack(pady=10)

btn_config = {'fg': 'yellow', 'bg': 'black', 'activebackground': 'gray20'}
start_btn = tk.Button(frame, text="Start", width=10, command=start, **btn_config)
start_btn.pack(side="left", padx=5)

pause_btn = tk.Button(frame, text="Pause", width=10, state="disabled", command=pause_resume, **btn_config)
pause_btn.pack(side="left", padx=5)

restart_btn = tk.Button(frame, text="Restart", width=10, state="disabled", command=restart, **btn_config)
restart_btn.pack(side="left", padx=5)

exit_btn = tk.Button(frame, text="Exit", width=10, command=root.destroy, **btn_config)
exit_btn.pack(side="left", padx=5)

root.mainloop()

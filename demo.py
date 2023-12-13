import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar  # Make sure to install tkcalendar: pip install tkcalendar

def get_calendar():
    def set_date():
        selected_date = cal.get_date()
        entry_date.delete(0, tk.END)
        entry_date.insert(0, selected_date)
        top.destroy()

    top = tk.Toplevel(root)
    cal = Calendar(top, selectmode='day', year=2023, month=1, day=1)
    cal.pack(padx=10, pady=10)
    btn_select = tk.Button(top, text="Select Date", command=set_date)
    btn_select.pack(pady=10)

def submit_info():
    user_info = {
        "Name": entry_name.get(),
        "Birthday": entry_date.get(),
        # Add more fields similarly
    }
    messagebox.showinfo("User Information", f"Submitted Information: \n{user_info}")

root = tk.Tk()
root.title("User Information")

# Function to create information row
def create_info_row(label_text, entry_widget, button_command=None):
    frame = tk.Frame(root)
    frame.pack(fill=tk.X, padx=10, pady=5)

    label = tk.Label(frame, text=label_text)
    label.pack(side=tk.LEFT)

    entry_widget.pack(side=tk.LEFT)

    if button_command:
        button = tk.Button(frame, text="Calendar", command=button_command)
        button.pack(side=tk.LEFT, padx=5)

# Name row
frame_name = tk.Frame(root)
frame_name.pack(fill=tk.X, padx=10, pady=5)

label_name = tk.Label(frame_name, text="Name:")
label_name.pack(side=tk.LEFT)

entry_name = tk.Entry(frame_name)
entry_name.pack(side=tk.LEFT)

# Birthday row
frame_birthday = tk.Frame(root)
frame_birthday.pack(fill=tk.X, padx=10, pady=5)

label_birthday = tk.Label(frame_birthday, text="Birthday:")
label_birthday.pack(side=tk.LEFT)

entry_date = tk.Entry(frame_birthday)
entry_date.pack(side=tk.LEFT)

btn_calendar = tk.Button(frame_birthday, text="Calendar", command=get_calendar)
btn_calendar.pack(side=tk.LEFT, padx=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_info)
submit_button.pack(pady=10)

root.mainloop()

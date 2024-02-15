import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pickle

wi = 650
hi = 400
col = 3
r = 0
binding_identifier = None  # Initialize binding identifier

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def saveto_file(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def on_enter_key1(roots):
    get_input_count(roots)

def on_enter_key2(roots):
    get_input_value(roots)

def yes(roots):
    labelyesno.grid_forget()
    buttonyes.grid_forget()
    buttonno.grid_forget()

    global entry_count
    global entry_value
    global submit_button
    global label
    global input_entries
    global label_count
    global button_count

    label_count = ttk.Label(roots, text="Enter number of Light Posts:")
    label_count.grid(row=0 + r, column=col, pady=10)

    # Create an entry widget for input count
    entry_count = ttk.Entry(roots, background="white", width=30)
    entry_count.grid(row=1 + r, column=col, pady=10)

    # Create a button to get the input count
    button_count = ttk.Button(roots, bootstyle=SUCCESS, text="Submit", command=lambda:get_input_count(roots))
    button_count.grid(row=2 + r, column=col, pady=10)
    global binding_identifier
    binding_identifier = roots.bind('<Return>', lambda _: on_enter_key1(roots))

    # List to store input values
    input_entries = []

    # Label for indicating the current input
    label = ttk.Label(roots, text="")
    label.grid(row=0 + r, column=col, pady=5)

    # Entry widget for input value
    entry_value = ttk.Entry(roots, width=30)

    # Button to get the next value
    submit_button = ttk.Button(roots, bootstyle=SUCCESS, text="Submit", state=ttk.DISABLED)
    submit_button.grid_forget()

    # Counter for the current input index
    global current_index
    current_index = 0

def no(roots):
    roots.after(1000, roots.destroy)

def get_input_count(roots):
    try:
        global input_count
        input_count = int(entry_count.get())
        label_count.grid_forget()
        submit_button.grid(row=4 + r, column=col, pady=10)
        create_input_boxes(roots, input_count)
    except ValueError:
        label_result = ttk.Label(roots, text="")
        label_result.config(text="Please enter a valid number.")
        label_result.grid(row=5 + r, column=col, pady=10)

def create_input_boxes(roots, count):
    entry_value.grid_forget()
    submit_button.grid_forget()
    global current_index
    current_index = 0

    if count > 0:
        label.config(text=f"Enter IP Address of LP 1")
        entry_value.grid(row=1 + r, column=col, pady=5)
        submit_button.config(command=lambda: get_input_value(roots), state=ttk.NORMAL)
        submit_button.grid(row=2 + r, column=col, pady=10)
        global binding_identifier
        roots.bind('<Return>', lambda _: on_enter_key2(roots))

def confirm(roots):
    saveto_file(filename='espip.pkl', data=input_entries)
    roots.after(1000, roots.destroy)

def edit(roots):
    roots.after(1000, roots.destroy)
    setup()

def get_input_value(roots):
    global current_index
    current_index += 1
    current_value = entry_value.get()
    input_entries.append(current_value)
    entry_value.delete(0, ttk.END)  # Clear the entry box

    if current_index < input_count:
        label.config(text=f"Enter IP Address of LP {current_index + 1}")
    elif current_index >= input_count:
        entry_value.delete(0, ttk.END)
        entry_value.destroy()
        entry_count.destroy()
        submit_button.destroy()
        button_count.destroy()

        if len(input_entries) > 4:
            wi = 650

        for i in range(len(input_entries)):
            label_result = ttk.Label(roots, text=f"You entered The IP Address of LP/{i + 1} is: {input_entries[i]}\n")
            label_result.grid(row=i + r, column=col, pady=0, padx=1)

        label_result = ttk.Label(roots, bootstyle=SUCCESS, text=f"Press Confirm to Continue")
        label_result.grid(row=i + r + 1, column=col, pady=0)
        roots.rowconfigure(i + r + 1, minsize=0)
        a = i + r + 1

        buttonconfirm = ttk.Button(roots, bootstyle="success-outline", text="Confirm", command=lambda: confirm(roots))
        buttonconfirm.grid(row=a + 1, column=3, pady=0)

        buttonedit = ttk.Button(roots, bootstyle="success-outline", text="Edit", command=lambda: edit(roots))
        buttonedit.grid(row=a + 1, column=4, pady=0)

        # Unbind the '<Return>' event using the saved binding identifier
        roots.unbind('<Return>', binding_identifier)

def setup(roots):
    global labelyesno
    global buttonyes
    global buttonno
    global canvas
    #roots=tk.Tk()
    local_style = ttk.Style()
    local_style.theme_use("darkly")
    roots.title("IP Address Setup")
    icon_path = "icon.ico"
    roots.iconbitmap(icon_path)
    roots.attributes("-fullscreen", False)
    roots.resizable(False, False)

    canvas = ttk.Canvas(roots, width=wi, height=hi, bg="white")
    canvas.grid(row=0, column=0, padx=10, rowspan=7, columnspan=7, pady=0)
    center_window(roots, wi, hi)

    labelyesno = ttk.Label(roots, bootstyle=SUCCESS, text="Do you want to Enter New IP Address:")
    labelyesno.grid(row=0 + r, column=3, pady=0)

    buttonyes = ttk.Button(roots, bootstyle="success-outline", text="Yes", command=lambda: yes(roots))
    buttonyes.grid(row=1 + r, column=1, pady=0)

    buttonno = ttk.Button(roots, bootstyle="success-outline", text="No", command=lambda: no(roots))
    buttonno.grid(row=1 + r, column=4, pady=0)

    roots.mainloop()
    return 1
# Start the program
if __name__ == "__main__":
    setup(tk.Tk())

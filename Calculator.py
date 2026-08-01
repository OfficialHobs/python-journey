import tkinter

# an ezample of nested list--- A list inside another list
buttons_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

# keep track of top items and right items
right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(buttons_values)  # how many rows are there = 5 rows
# column - count the number of item on first row
column_count = len(buttons_values[0])

color_ash = "#D4D4D2"
color_white = "white"
color_orange = "#FF9500"
color_grey = "#505050"
color_black = "#1C1C1C"

# creating a window/interface
windows = tkinter.Tk()
windows.title("calculator")
windows.resizable(False, False)  # (width=false, height=false)

frame = tkinter.Frame(windows)  # we are put a frame inside the (windows area)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black,
                      # insert label into frame and other properties
                      foreground=color_white, anchor="e")
label.grid(row=0, column=0, columnspan=column_count,
           sticky="we")  # "we"==west side


def button_clicked(value):
    pass


for row in range(row_count):  # for each item in row count// for each list in row count
    # for each item in column count// for each item in each row count list
    for column in range(column_count):
        # value is == each row and the item in row [colmn count]
        value = buttons_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        button.grid(row=row+1, column=column)

        if value in top_symbols:
            button.config(foreground=color_black, background=color_ash)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_grey)

frame.pack()  # pack all items to fit a size

# center our app window to screen
windows.update()
windows_width = windows.winfo_width()
windows_height = windows.winfo_height()
screen_width = windows.winfo_screenwidth()
screen_height = windows.winfo_screenheight()

windows_x = int((screen_width/2)-(windows_width/2))
windows_y = int((screen_height/2)-(windows_height/2))

windows.geometry(f"{windows_width}x{windows_height}+{windows_x}+{windows_y}")


windows.mainloop()  # keep windows running as program runs

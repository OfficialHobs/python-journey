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

color_light_blue = "#205b7a"
color_sky_blue = "#a2bbcf"
color_navy_blue = "#142f44"
color_Ash_blue = "#1d3849"
color_black = "#000000"

# creating a window/interface
windows = tkinter.Tk()
windows.title("calculator")
windows.resizable(False, False)  # (width=false, height=false)

frame = tkinter.Frame(windows)  # we are put a frame inside the (windows area)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black,
                      foreground=color_sky_blue)  # insert label into frame and other properties
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

frame.pack()  # pack all items to fit a size


windows.mainloop()  # keep windows running as program runs

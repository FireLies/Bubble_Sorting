from tkinter import *
from random import randint

'''
variables description:

horizon -> the base of the line (x0) equal to x1 and width-1
length  -> the length of each line (y1)
lines   -> an array containing lengths of each line
line    -> a single line in lines[]
'''


def generate():

    canvas.delete('all')

    horizon, lines = width-1, []
    for _ in range(width):
        length = randint(0, height)
        canvas.create_line(horizon, height, horizon, length, fill="#0278D7", width=1)
        lines.append(length)
        horizon -= 1

    button.configure(text="Sort", command=sort)
    return lines, width-1


def sort():

    lines, horizon = generate()

    canvas.delete('all')
    button['state'] = DISABLED

    # Bubble Sorting algorithm
    for i in range(len(lines)):
        for j in range(len(lines) - i - 1):
            if lines[j] > lines[j + 1]:
                lines[j], lines[j + 1] = lines[j + 1], lines[j]

    # Visualizing the output
    for line in range(len(lines)):
        canvas.create_line(horizon, height, horizon, lines[line], fill="#0278D7", width=1)
        canvas.update()
        horizon -= 1

    button['state'] = NORMAL
    button.configure(text="Generate array", command=generate)


width, height = 760, 400

window = Tk()
window.title("Bubble Sorting Visualization")
window.resizable(False, False)

button = Button(window, text="Sort", relief=RIDGE, command=sort)
button.pack(side=BOTTOM, anchor=S, fill=X, padx=2, pady=2)

canvas = Canvas(width=width, height=height, background="#072E50", highlightthickness=0)
canvas.pack(padx=2)
generate()

window.mainloop()

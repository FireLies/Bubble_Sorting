from tkinter import *
import random


def generate():

    canvas.delete("all")

    lines = []
    x0, y0 = width, height
    for _ in range(width):
        y1 = random.randint(0, height)
        canvas.create_line(x0, y0, x0, y1, fill="#0278D7", width=1)
        lines.append(y1)    # Store line length in a list
        x0 -= 1

    x0 = width

    button['state'] = NORMAL
    button.configure(text="Sort", command=sort)
    return lines, x0, y0


def sort():

    lines, x0, y0 = generate()
    canvas.delete("all")
    button['state'] = DISABLED

    # Bubble Sorting algorithm
    for i in range(len(lines)):
        for j in range(len(lines) - i - 1):
            if lines[j] > lines[j + 1]:
                lines[j], lines[j + 1] = lines[j + 1], lines[j]

    # Visualizing the output
    for line in range(len(lines)):
        canvas.create_line(x0, y0, x0, lines[line], fill="#0278D7", width=1)
        x0 -= 1

        canvas.update()

    button['state'] = NORMAL
    button.configure(text="Generate array", command=generate)


width, height = 660, 400

window = Tk()
window.title("Bubble Sorting Visualization")
window.resizable(False, False)

button = Button(window, text="Sort", relief=RIDGE, command=sort)
button.pack(side=BOTTOM, anchor=S, fill=X, padx=2, pady=2)

canvas = Canvas(width=width, height=height, background="#072E50", highlightthickness=0)
canvas.pack(padx=2)
generate()

window.mainloop()

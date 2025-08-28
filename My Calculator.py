from tkinter import *
from math import *

# ... Functions ...

def BackSpace():
    ex = screen.get()
    if ex:
        ex = ex[:-1]
        screen.delete(0, END)
        screen.insert(0, ex)

def getvals(event):
    value = event.widget.cget('text')
    if value == 'AC':
        sc_variable.set('')
    elif value == '=':
        try:
            ex = screen.get()
            ex = ex.replace('÷', '/')
            ex = ex.replace('%', '/100')
            if 'sin' in ex:
                ex = ex.replace('sin', 'sin(radians')
                ex += ')'
            elif 'cos' in ex:
                ex = ex.replace('cos', 'cos(radians')
                ex += ')'
            elif 'tan' in ex:
                ex = ex.replace('tan', 'tan(radians')
                ex += ')'
            result = eval(ex)
            sc_variable.set(result)
        except Exception:
            sc_variable.set('Error')
    else:
        sc_variable.set(sc_variable.get() + value)

# ... Colors & Fonts ...

BG_COLOR = "#2e2e2e"
DISPLAY_COLOR ="#1c1c1c"
BUTTON_COLOR = "#3e3e3e"
OPERATOR_COLOR = "#fe9505"
FUNCTION_COLOR = "#5bc0de"
TEXT_COLOR = "white"
BACK_COLOR = "#d9534f"
FONT = ('Segoe UI', 16, 'bold')

# ... Main UI ...

root = Tk()
root.geometry('375x480')
root.title('My Calculator')
root.config(bg=BG_COLOR)
root.resizable(False, False)

# ... Display Screen ...

sc_variable = StringVar()
screen = Entry(root, textvariable=sc_variable, font=('Segoe UI', 28, 'bold'),
               fg=TEXT_COLOR, bg=DISPLAY_COLOR, borderwidth=10, relief=FLAT, justify=RIGHT)
screen.pack(pady=10, padx=10, fill=X)

# ... Button Configuration Function ...

def make_button(frame, text, color, row, col, cmd=None):
    btn = Button(frame, text=text, font=FONT, fg=TEXT_COLOR, bg=color,
                 width=3, height=1, borderwidth=0, padx=10, pady=10)
    btn.grid(row=row, column=col, padx=5, pady=5)
    if cmd:
        btn.config(command=cmd)
    else:
        btn.bind('<Button-1>', getvals)

# ... Create Button Rows ...

btn_texts = [
    [('AC', OPERATOR_COLOR), ('(', OPERATOR_COLOR), (')', OPERATOR_COLOR), ('÷', OPERATOR_COLOR), ('←', BACK_COLOR)],
    [('7', BUTTON_COLOR), ('8', BUTTON_COLOR), ('9', BUTTON_COLOR), ('*', OPERATOR_COLOR), ('sin', FUNCTION_COLOR)],
    [('4', BUTTON_COLOR), ('5', BUTTON_COLOR), ('6', BUTTON_COLOR), ('-', OPERATOR_COLOR), ('cos', FUNCTION_COLOR)],
    [('1', BUTTON_COLOR), ('2', BUTTON_COLOR), ('3', BUTTON_COLOR), ('+', OPERATOR_COLOR), ('tan', FUNCTION_COLOR)],
    [('.', OPERATOR_COLOR), ('0', BUTTON_COLOR), ('00', OPERATOR_COLOR), ('%', OPERATOR_COLOR), ('=', OPERATOR_COLOR)],
]

for row_index, row_values in enumerate(btn_texts):
    f = Frame(root, bg=BG_COLOR)
    f.pack()
    for col_index, (text, color) in enumerate(row_values):
        if text == '←':
            make_button(f, text, color, row=0, col=col_index, cmd=BackSpace)
        else:
            make_button(f, text, color, row=0, col=col_index)


root.mainloop()

import tkinter as tk
import math
from gui.styles import *

BUTTON_LAYOUT = [
    ("sin", 2, 0, "sci"), ("cos", 2, 1, "sci"), ("tan", 2, 2, "sci"),
    ("log", 2, 3, "sci"), ("√",   2, 4, "sci"),
    ("7",  3, 0, "num"),  ("8",  3, 1, "num"),  ("9",  3, 2, "num"),
    ("/",  3, 3, "op"),   ("C",  3, 4, "clear"),
    ("4",  4, 0, "num"),  ("5",  4, 1, "num"),  ("6",  4, 2, "num"),
    ("*",  4, 3, "op"),   ("⌫",  4, 4, "op"),
    ("1",  5, 0, "num"),  ("2",  5, 1, "num"),  ("3",  5, 2, "num"),
    ("-",  5, 3, "op"),   ("^",  5, 4, "op"),
    ("0",  6, 0, "num"),  (".",  6, 1, "num"),  ("=",  6, 2, "equal"),
    ("+",  6, 3, "op"),   ("n!", 6, 4, "sci"),
]

COLORS = {
    "num": BUTTON_NUMBER_COLOR,
    "op": BUTTON_OPERATOR_COLOR,
    "sci": "BUTTON_SCIENTIFIC_COLOR",
    "clear": "BUTTON_CLEAR_COLOR",
    "equal": "BUTTON_EQUAL_COLOR"
}

def setup_buttons(app):
    for (text, row, col, btype) in BUTTON_LAYOUT:
     cmd = lambda t=text: handle_click(app, t)
     btn = tk.Button(
        app.window,
        text=text,
        font=FONT_BUTTON if len(text) <= 2 else FONT_BUTTON_SMALL,
        bg=COLORS[btype],
        fg=TEXT_COLOR,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        relief="flat",
        command=cmd
     )
    btn.grid(row=row, column=col,
                 padx=BUTTON_PADDING, pady=BUTTON_PADDING)\

def handle_click(app, text): # Handle button clicks based on the button type. It checks the text of the button and calls the appropriate function to perform the action. For example, if the "C" button is clicked, it calls the _clear function to reset the display. If the "=" button is clicked, it calls the _calculate function to evaluate the expression. If a scientific function button is clicked, it calls the _scientific function with the corresponding function name. For number and operator buttons, it appends the text to the current display.
   if text == "C":
      _clear(app)
   elif text == "⌫":
      _backspace(app)       
   elif text == "=":
      _calculate(app)
   elif text in ["sin", "cos", "tan", "log", "√", "n!"]:
      _scientific(app, text)
   else:
      _append(app, text)       

def _append(app, text): # Append the clicked button's text to the current display. If the current display is "0", it replaces it with the new text. Otherwise, it concatenates the new text to the existing display. Finally, it updates the display with the new text.
    if app.current_input == "0" and text.isdigit():
        app.current_input = text
    else:
        app.current_input += text # Append the new text to the existing input 
        app.update_display(app.current_input)

def _clear(app): # Clear the display by resetting it to "0". This function is called when the "C" button is clicked, allowing the user to start a new calculation.
    app.current_input = ""
    app.update_display("0")    

def _backspace(app): # Remove the last character from the current input in the display. This function is called when the "⌫" button is clicked, allowing the user to correct mistakes by deleting the last entered character. If the input becomes empty after backspacing, it resets to "0".
    app.current_input = app.current_input[:-1]
    app.update_display(app.current_input or "0")

def _calculate(app): # Evaluate the expression in the display and show the result. If the expression is invalid, it shows an error message.
    try:
        expression = app.current_input.replace("^", "**") 
        result = eval(expression)
        result = round(result, 10)
        app.history_obj.add(app.current_input, str(result))
        app.history_label.config(text=f"{app.current_input} = {str(result)}")
        app.current_input = str(result)
        app.update_display(result)
    except ZeroDivisionError:
        app.update_display("Error: Division by zero")
        app.current_input = ""
    except Exception:
        app.update_display("Error")
        app.current_input = ""

def _scientific(app, func): # Perform scientific calculations based on the function button clicked. It retrieves the current value from the display, applies the corresponding mathematical function, and updates the display with the result. If there is an error during the calculation (e.g., invalid input), it shows an error message.
    try:
        x = float(app.current_input)
        if func == "sin": result = math.sin(math.radians(x))
        elif func == "cos": result = math.cos(math.radians(x))
        elif func == "tan": result = math.tan(math.radians(x))
        elif func == "log": result = math.log10(x)
        elif func == "√": result = math.sqrt(x)
        elif func == "n!": result = math.factorial(int(x))
        result = round(result, 10)
        app.history_obj.add(f"{func}({app.current_input})", str(result))
        app.history_label.config(text=f"{func}({x}) =")
        app.current_input = str(result)
        app.update_display(result)
    except Exception:
        app.update_display("Error")
        app.current_input = ""
        
            

        
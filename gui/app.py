import tkinter as tk
from gui.styles import *
from calculator.history import History

class CalculatorApp:    
    def __init__(self): 
        self.window = tk.Tk()
        self.window.title("Engineering Calculator")
        self.window.configure(bg=BACKGROUND_COLOR)
        self.window.resizable(False, False)

        # Initialize history
        self.current_history = ""
        self.history = History()

        # Create display
        self._build_history_display()
        self._build_main_display()

    def _build_history_display(self): # Create a label to display the history of calculations. It is styled with a specific font, background color, and text color. The label is aligned to the right and has a fixed width. It is placed in the first row of the grid layout, spanning all columns, with padding around it.
        self.history_label = tk.Label(
            self.window,
            text="",
            font=FONT_HISTORY,
            bg=BACKGROUND_COLOR,
            fg=HISTORY_COLOR,
            anchor="e",    
            width=35
        )
        self.history_label.grid(row=0, column=0, columnspan=4, 
                                padx=10, pady=(10, 0))

    def _build_main_display(self): # Create a label to display the current input and result of calculations. It is styled with a specific font, background color, and text color. The label is aligned to the right and has a fixed width. It is placed in the second row of the grid layout, spanning all columns, with padding around it.
        self.display = tk.Label( 
            self.window,
            text="0",
            font=FONT_DISPLAY,
            bg=DISPLAY_COLOR
            fg=TEXT_COLOR,
            anchor="e",
            width=20
            padx=15
        )
        self.display.grid(row=1, column=0, columnspan=5, 
                          padx=10, pady=(0, 10))
        
        def update_history(self, value):
            self.display.config(text=str(value))

        def run(self):
            self.window.mainloop()
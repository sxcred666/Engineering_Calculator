import tkinter as tk
from tkinter import ttk
import math
from gui.styles import *
from calculator.history import History
from calculator import basic, scientific


class CalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Engineering Calculator")
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.window.configure(bg=BACKGROUND_COLOR)
        self.window.resizable(False, False)

        # State
        self.current_input = "0"
        self.previous_input = ""
        self.operation = None
        self.should_reset = False
        self.history = History()
        self.second_mode = False        # for 2nd function button

        self._build_ui()
        self._bind_keyboard()

    # ─── UI BUILDING ──────────────────────────────────────────────────────────

    def _build_ui(self):
        """Build the entire UI"""
        self._build_header()
        self._build_display()
        self._build_buttons()

    def _build_header(self):
        """Top title bar"""
        header = tk.Frame(self.window, bg=BACKGROUND_COLOR)
        header.pack(fill=tk.X, padx=15, pady=(12, 0))

        tk.Label(
            header,
            text="ENG CALC",
            font=FONT_TITLE,
            bg=BACKGROUND_COLOR,
            fg=ACCENT_COLOR
        ).pack(side=tk.LEFT)

        # History button
        self.hist_btn = tk.Button(
            header,
            text="HISTORY",
            font=("Consolas", 9, "bold"),
            bg=BACKGROUND_COLOR,
            fg=HISTORY_COLOR,
            relief=tk.FLAT,
            bd=0,
            cursor="hand2",
            command=self._show_history
        )
        self.hist_btn.pack(side=tk.RIGHT)

    def _build_display(self):
        """Display area"""
        display_frame = tk.Frame(
            self.window,
            bg=DISPLAY_COLOR,
            highlightbackground=DISPLAY_BORDER,
            highlightthickness=1
        )
        display_frame.pack(fill=tk.X, padx=15, pady=10)

        # History / expression line
        self.history_label = tk.Label(
            display_frame,
            text="",
            font=FONT_HISTORY,
            bg=DISPLAY_COLOR,
            fg=HISTORY_COLOR,
            anchor="e",
            padx=15
        )
        self.history_label.pack(fill=tk.X, pady=(10, 0))

        # Main number display
        self.display = tk.Label(
            display_frame,
            text="0",
            font=FONT_DISPLAY,
            bg=DISPLAY_COLOR,
            fg=TEXT_COLOR,
            anchor="e",
            padx=15,
            pady=8
        )
        self.display.pack(fill=tk.X)

        # Mode indicator
        self.mode_label = tk.Label(
            display_frame,
            text="DEG",
            font=("Consolas", 9),
            bg=DISPLAY_COLOR,
            fg=ACCENT_COLOR,
            anchor="w",
            padx=15
        )
        self.mode_label.pack(fill=tk.X, pady=(0, 8))

    def _build_buttons(self):
        """Build all button rows"""
        btn_frame = tk.Frame(self.window, bg=BACKGROUND_COLOR)
        btn_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))

        # Configure grid columns equal width
        for col in range(5):
            btn_frame.grid_columnconfigure(col, weight=1, uniform="col")
        for row in range(8):
            btn_frame.grid_rowconfigure(row, weight=1, uniform="row")

        # Layout: (label, row, col, colspan, type, command_key)
        buttons = [
            # Row 0 — memory & clear row
            ("MC",   0, 0, 1, "mem",   "MC"),
            ("MR",   0, 1, 1, "mem",   "MR"),
            ("M+",   0, 2, 1, "mem",   "M+"),
            ("C",    0, 3, 1, "clear", "C"),
            ("⌫",   0, 4, 1, "clear", "BS"),

            # Row 1 — scientific row 1
            ("sin",  1, 0, 1, "sci",   "sin"),
            ("cos",  1, 1, 1, "sci",   "cos"),
            ("tan",  1, 2, 1, "sci",   "tan"),
            ("cot",  1, 3, 1, "sci",   "cot"),
            ("√",    1, 4, 1, "sci",   "sqrt"),

            # Row 2 — scientific row 2
            ("log",  2, 0, 1, "sci",   "log"),
            ("ln",   2, 1, 1, "sci",   "ln"),
            ("exp",  2, 2, 1, "sci",   "exp"),
            ("x!",   2, 3, 1, "sci",   "factorial"),
            ("xʸ",   2, 4, 1, "sci",   "power"),

            # Row 3 — scientific row 3
            ("π",    3, 0, 1, "sci",   "pi"),
            ("e",    3, 1, 1, "sci",   "euler"),
            ("x²",   3, 2, 1, "sci",   "square"),
            ("1/x",  3, 3, 1, "sci",   "reciprocal"),
            ("%",    3, 4, 1, "op",    "%"),

            # Row 4 — numbers + operators
            ("7",    4, 0, 1, "num",   "7"),
            ("8",    4, 1, 1, "num",   "8"),
            ("9",    4, 2, 1, "num",   "9"),
            ("÷",    4, 3, 1, "op",    "/"),
            ("mod",  4, 4, 1, "op",    "mod"),

            # Row 5
            ("4",    5, 0, 1, "num",   "4"),
            ("5",    5, 1, 1, "num",   "5"),
            ("6",    5, 2, 1, "num",   "6"),
            ("×",    5, 3, 1, "op",    "*"),
            ("(",    5, 4, 1, "op",    "("),

            # Row 6
            ("1",    6, 0, 1, "num",   "1"),
            ("2",    6, 1, 1, "num",   "2"),
            ("3",    6, 2, 1, "num",   "3"),
            ("−",    6, 3, 1, "op",    "-"),
            (")",    6, 4, 1, "op",    ")"),

            # Row 7
            ("+/−",  7, 0, 1, "num",   "negate"),
            ("0",    7, 1, 1, "num",   "0"),
            (".",    7, 2, 1, "num",   "."),
            ("+",    7, 3, 1, "op",    "+"),
            ("=",    7, 4, 1, "equal", "="),
        ]

        color_map = {
            "num":   (BUTTON_NUMBER_COLOR,     BUTTON_TEXT_COLOR),
            "op":    (BUTTON_OPERATOR_COLOR,   BUTTON_OPERATOR_TEXT),
            "sci":   (BUTTON_SCIENTIFIC_COLOR, BUTTON_OPERATOR_TEXT),
            "mem":   (BUTTON_MEMORY_COLOR,     BUTTON_TEXT_COLOR),
            "clear": (BUTTON_CLEAR_COLOR,      BUTTON_CLEAR_TEXT),
            "equal": (BUTTON_EQUAL_COLOR,      BUTTON_EQUAL_TEXT),
        }

        for (label, row, col, colspan, btn_type, cmd_key) in buttons:
            bg, fg = color_map.get(btn_type, (BUTTON_NUMBER_COLOR, BUTTON_TEXT_COLOR))
            font = FONT_BUTTON if len(label) <= 3 else FONT_BUTTON_SMALL

            btn = tk.Button(
                btn_frame,
                text=label,
                font=font,
                bg=bg,
                fg=fg,
                activebackground=bg,
                activeforeground=fg,
                relief=tk.FLAT,
                bd=0,
                cursor="hand2",
                command=lambda k=cmd_key: self._handle(k)
            )
            btn.grid(
                row=row, column=col, columnspan=colspan,
                padx=BUTTON_PADDING, pady=BUTTON_PADDING,
                sticky="nsew"
            )

            # Hover effects
            btn.bind("<Enter>", lambda e, b=btn, c=bg: b.config(bg=self._lighten(c)))
            btn.bind("<Leave>", lambda e, b=btn, c=bg: b.config(bg=c))

        # Memory storage
        self.memory = 0

    # ─── KEYBOARD BINDING ─────────────────────────────────────────────────────

    def _bind_keyboard(self):
        """Bind keyboard keys"""
        self.window.bind("<Key>", self._on_key)

    def _on_key(self, event):
        key = event.char
        keysym = event.keysym

        if key in "0123456789.":
            self._handle(key)
        elif key in "+-*/":
            self._handle(key)
        elif key == "%":
            self._handle("%")
        elif keysym == "Return":
            self._handle("=")
        elif keysym == "BackSpace":
            self._handle("BS")
        elif keysym == "Escape":
            self._handle("C")

    # ─── BUTTON HANDLER ───────────────────────────────────────────────────────

    def _handle(self, key):
        """Route button press to correct handler"""
        if key in "0123456789":
            self._append_digit(key)
        elif key == ".":
            self._append_dot()
        elif key in ("+", "-", "*", "/"):
            self._set_operation(key)
        elif key == "=":
            self._calculate()
        elif key == "C":
            self._clear()
        elif key == "BS":
            self._backspace()
        elif key == "negate":
            self._negate()
        elif key == "%":
            self._percent()
        elif key == "mod":
            self._set_operation("mod")
        elif key in ("sin", "cos", "tan", "cot", "sqrt", "log",
                     "ln", "exp", "factorial", "square", "reciprocal"):
            self._scientific(key)
        elif key == "power":
            self._set_operation("^")
        elif key == "pi":
            self._insert_constant(math.pi)
        elif key == "euler":
            self._insert_constant(math.e)
        elif key in ("MC", "MR", "M+"):
            self._memory(key)

    # ─── NUMBER INPUT ─────────────────────────────────────────────────────────

    def _append_digit(self, digit):
        if self.should_reset or self.current_input == "0":
            self.current_input = digit
            self.should_reset = False
        else:
            if len(self.current_input) < 15:
                self.current_input += digit
        self._refresh()

    def _append_dot(self):
        if self.should_reset:
            self.current_input = "0."
            self.should_reset = False
        elif "." not in self.current_input:
            self.current_input += "."
        self._refresh()

    def _negate(self):
        if self.current_input not in ("0", ""):
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
        self._refresh()

    def _percent(self):
        try:
            val = float(self.current_input)
            if self.previous_input and self.operation in ("+", "-"):
                prev = float(self.previous_input)
                result = prev * val / 100
            else:
                result = val / 100
            self.current_input = self._format(result)
            self.should_reset = True
            self._refresh()
        except Exception:
            self._show_error("Error")

    def _insert_constant(self, value):
        self.current_input = self._format(value)
        self.should_reset = False
        self._refresh()

    # ─── OPERATIONS ───────────────────────────────────────────────────────────

    def _set_operation(self, op):
        """Store operation and previous value"""
        if self.operation and not self.should_reset:
            self._calculate(update_history=False)

        self.previous_input = self.current_input
        self.operation = op

        display_op = {"*": "×", "/": "÷", "-": "−", "^": "^", "mod": "mod"}.get(op, op)
        self.history_label.config(text=f"{self._format_display(self.current_input)} {display_op}")
        self.should_reset = True

    def _calculate(self, update_history=True):
        """Perform calculation"""
        if not self.operation or (self.should_reset and self.operation):
            return

        try:
            prev = float(self.previous_input)
            curr = float(self.current_input)
            op = self.operation

            if op == "+":
                result = basic.add(prev, curr)
            elif op == "-":
                result = basic.subtract(prev, curr)
            elif op == "*":
                result = basic.multiply(prev, curr)
            elif op == "/":
                result = basic.divide(prev, curr)
                if result is None:
                    self._show_error("Cannot ÷ 0")
                    return
            elif op == "^":
                result = scientific.power(prev, curr)
            elif op == "mod":
                result = scientific.modulus(prev, curr)
                if result is None:
                    self._show_error("Mod by 0")
                    return

            if result is None:
                self._show_error("Error")
                return

            result = round(result, 10)
            expr = f"{self.previous_input} {op} {self.current_input}"

            if update_history:
                self.history.add_record(expr, str(result))
                display_op = {"*": "×", "/": "÷", "-": "−"}.get(op, op)
                self.history_label.config(
                    text=f"{self._format_display(self.previous_input)} {display_op} {self._format_display(self.current_input)} ="
                )

            self.current_input = self._format(result)
            self.operation = None
            self.should_reset = True
            self._refresh()

        except Exception:
            self._show_error("Error")

    # ─── SCIENTIFIC ───────────────────────────────────────────────────────────

    def _scientific(self, func):
        """Apply scientific function to current value"""
        try:
            x = float(self.current_input)
            result = None
            label = func

            if func == "sin":
                result = scientific.sin(x)
            elif func == "cos":
                result = scientific.cos(x)
            elif func == "tan":
                result = scientific.tan(x)
                if result is None:
                    self._show_error("Undefined")
                    return
            elif func == "cot":
                result = scientific.cot(x)
                if result is None:
                    self._show_error("Undefined")
                    return
            elif func == "sqrt":
                result = scientific.sqrt(x)
                if result is None:
                    self._show_error("Invalid input")
                    return
                label = "√"
            elif func == "log":
                result = scientific.log(x, 10)
                if result is None:
                    self._show_error("Invalid input")
                    return
            elif func == "ln":
                result = scientific.log(x)
                if result is None:
                    self._show_error("Invalid input")
                    return
            elif func == "exp":
                result = scientific.exp(x)
            elif func == "factorial":
                n = int(x)
                result = scientific.factorial(n)
                if result is None:
                    self._show_error("Invalid input")
                    return
                label = "!"
            elif func == "square":
                result = scientific.power(x, 2)
                label = "x²"
            elif func == "reciprocal":
                if x == 0:
                    self._show_error("Cannot ÷ 0")
                    return
                result = basic.divide(1, x)
                label = "1/x"

            result = round(result, 10)
            expr = f"{label}({x})"
            self.history.add_record(expr, str(result))
            self.history_label.config(text=f"{label}({self._format_display(self.current_input)}) =")
            self.current_input = self._format(result)
            self.should_reset = True
            self._refresh()

        except Exception:
            self._show_error("Error")

    # ─── MEMORY ───────────────────────────────────────────────────────────────

    def _memory(self, key):
        try:
            if key == "MC":
                self.memory = 0
                self.history_label.config(text="Memory cleared")
            elif key == "MR":
                self.current_input = self._format(self.memory)
                self.should_reset = False
                self._refresh()
            elif key == "M+":
                self.memory += float(self.current_input)
                self.history_label.config(text=f"M = {self._format(self.memory)}")
        except Exception:
            pass

    # ─── HISTORY WINDOW ───────────────────────────────────────────────────────

    def _show_history(self):
        """Show history popup"""
        win = tk.Toplevel(self.window)
        win.title("Calculation History")
        win.geometry("360x400")
        win.configure(bg=BACKGROUND_COLOR)
        win.resizable(False, False)

        tk.Label(
            win,
            text="HISTORY",
            font=("Consolas", 12, "bold"),
            bg=BACKGROUND_COLOR,
            fg=ACCENT_COLOR
        ).pack(pady=10)

        # Scrollable list
        frame = tk.Frame(win, bg=DISPLAY_COLOR)
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(
            frame,
            font=("Consolas", 11),
            bg=DISPLAY_COLOR,
            fg=TEXT_COLOR,
            selectbackground=ACCENT_COLOR,
            relief=tk.FLAT,
            bd=0,
            yscrollcommand=scrollbar.set
        )
        listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)

        records = self.history.get_all()
        if not records:
            listbox.insert(tk.END, "  No history yet")
        else:
            for rec in reversed(records):
                listbox.insert(tk.END, f"  {rec['expression']} = {rec['result']}")

        # Clear button
        tk.Button(
            win,
            text="CLEAR HISTORY",
            font=("Consolas", 10, "bold"),
            bg=BUTTON_CLEAR_COLOR,
            fg=BUTTON_CLEAR_TEXT,
            relief=tk.FLAT,
            bd=0,
            cursor="hand2",
            command=lambda: [self.history.clear(), win.destroy()]
        ).pack(pady=(0, 15), padx=15, fill=tk.X)

    # ─── HELPERS ──────────────────────────────────────────────────────────────

    def _clear(self):
        self.current_input = "0"
        self.previous_input = ""
        self.operation = None
        self.should_reset = False
        self.history_label.config(text="")
        self._refresh()

    def _backspace(self):
        if self.should_reset:
            return
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
        else:
            self.current_input = "0"
        self._refresh()

    def _format(self, value):
        """Format number for display — remove trailing zeros"""
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)

    def _format_display(self, text):
        """Shorten long numbers for history label"""
        if len(text) > 10:
            return text[:10] + "…"
        return text

    def _refresh(self):
        """Update main display"""
        text = self.current_input
        if len(text) > 14:
            # Shrink font for long numbers
            self.display.config(font=("Consolas", 24, "bold"), text=text)
        else:
            self.display.config(font=FONT_DISPLAY, text=text)

    def _show_error(self, msg):
        """Show error on display"""
        self.display.config(text=msg, font=("Consolas", 22, "bold"))
        self.current_input = "0"
        self.should_reset = True

    def _lighten(self, hex_color):
        """Lighten a hex color slightly for hover effect"""
        try:
            r = int(hex_color[1:3], 16)
            g = int(hex_color[3:5], 16)
            b = int(hex_color[5:7], 16)
            r = min(255, r + 25)
            g = min(255, g + 25)
            b = min(255, b + 25)
            return f"#{r:02x}{g:02x}{b:02x}"
        except Exception:
            return hex_color

    def run(self):
        self.window.mainloop()
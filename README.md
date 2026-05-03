# Engineering Calculator

A desktop engineering calculator built with **Python + tkinter**. Clean dark UI, full scientific function set, persistent history, and keyboard support.

---

## Features

- Basic arithmetic — `+` `−` `×` `÷`
- Scientific functions — `sin` `cos` `tan` `cot` `√` `log` `ln` `exp` `x!` `xʸ` `x²` `1/x`
- Constants — `π` and `e`
- Memory — `MC` `MR` `M+`
- Modulus and percent — `mod` `%`
- Calculation history — saved to `history.json`, viewable and clearable in-app
- Keyboard input — digits, operators, Enter, Backspace, Escape
- Error handling — friendly messages for division by zero, invalid input, undefined trig values

---

## Project Structure

```
engineering_calculator/
│
├── main.py                  # Entry point
├── requirements.txt         # Dependencies
├── README.md
├── history.json             # Auto-generated history file
│
├── calculator/
│   ├── __init__.py
│   ├── basic.py             # add, subtract, multiply, divide
│   ├── scientific.py        # sin, cos, tan, cot, sqrt, log, exp, factorial, power, modulus
│   └── history.py           # History class — saves/loads JSON
│
├── gui/
│   ├── __init__.py
│   ├── app.py               # Main window, all UI logic
│   └── styles.py            # Colors, fonts, sizes
│
└── tests/
    ├── __init__.py
    ├── test_basic.py
    └── test_scientific.py
```

---

## Installation

```bash
# 1. Clone the repo
git clone https://github.com/sxcred666/Engineering_Calculator.git
cd Engineering_Calculator

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
python main.py
```

**Requirements:** Python 3.10+, tkinter (bundled with Python)

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0–9` `.` | Number input |
| `+ - * /` | Arithmetic operators |
| `%` | Percent |
| `Enter` | Calculate `=` |
| `Backspace` | Delete last digit |
| `Escape` | Clear all `C` |

---

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

---

## What Changed in Latest Refactor

### `gui/app.py` — rewritten from scratch
- Added missing buttons: `log` `ln` `exp` `x!` `xʸ` `x²` `1/x` `cot` `mod` `%` `π` `e` `( )`
- Added memory: `MC` `MR` `M+`
- Added keyboard support
- Added history popup window with scroll and clear button
- Connected `history.py` — now actually saves every calculation
- Hover effects on all buttons
- Smart display — shrinks font for long numbers
- Removed all error `print()` calls — errors show on display instead

### `gui/styles.py` — modern dark theme
- Replaced Soviet theme with clean dark palette
- Purple accent `#6C63FF`, dark background `#0F0F13`
- Monospace `Consolas` font throughout

### `calculator/basic.py` and `calculator/scientific.py`
- Removed `print()` from all functions — GUI handles error display
- All functions return `None` on invalid input

### `calculator/history.py`
- Added `MAX_RECORDS = 1000` cap to prevent unbounded file growth
- No other changes — was already correct

---

## License

MIT

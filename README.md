# 📱 QR Code Generator

A Python-based QR Code Generator that allows users to create both standard QR codes and branded QR codes with a custom logo placed in the center.

This project combines QR code generation, image processing, file handling, menu-driven programming, and exception handling to create a practical real-world application.

---

# 🚀 Features

## 📌 Simple QR Code Generation

* Generate QR codes from:

  * URLs
  * Text
  * Contact Information
  * Any Custom Data
* Save QR codes as PNG files
* Automatically preview generated QR code

## 🎨 QR Code with Logo

* Insert custom logo in the center
* Automatic logo resizing
* Maintains QR code readability
* Generates branded QR codes
* Saves logo-based QR separately

## 🖥️ User Interface

* Menu-driven application
* Colored terminal output using Colorama
* Easy-to-use command-line interface
* Auto image preview support

## 🛡️ Error Handling

* Invalid menu selection handling
* Keyboard Interrupt support
* File-related error handling
* Input validation

---

# 📸 Menu Preview

```text
===================================
        QR Code Generator!
===================================

1 - Simple QR Code
2 - QR with Logo in Center
3 - Exit
```

---

# 📦 Modules Used

```python
import qrcode
from PIL import Image
from colorama import init, Fore, Style
```

| Module       | Purpose                 |
| ------------ | ----------------------- |
| qrcode       | Generate QR Codes       |
| Pillow (PIL) | Logo/Image Processing   |
| colorama     | Colored Terminal Output |

---

# 🧠 Concepts Used

This project helped practice:

* Python Modules
* Image Processing
* QR Code Generation
* File Handling
* Loops
* Conditional Statements
* Exception Handling
* User Input Validation
* Menu-Driven Applications

---

# 📂 Project Structure

```text
Project-8-QR-Code-Generator/
│
├── qr-code.py
├── README.md
└── sample_logo.png
```

---

# ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/basantjangra79/Project-8-QR-Code-Generator.git
```

### Move Into Project Directory

```bash
cd Project-8-QR-Code-Generator
```

### Install Required Packages

```bash
pip install qrcode[pil]
pip install pillow
pip install colorama
```

---

# ▶️ Run the Program

```bash
python qr-code.py
```

---

# 📌 Generate a Simple QR Code

### Example

```text
Enter Text or Link:
https://github.com

Enter File Name without PNG:
github_qr
```

### Output

```text
QR Code saved as github_qr.png
```

---

# 🎨 Generate QR Code with Logo

### Example

```text
Enter Text or Link:
https://github.com

Enter Logo Name [without PNG]:
logo

Enter File Name without PNG:
github
```

### Output

```text
QR Code saved as 'github_with_logo.png'
```

---

# 🖼️ How Logo Placement Works

The application:

1. Creates a QR code with high error correction.
2. Opens the selected logo image.
3. Resizes the logo to approximately 20% of the QR code size.
4. Calculates the center position.
5. Places the logo in the middle.
6. Saves the final branded QR code.

This allows scanners to read the QR code even with a logo present.

---

# ⚠️ Error Handling

### Invalid Menu Input

```text
Invalid Input! Try Again...
```

### User Exit

```text
QR Code Generator Closed by User
```

### Missing Logo File

If the logo image is not found, the program catches the error and displays an error message.

---

# 🎯 Learning Outcomes

Through this project, I practiced:

* Creating QR codes programmatically
* Working with external Python libraries
* Understanding image manipulation
* Handling files and directories
* Building interactive CLI applications
* Implementing exception handling
* Combining multiple libraries in a single project

---

# 🔮 Future Improvements

Possible upgrades for future versions:

* Custom QR Colors
* Custom Background Colors
* Transparent QR Codes
* Multiple Image Formats
* Batch QR Generation
* WiFi QR Generator
* Contact Card (vCard) QR Generator
* QR Code Scanner
* GUI Version using Tkinter
* Web Version using Flask

---

# 👨‍💻 Author

**Basant Jangra**

Python Learning Journey — Project #8

### Completed Projects

* Project 1 — Advance Mini Calculator
* Project 2 — Number Guessing Game
* Project 3 — Password Generator
* Project 4 — To-Do List Maker
* Project 5 — Age Calculator
* Project 6 — OTP Generator
* Project 7 — Calendar Generator
* Project 8 — QR Code Generator

GitHub:
https://github.com/basantjangra79

Instagram:
@Basantjangra79

---

## ⭐ If you found this project useful, consider starring the repository and following my Python learning journey.

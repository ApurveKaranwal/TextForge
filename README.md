# TextForge

### 🎨 A Python command-line utility for converting standard text input into creative, stylized ASCII art displays.

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)

---

### ✨ Features

* **Diverse Styles:** Utilizes the powerful `pyfiglet` library to offer a wide range of ASCII art fonts.
* **Command-Line Interface (CLI):** Simple, direct execution from your terminal.
* **Standard Input Support:** Easily pipe text from other programs or files.
* **Randomized Output:** Option to choose a random, fun font for quick creative flair.

---

### 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine.

#### Prerequisites

You need **Python 3.6 or newer** installed on your system.

#### Installation

1.  **Clone the repository** :

    ```bash
    git clone https://github.com/ApurveKaranwal/TextForge
    cd TextForge
    ```

2.  **Install the required dependencies:**

    This project requires the `pyfiglet` library.

    ```bash
    pip install pyfiglet
    ```

3.  **Ensure `TextForge.py` is executable** (if necessary):

    ```bash
    chmod +x TextForge.py
    ```

---

### 💡 Usage

The basic command structure is designed to be simple and intuitive.

#### Basic Text Conversion

To convert a single string of text, run the script and pass the text as an argument.

```bash
python textforge.py
```
![Basic TextForge Output](https://github.com/ApurveKaranwal/TextForge/blob/main/1.png)

![Basic TextForge Output](https://github.com/ApurveKaranwal/TextForge/blob/main/2.png)

![Basic TextForge Output](https://github.com/ApurveKaranwal/TextForge/blob/main/3.png)

### Using a Specific Font
```bash
python textforge.py --font Slant
```
![Basic TextForge Output](https://github.com/ApurveKaranwal/TextForge/blob/main/4.png)

### 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request



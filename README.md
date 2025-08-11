# DayZ-Trader-Converter-Script

# How to Use This DayZ Trader Converter Script

This repository provides a simple, drag-and-drop Python script for converting DayZ `types.xml` or classnames lists into popular trader formats: **Dr. Jones**, **Trader Plus**, and **Expansion Markets**.

---

## 📁 Setup

1. **Download or Clone This Repository**
    - Click the green "Code" button above and select "Download ZIP", then extract the files.
    - Or clone via Git:
      ```sh
      git clone https://github.com/yourusername/yourrepo.git
      ```

2. **Prepare Your Input Files**
    - Place your `types.xml` and/or a classnames file (e.g., `classnames.txt`) in the same folder as the script.
    - Make sure your file is named exactly `types.xml` (not `types.xml.xml`).

3. **Install Python (if needed)**
    - This script requires Python 3.x. Download from [python.org](https://www.python.org/downloads/).

---

## ▶️ Usage

### **Method 1: Double-Click**

- Place the script and your `types.xml` or `classnames.txt` in the same folder.
- Double-click `dayz_trader_converter.py`.
- Follow the on-screen prompts to select output format and file name.

### **Method 2: Command Line**

1. Open a terminal or command prompt in the script's folder.
2. Run:
    ```sh
    python dayz_trader_converter.py
    ```
3. Follow the interactive prompts.

---

## 📝 Output Formats

- **Dr. Jones:**  
  Outputs lines like:  
  ```
  ClassName,0,1,-1,-1,0,0
  ```

- **Trader Plus:**  
  Outputs lines like:  
  ```
  ClassName,100,10,1,100,Category
  ```

- **Expansion Market:**  
  Outputs JSON-style entries for each item.

---

## ⚠️ Troubleshooting

- **Not detecting your file?**
    - Make sure your `types.xml` is not accidentally named `types.xml.xml`.
    - Enable file extensions in Windows Explorer for clarity.
    - The script prints the current folder and files it detects at startup.

- **Need a different format or custom fields?**  
  Edit the script's formatting functions to suit your server’s needs!

---

## 💡 Contributing

Pull requests and suggestions are welcome! Fork the repo, make your changes, and open a PR.

---

## 📜 License

This project is open source under the MIT License.


# 🖥️ Advanced Keylogger in Python

## 🔍 About  
This is a powerful keylogger built using Python that not only records keystrokes but also monitors various system activities such as audio recording, clipboard tracking, screenshots, and camera usage. The collected data is securely stored and shared with an admin email at specified intervals.  

⚠ **Disclaimer**  
This project is strictly for **educational and ethical purposes**. Unauthorized usage for spying or data theft is illegal and punishable by law. Use this tool responsibly and only on systems you have explicit permission to monitor.  

---

## 🚀 Features  
- ✅ **System Information Retrieval**: Captures system details such as OS, IP address, and hardware information.  
- ✅ **Keystroke Logging**: Records all keystrokes and saves them securely.  
- ✅ **Smart Audio Recording**: Waits for the microphone to activate and records audio only when the sound exceeds a certain RMS threshold.  
- ✅ **Periodic Screenshots**: Takes screenshots of the screen at regular intervals.  
- ✅ **Camera Activity Detection**: Detects when the camera is activated and records video for the next 15 seconds.  
- ✅ **Clipboard Monitoring**: Detects `Ctrl + C` presses and stores copied data in a file.  
- ✅ **Data Encryption**: Encrypts all text-based files to enhance security.  
- ✅ **Database Storage**:  
  - Stores system info, screenshots, and audio in **MySQL database**.  
  - Saves video recordings, log files, and clipboard data in **Firebase**.  
- ✅ **Email Sharing**: Automatically sends all collected data to an admin email at specified time intervals.  

---

## 🛠️ Requirements  
- Python 3.x  
- Python Packages:  
  ```
  pynput, sounddevice, numpy, wave, opencv-python, pyaudio, cryptography, firebase-admin, pyrebase, mysql-connector-python, smtplib, win32clipboard, pyautogui, socket, platform, requests, psutil, threading
  ```
- MySQL database (configured with your credentials)  
- Firebase Storage setup  

---

## 🔧 Installation & Usage  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Subhranshu-Patra29/keyloggerPython.git
   cd keylogger
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MySQL database**  
   - Create a MySQL database and configure the credentials in the script.  
   - Use the `keylogger.sql` file to create all the required tables.  
   - Ensure tables for storing system info, screenshots, and audio logs are created.  

4. **Set up Firebase**  
   - Configure Firebase Storage and set up authentication.  
   - Update Firebase credentials in the script.  

5. **Run the keylogger**  
   ```bash
   python keylogger.py
   ```

6. **Stop the keylogger**  
   - Use `Ctrl + C` in the terminal  
   - Or close the script from the task manager  

---

## 📁 Data Storage Details  

| Data Type          | Storage Location |
|--------------------|-----------------|
| System Info       | MySQL database   |
| Screenshots       | MySQL database   |
| Audio Recordings  | MySQL database   |
| Camera Recordings | Firebase Storage |
| Keystrokes        | Encrypted log file |
| Clipboard Data    | Firebase Storage |
| Log File          | Firebase Storage |

---

## 🔄 Future Improvements  
- Add a stealth mode for better background execution.  
- Improve encryption techniques.  
- Implement a cloud-based dashboard for real-time monitoring.  

---

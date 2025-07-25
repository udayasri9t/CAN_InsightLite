# 🚗 CAN Insight Lite

**CAN Insight Lite** is a simulation-based vehicle diagnostics dashboard designed to visualize, analyze, and log Controller Area Network (CAN) messages in real time. Built with Python and Dash, it helps users monitor simulated vehicle behavior without needing physical automotive hardware.

---

## 📸 Live Preview

![Dashboard Preview](assets/demo_screenshot.png) <!-- Add your screenshot or GIF here -->

---

## 🧠 Features

- 📡 **CAN Simulator**: Generates realistic CAN messages with varying vehicle data.
- 📈 **Real-Time Dashboard**: Live graphs for vehicle speed, RPM, temperature, etc.
- 🔍 **Anomaly Detection**: Highlights abnormal behavior using threshold logic.
- 🧾 **Log to CSV**: Auto-saves all CAN data to `/logs` folder.
- ⚠️ **Alert Cards**: Dynamic alerts shown for real-time anomalies.
- 📂 **GitHub-ready Structure**: Clean modular files and folders.

---

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python     | Backend logic & simulation |
| Dash       | Real-time dashboard UI |
| Plotly     | Interactive charts |
| Dash Bootstrap Components | UI styling |
| CSV        | Data logging |
| Git        | Version control |

---

## 🧰 Folder Structure

 Install Requirements
bash
Copy code
pip install -r requirements.txt


Launch the Dashboard
bash
Copy code
python src/can_dashboard.py
Then open your browser to http://127.0.0.1:8050

🧠 Tech Stack
Tool / Library	Purpose
Python	Core logic & simulation
Dash + Dash Bootstrap	UI & Web Dashboard
Plotly	Graphs & Interactions
CSV	Log storage
Git	Version control


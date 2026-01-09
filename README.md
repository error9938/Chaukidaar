# 🚜 Chaukidaar – AI Based Animal Detection & Repelling System

## 📌 Overview
**Chaukidaar** is an AI-powered agriculture security system developed to help
farmers detect and safely repel animals from farm boundaries using
computer vision and machine learning.

The system is designed to work on **low-cost hardware** such as laptops
with USB webcams, making it affordable and accessible for farmers.

---

## ❓ Problem Statement
Crop damage caused by animals is a major challenge for farmers.
Traditional protection methods are expensive, unsafe, or require
continuous human involvement.

---

## 💡 Proposed Solution
Chaukidaar uses a **YOLO-based deep learning model** to detect animals in
real time through a camera feed.  
When an animal is detected, the system triggers an **alert or repelling
mechanism**, helping farmers protect crops without harming wildlife.

---

## ⚙️ System Workflow
Camera → Frame Capture → YOLO Detection → Animal Classification →
Decision Logic → Alert / Repel

---

## 🧠 Key Features
- Real-time animal detection using AI
- YOLO-based object detection
- Works with USB webcam
- Cost-effective and scalable
- Safe and non-harmful animal repelling approach

---

## 🛠️ Technology Stack
- **Programming Language:** Python  
- **Libraries:** OpenCV, NumPy  
- **AI Model:** YOLO (Demo / Pre-trained Model)  
- **Hardware:** USB Webcam, Arduino (optional)  

---

## 📂 Project Structure
chaukidaar/
├── src/ # Python source code
├── model/ # YOLO model files
├── arduino/ # Arduino code (optional)
├── docs/ # Architecture & workflow
├── requirements.txt
├── README.md



---

## ▶️ How to Run
1. Clone the repository
2. Install dependencies using `requirements.txt`
3. Connect USB webcam
4. Run the Python detection script
5. System automatically detects animals and triggers alerts

---

## 🚀 Future Scope
- Android application integration
- Support for more animal classes
- Cloud-based monitoring dashboard
- SMS / mobile alert system

---

## 👨‍💻 Author
**error9938**  
Final Year Engineering Project – AI + Agriculture

---

## 📄 License
This project is developed for academic and learning purposes.

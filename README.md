# 🚜 Chaukidaar – AI Based Animal Detection & Repelling System

## 📌 Overview
Chaukidaar is an AI-powered agriculture security system developed to help farmers
detect and safely repel animals from farm boundaries using computer vision and
machine learning.

The system is designed to work on low-cost hardware such as laptops with USB
webcams, making it affordable and accessible for farmers.

---

## ❓ Problem Statement
Farmers suffer major crop losses due to animal intrusion, especially during night
hours. Manual guarding and fencing methods are expensive, unsafe, and unreliable.

---

## 💡 Proposed Solution
Chaukidaar uses a YOLO-based deep learning model to detect animals in real time.
When an animal is detected, the system triggers an alert (siren) and can interface
with external hardware for safe repelling without harming animals.

---

## ⚙️ System Workflow
Camera → Frame Capture → YOLO Detection → Animal Classification →
Alert / Repelling Mechanism

---

## 🧠 Key Features
- Real-time animal detection
- YOLOv8 model integration
- USB webcam support
- Audio alert using siren
- Low-cost and farmer-friendly design

---

## 🛠️ Technology Stack
- **Language:** Python
- **Libraries:** OpenCV, NumPy
- **AI Model:** YOLOv8
- **Hardware:** Webcam

---

## 📂 Project Structure
Chaukidaar/
├── chaukidaar.py
├── test_siren.py
├── siren.wav
├── yolov8n.pt
├── requirements.txt
├── Dockerfile
├── README.md

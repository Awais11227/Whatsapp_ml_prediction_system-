# 📱 WhatsApp ML Prediction System (Twilio + Flask + Machine Learning)

## 📌 Project Overview
This project demonstrates a real-time machine learning system integrated with WhatsApp using Twilio and Flask. Users send comma-separated numerical values via WhatsApp, and the system predicts outcomes using a trained ML model and returns results instantly.

---

## ⚙️ How It Works

1. User sends numbers (comma-separated) via WhatsApp  
2. Twilio webhook receives the message  
3. Flask backend processes the input  
4. Data is parsed and validated  
5. Features are scaled using `scaler.pkl`  
6. ML model predicts the output using `model.pkl`  
7. Result is sent back to WhatsApp via Twilio  

---

## 🧠 Machine Learning Pipeline

- Input: 11 numerical features (comma-separated)
- Preprocessing: Feature parsing + validation
- Scaling: StandardScaler
- Model: Trained classification model (e.g., Logistic Regression / Random Forest)
- Output: Class label + confidence score
## 📁 Project Structure

<img width="468" height="601" alt="image" src="https://github.com/user-attachments/assets/9e9d0d34-8d93-411d-829a-f76abdec00bd" />

---

## 🚀 How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt

### 2. Run Flask app
```bash
python app.py

### 3. Start ngrok tunnel
```bash
ngrok http 5000



### 4. Update Twilio webhook
```bash
https://your-ngrok-url/whatsapp

### 👨‍💻 Author
### Awais Manzoor


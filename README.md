# 📰 Fake News Detector

This is a **real-time fake news detection web application** built using **Streamlit**, **Scikit-learn**, and **Natural Language Processing (NLP)** techniques. It allows users to input any news content and get an instant prediction on whether the news is **REAL** or **FAKE**.

---

## 📌 Features

* ✅ Real-time text classification
* 📊 Machine Learning (Passive Aggressive Classifier)
* 🧠 TF-IDF vectorization for feature extraction
* 💻 Clean and interactive Streamlit user interface
* 🔐 Offline processing (no need for API keys or live data)

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend/ML:** Python, Scikit-learn, TextBlob, Pandas
* **Model:** Passive Aggressive Classifier with TF-IDF

---

## 🚀 How to Run the Project

### 1. Clone or Download the Repository

```bash
mkdir fake-news-detector
cd fake-news-detector
```

Create a file `app.py` and paste the project code inside it.

### 2. Install Required Packages

```bash
pip install streamlit pandas scikit-learn joblib
```

### 3. Run the Application

```bash
streamlit run app.py
```

This will open the app in your browser at `http://localhost:8501`

---

## 🧪 How it Works

1. A small dataset is used to train a classifier on real/fake news.
2. TF-IDF Vectorizer converts news text into numerical features.
3. A Passive Aggressive Classifier predicts whether the news is FAKE or REAL.
4. The model is trained, saved using `joblib`, and reused during each prediction.
5. User enters any news sentence → app shows real/fake label instantly.

---

## 🖼️ UI Preview

* 📝 Text area for entering news content
* 🔘 Button to check news
* ✅/🚫 Result shown based on model prediction

---

## 📚 Example Inputs

| News Content Example                           | Prediction |
| ---------------------------------------------- | ---------- |
| "Government announces free education for all." | ✅ REAL     |
| "Aliens landed on Earth near Taj Mahal."       | 🚫 FAKE    |

---

## 📈 Future Improvements

* Add a large dataset (e.g., Kaggle news dataset)
* Connect to live news feed APIs (e.g., NewsAPI)
* Deploy to Streamlit Cloud / Render
* Add news category classification
* Store user inputs in a log file or database

---

## 📄 License

This project is for educational/demo purposes. You can freely use, modify, and distribute it.

---

## 🤝 Author

Created by \[Saladi Rudra Naga Prasanna Lakshmi] – feel free to connect on LinkedIn/GitHub!

---

## 🙋‍♀️ Need Help?

If you run into issues, feel free to ask me here, and I’ll help you debug or improve the project.

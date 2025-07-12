# 💳 Credit Risk Segmentation App using Streamlit

A fully automated **Credit Risk Customer Segmentation Pipeline** using **PCA + KMeans Clustering** and deployed with a **Streamlit frontend**.

---

## 🚀 Project Overview

This project segments banking customers into **3 distinct clusters** based on their financial and demographic behavior. The aim is to help financial institutions:

* Group similar credit customers
* Identify high-risk vs. low-risk profiles
* Make better credit strategy decisions

---

## 🧠 Techniques Used

* **Label Encoding**: Transform categorical variables into numeric codes
* **StandardScaler**: Normalize features for optimal performance
* **PCA (Principal Component Analysis)**: Reduce dimensions while preserving patterns
* **KMeans Clustering**: Group customers into behavior-based clusters
* **Streamlit**: Build and run an interactive web app

---

## 📂 Folder Structure

```
Automated credit risk predictor/
├── app.py                         # Streamlit frontend
├── scaler.pkl                     # Saved StandardScaler
├── pca.pkl                        # Saved PCA transformer
├── kmeans_model.pkl              # Trained KMeans model
├── german_credit_data.csv        # Input dataset
├── README.md                      # Project overview
└── assets/
    └── cluster_visualization.png  # Optional cluster scatter plot
```

---

## 🖥️ Streamlit App UI

* Accepts user inputs: Age, Job Type, Credit Amount, etc.
* Applies the same preprocessing pipeline
* Predicts which cluster the user belongs to
* Displays prediction with description

---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repo
https://github.com/Rohit2255/Automating-Credit-risk-using-streamlit.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

---

## 📊 Input Features

* Age
* Sex (Male/Female)
* Job Type (0 to 3)
* Housing (Own, Rent, Free)
* Saving Account Type
* Checking Account Type
* Credit Amount (Euro)
* Duration (months)
* Purpose (Car, Education, etc.)

---

## 🔍 Use Cases

* Credit scoring segmentation
* Behavior-based customer profiling
* Pre-lending risk assessment

---

## 📎 License

This project is open-source and free to use for educational and portfolio purposes.

---

## 🤝 Connect

Built by [Rohit Yadav](https://www.linkedin.com/in/rohit-kumar-yadav-b97360194/). Let’s connect and collaborate on more finance + data science projects!

# Diabetes Prediction from Health Data

A machine learning application that predicts whether a person is **Diabetic or Not Diabetic** based on key health indicators. This project showcases an end-to-end workflow, from data analysis and model training to deployment using a **Streamlit web application**.

<!-- Optional: Add a GIF or Screenshot of your web app in action here! -->
<!-- ![Demo GIF](./demo.gif) -->

---

## Features

-   **Exploratory Data Analysis (EDA):** In-depth analysis and visualization of the PIMA Indians Diabetes Database.
-   **Data Preprocessing:** Handled missing values (imputation) and standardized features for optimal model performance.
-   **Multi-Model Training:** Trained and evaluated several classification algorithms, including Logistic Regression, K-Nearest Neighbors, Random Forest, and XGBoost.
-   **Hyperparameter Tuning:** Utilized `GridSearchCV` to find the optimal parameters for the best-performing model.
-   **Reusable ML Pipeline:** Encapsulated the entire preprocessing and prediction workflow into a single, robust `scikit-learn` Pipeline.
-   **Model Deployment:** Deployed the trained pipeline using **Streamlit** for real-time predictions.
-   **Interactive Web Interface:** Built a user-friendly web interface with **Streamlit** that allows users to input patient data and receive instant predictions.

---

## Technology Stack

-   **Application Framework:** Streamlit  
-   **Machine Learning:** Scikit-learn, Pandas, NumPy, XGBoost  
-   **Data Visualization:** Matplotlib, Seaborn  
-   **Development Environment:** Jupyter Notebook, Git  

---

## Setup and Installation

To run this project locally, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    The project's dependencies are listed in the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

---

## How to Run

Once the setup is complete, you can run the application with the following command:

```bash
streamlit run app.py
```
You should see the application running at:
```bash
http://localhost:8501
```

## Example Input
```bash
{
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
}
```
## Output
```bash
Prediction: Diabetic
```
Or
```bash
Prediction: Not Diabetic
```

## Future Improvements
- ***Improve model accuracy using deep learning techniques***
- ***Add medical recommendation system***
- ***Add user authentication***
- ***Add visualization dashboards***

## Author
***Developed by Mohit Oza***

## Disclaimer
***This project is for educational purposes only and should not be used as a real medical diagnostic system.***
  

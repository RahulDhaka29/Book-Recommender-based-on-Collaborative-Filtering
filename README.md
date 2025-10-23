# Book Recommendation System

A web application that provides book recommendations using machine learning. It features both popularity-based and collaborative filtering methods to suggest books.

## Features ✨

- **Top 50 Popular Books:** The homepage displays the 50 highest-rated books based on **average ratings** and the **number of ratings** from the dataset.

- **Collaborative Filtering:** Recommends books similar to a user's input based on the ratings of other users with similar tastes. It finds books frequently rated highly by users who also rated the input book highly.

- **Web Interface:** A simple and clean user interface built with Flask and styled using basic CSS or a framework like **Tailwind CSS** (adjust based on your actual styling).

## Project Structure 📁

```
/book-recommender-system/
|-- app.py                          # Main Flask application logic
|-- popular.pkl                     # Data for Top 50 popular books (DataFrame)
|-- pt.pkl                          # Pivot table (user-item matrix) used for collaborative filtering
|-- books.pkl                       # DataFrame containing book details
|-- similarity_scores.pkl           # Pre-computed similarity scores between books
|-- book-recommender-system.ipynb   # Jupyter notebook for EDA and model building
|-- README.md                       # This file
|-- requirements.txt                # List of Python dependencies
|-- /templates/
|   |-- index.html                  # Homepage template (Top 50)
|   |-- recommend.html              # Recommendation page template
```
---

(Adjust file names like .ipynb if yours are different)

## Dataset 📊

This project uses the **SMS Spam Collection Dataset**.

* **Source:** Commonly found on platforms like Kaggle or the UCI Machine Learning Repository. (Example Kaggle Link: [https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) - *adjust link if you used a different source*)
* **Content:** The dataset consists of SMS messages tagged as either "ham" (legitimate) or "spam".
* **File Used:** `spam.csv` (or your specific file name). This file is included in the repository for ease of use, as it is relatively small.

## Setup and Installation ⚙️

1.  **Clone the repository (or set up your local folder):**
    ```bash
    git clone [https://github.com/your-username/spam-classifier.git](https://github.com/your-username/spam-classifier.git)
    cd spam-classifier
    ```
    *(Replace `your-username` with your actual GitHub username and `spam-classifier` with your repository name)*

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Make sure you have created a `requirements.txt` file. See instructions below.)*

4.  **Download NLTK Data:** The application requires specific NLTK datasets. Run these lines in a Python interpreter within your activated environment:
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

## How to Run 🚀

1.  **Ensure Model Files Exist:** Make sure `vectorizer.pkl` and `model.pkl` are present in the project's root directory. If not, run the `sms-spam-detection.ipynb` notebook to generate them using the `spam.csv` dataset.
2.  **Activate your virtual environment:** (See Setup step 2).
3.  **Run the Flask app:**
    ```bash
    python app.py
    ```
4.  **Open your web browser** and navigate to `http://127.0.0.1:5000`.

## Model Building Process (Summary) 🧠

The `sms-spam-detection.ipynb` notebook details the model creation:
1.  **Data Loading & Cleaning:** Loaded the SMS dataset (`spam.csv`), checked for missing values, and performed initial cleaning.
2.  **Text Preprocessing:** Applied a sequence of NLP techniques using NLTK: lowercasing, tokenization, removing non-alphanumeric characters, removing stop words and punctuation, and stemming.
3.  **Feature Extraction:** Converted the processed text messages into numerical vectors using `TfidfVectorizer` from Scikit-learn.
4.  **Model Training:** Split the data into training and testing sets and trained a `MultinomialNB` (Naive Bayes) classifier.
5.  **Evaluation:** Assessed the model's performance using metrics like accuracy, precision, and recall.
6.  **Model Export:** Saved the trained `TfidfVectorizer` and the `MultinomialNB` model using `pickle`.

## Technologies Used 💻

* **Python:** Core programming language
* **Pandas:** Data manipulation and analysis
* **NumPy:** Numerical computations
* **Scikit-learn:** TF-IDF vectorization, Naive Bayes model, model evaluation
* **NLTK:** Natural Language Toolkit for text preprocessing
* **Flask:** Micro web framework for the backend server
* **HTML & Tailwind CSS:** Frontend structure and styling
* **Jupyter Notebook:** For model development, EDA, and experimentation
* **Git & GitHub:** Version control and code hosting

---

## 👨‍💻 Author

Project created by **[Rahul Dhaka]**  
[LinkedIn](https://www.linkedin.com/in/rahul-dhaka-56b975289/),  [GitHub](https://github.com/RahulDhaka29)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
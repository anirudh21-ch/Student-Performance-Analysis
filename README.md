AI-Powered NEET Testline Performance Insights
Project Overview
This project analyzes quiz performance data for students preparing for the NEET exam. It provides personalized insights, identifies weak topics, and offers actionable recommendations to improve preparation. The system leverages machine learning models, dynamic API integration, and an interactive dashboard built using Streamlit.

Features
Dynamic Data Fetching:
Fetches current quiz data and historical performance data from API endpoints.
Topic Insights:
Identifies multiple weak topics and generates structured insights.
Performance Visualization:
Visualizes overall historical quiz scores and individual topic trends.
Recommendations:
Provides tailored learning strategies for each weak topic.
Model Training:
Trains a machine learning model (Random Forest Classifier) to predict weak topics.
Tech Stack
Programming Language: Python
Framework: Streamlit
Libraries:
Data Handling: pandas, numpy
Visualization: matplotlib
Machine Learning: scikit-learn
API Integration: requests
Natural Language Processing: transformers
Deep Learning (optional): tensorflow, torch, torchvision
Folder Structure
bash
Copy
Edit
.
├── src3
│   ├── app.py                        # Main application file
│   ├── fetch_data.py                 # Handles data fetching from APIs
│   ├── data_preparation.py           # Prepares data for model training
│   ├── train_model.py                # Trains and evaluates the ML model
│   ├── recommendation_engine.py      # Identifies weak topics using the ML model
│   ├── generate_insights.py          # Generates AI-based insights and recommendations
│   ├── generate_learning_levels.py   # Categorizes learning levels for topics
├── requirements.txt                  # Project dependencies
└── README.md                         # Project documentation
Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone <repository_url>
cd student-performance-analysis
2. Install Dependencies
Install all required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the Application
Run the Streamlit app locally:

bash
Copy
Edit
streamlit run src3/app.py
4. View the Dashboard
Open the provided local URL in a browser (e.g., http://localhost:8501).
API Endpoints
Current Quiz Data:
Endpoint: https://www.jsonkeeper.com/b/LLQT

Contains details of the latest quiz submission.
Historical Quiz Data:
Endpoint: https://api.jsonserve.com/XgAgFJ

Provides performance data for the last 5 quizzes per user.
Key Components
1. Data Handling
Fetches and processes current and historical data.
Handles missing keys and incorrect formats dynamically.
2. Machine Learning
Trains a RandomForestClassifier to predict weak topics based on:
Score
Accuracy
Duration (time spent on quizzes).
3. Insights Generation
Identifies weak topics using historical data and model predictions.
Categorizes topics into learning levels (e.g., "Review Basics", "Advanced Focus").
Provides actionable recommendations.
4. Visualization
Displays:
Historical quiz scores.
Performance trends for each weak topic.
Example Insights Output
plaintext
Copy
Edit
AI-Generated Insights:
Topic: Principles of Inheritance and Variation
Performance Trend: Declining
Reason for Weakness: Frequent mistakes and low scores in recent quizzes.
Historical Performance:
| Date          | Score | Accuracy | Total Questions | Correct | Incorrect |
|---------------|-------|----------|-----------------|---------|-----------|
| 2025-01-15    | 36    | 31%      | 100             | 9       | 20        |
| 2025-01-16    | 92    | 100%     | 23              | 23      | 0         |

Recommendations:
1. Review core concepts using concise notes.
2. Practice targeted questions on common mistakes.
3. Use flowcharts to understand complex patterns.
4. Track your progress over time.

Contributing
Fork the repository.

Create a new branch:
git checkout -b feature/your-feature

Commit changes:
git commit -m "Add your message"

Push to the branch:
git push origin feature/your-feature

Open a Pull Request.

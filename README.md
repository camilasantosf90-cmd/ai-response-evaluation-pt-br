
# 🧠 EvalLab AI
### AI Response Evaluation & Quality Intelligence Platform

EvalLab AI is an independent software project designed to compare, evaluate, and analyze AI-generated responses through structured quality assessment.

## 🎯 Project Goal

The goal is to provide a simple and organized environment for evaluating two AI-generated responses to the same user prompt.

## ✨ Features

- Compare two AI-generated responses.
- Assign quality scores from 0 to 10.
- Identify the preferred response based on scores.
- Calculate score differences.
- Maintain an evaluation history during the session.
- Export evaluation reports as CSV files.
- Validate empty responses and invalid scores.

## 🛠️ Technologies

- Python
- Streamlit
- Pandas
- Pytest

## 📁 Project Structure

```text
ai-response-evaluation-pt-br/
├── app.py
├── evaluator.py
├── requirements.txt
├── README.md
└── tests/
    └── test_evaluator.py
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/camilasantosf90-cmd/ai-response-evaluation-pt-br.git
cd ai-response-evaluation-pt-br
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🧪 Tests

Run the automated tests with:

```bash
pytest
```

## 📌 Current Scope

EvalLab AI currently uses manually supplied responses and quality scores. It does not connect directly to AI model APIs or automatically determine factual accuracy.

## 👩‍💻 Project Status

This is an independent project under active development, created to explore software engineering, AI response evaluation, and quality assessment workflows.


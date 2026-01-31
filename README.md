# AI-Based Mock Interview Practice System

## Project Overview
This project is an **AI-Based Mock Interview Practice System** developed as part of the MCA coursework. It aims to help students practice Technical and HR interview questions in a simulated environment. The system generates questions, captures user responses, and uses **Natural Language Processing (NLP)** techniques to evaluate the answers against reference data, providing instant scoring and feedback.

## Objectives
- To simulate a real interview environment.
- To evaluate student answers automatically using NLP string similarity algorithms.
- To provide immediate feedback and scoring to help students improve.
- To demonstrate **MVC Architecture** in a web application using **Flask**.

## Technology Stack
- **Frontend**: HTML5, CSS3 (Custom Styling)
- **Backend**: Python 3.x, Flask (Micro-framework)
- **Database**: SQLite (SQLAlchemy ORM)
- **NLP**: Python `difflib` (SequenceMatcher) for semantic similarity

## System Architecture (MVC)
- **Model**: `models/database.py` defines the schema for `Question` and `InterviewSession`.
- **View**: `templates/` folder contains HTML files (`index.html`, `interview.html`, `result.html`) acting as the potential user interface.
- **Controller**: `controllers/main_controller.py` handles the business logic, routing, and interaction between Models and Views.

## Workflow
1. **Home Page**: User lands on the dashboard and selects "Technical" or "HR" interview mode.
2. **Interview Session**:
   - The system retrieves a set of random questions from the SQLite database.
   - User types answers into the text areas.
3. **Evaluation**:
   - On submission, the **NLP Service** (`services/nlp_service.py`) processes the text.
   - It compares the User Answer with the stored Reference Answer.
   - A similarity score (0-100%) is calculated.
4. **Results**:
   - The system displays a scorecard with the total percentage.
   - Detailed feedback is provided for each question, showing the ideal answer.

## Setup & Running
1. Clone the repository.
2. Create virtual environment: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate` (Windows)
4. Install requirements: `pip install -r requirements.txt`
5. Initialize DB: `python init_db.py`
6. Run App: `python app.py`

## Future Enhancements
- Integration of Speech-to-Text for voice interviews.
- Advanced NLP models (BERT/GPT) for deeper semantic understanding.
- User authentication and history tracking.

---
**Submitted by:** [Your Name/USN]
**Department of MCA**

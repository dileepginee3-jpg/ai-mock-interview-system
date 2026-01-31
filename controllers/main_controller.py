from flask import Blueprint, render_template, request, session, redirect, url_for
from models.database import db, Question, InterviewSession
from services.nlp_service import NLPService
from sqlalchemy.sql.expression import func
import json

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/interview', methods=['GET', 'POST'])
def interview():
    if request.method == 'GET':
        # Start a new session or continue
        category = request.args.get('category', 'Technical')
        # Get 5 random questions
        questions = Question.query.filter_by(category=category).order_by(func.random()).limit(5).all()
        return render_template('interview.html', questions=questions, category=category)
    
    if request.method == 'POST':
        # Process answers
        answers = request.form
        total_score = 0
        details = []
        
        for key, user_answer in answers.items():
            if key.startswith('q_'):
                q_id = int(key.split('_')[1])
                question = Question.query.get(q_id)
                if question:
                    score = NLPService.calculate_similarity(user_answer, question.reference_answer)
                    feedback = NLPService.get_feedback(score)
                    total_score += score
                    details.append({
                        'question': question.text,
                        'user_answer': user_answer,
                        'reference_answer': question.reference_answer,
                        'score': score,
                        'feedback': feedback
                    })
        
        # Calculate average score
        avg_score = total_score / len(details) if details else 0
        
        # Save session
        new_session = InterviewSession(
            user_name="Student", # Could be dynamic
            score=round(avg_score, 2),
            details=json.dumps(details)
        )
        db.session.add(new_session)
        db.session.commit()
        
        # Prepare chart data
        labels = [f"Q{i+1}" for i in range(len(details))]
        scores = [d['score'] for d in details]
        
        return render_template('result.html', score=round(avg_score, 2), details=details, labels=labels, scores=scores)


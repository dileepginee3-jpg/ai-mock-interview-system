from app import app
from models.database import db, Question

def init_db():
    with app.app_context():
        db.create_all()
        
        # Check if we have enough questions, if not, add more
        if Question.query.count() < 10:
            print("Seeding more questions...")
            questions = [
                # Technical Questions
                Question(text="What is the difference between a list and a tuple in Python?", 
                         category="Technical", 
                         reference_answer="Lists are mutable and defined by square brackets, while tuples are immutable and defined by parentheses."),
                Question(text="Explain the concept of inheritance in OOP.", 
                         category="Technical", 
                         reference_answer="Inheritance allows a class to derive attributes and methods from another class, promoting code reuse."),
                Question(text="What is Flask?", 
                         category="Technical", 
                         reference_answer="Flask is a micro web framework for Python."),
                Question(text="What are Python decorators?", 
                         category="Technical", 
                         reference_answer="Decorators are functions that modify the behavior of other functions or methods."),
                Question(text="Explain the difference between 'is' and '==' in Python.", 
                         category="Technical", 
                         reference_answer="'is' checks for identity (same object in memory), while '==' checks for equality (same value)."),
                Question(text="What is a lambda function?", 
                         category="Technical", 
                         reference_answer="A lambda function is an anonymous small function defined with the lambda keyword."),
                Question(text="How does memory management work in Python?", 
                         category="Technical", 
                         reference_answer="Python uses a private heap space and garbage collection (reference counting) to manage memory."),
                Question(text="What is the usage of 'self' in class methods?", 
                         category="Technical", 
                         reference_answer="'self' represents the instance of the class and allows access to attributes and methods."),
                
                # HR Questions
                Question(text="Tell me about yourself.", 
                         category="HR", 
                         reference_answer="I am a motivated MCA student with a passion for software development and AI."),
                Question(text="What are your strengths?", 
                         category="HR", 
                         reference_answer="I am a quick learner, good team player, and persistent problem solver."),
                Question(text="Where do you see yourself in 5 years?", 
                         category="HR", 
                         reference_answer="I hope to be a senior developer leading projects and mentoring juniors."),
                Question(text="Why should we hire you?", 
                         category="HR", 
                         reference_answer="I have the skills, the drive to learn, and I fit well with the company culture."),
                Question(text="Describe a challenge you overcame.", 
                         category="HR", 
                         reference_answer="I faced a complex bug in my project, but by breaking it down and researching, I solved it."),
                Question(text="How do you handle stress?", 
                         category="HR", 
                         reference_answer="I prioritize tasks, take short breaks, and focus on one thing at a time."),
            ]
            
            db.session.add_all(questions)
            db.session.commit()
            print("Database initialized with sample questions.")
        else:
             print("Database already has sufficient questions.")

if __name__ == "__main__":
    init_db()

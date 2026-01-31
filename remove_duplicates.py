from app import app
from models.database import db, Question

def remove_duplicates():
    with app.app_context():
        # Fetch all questions
        all_questions = Question.query.all()
        seen_texts = set()
        duplicates = []

        for q in all_questions:
            # Normalize text for comparison
            text = q.text.strip().lower()
            if text in seen_texts:
                duplicates.append(q)
            else:
                seen_texts.add(text)
        
        if duplicates:
            print(f"Found {len(duplicates)} duplicate questions. Removing them...")
            for dup in duplicates:
                db.session.delete(dup)
            db.session.commit()
            print("Duplicates removed.")
        else:
            print("No duplicates found.")

if __name__ == "__main__":
    remove_duplicates()

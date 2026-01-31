import difflib

class NLPService:
    @staticmethod
    def calculate_similarity(user_answer, reference_answer):
        """
        Calculates similarity between user answer and reference answer
        using SequenceMatcher. Returns a score between 0 and 100.
        """
        if not user_answer or not reference_answer:
            return 0.0
            
        # Basic normalization: lowercase and strip whitespace
        user_answer = user_answer.lower().strip()
        reference_answer = reference_answer.lower().strip()
        
        matcher = difflib.SequenceMatcher(None, user_answer, reference_answer)
        similarity = matcher.ratio() * 100
        
        return round(similarity, 2)

    @staticmethod
    def get_feedback(score):
        if score >= 80:
            return "Excellent! Your answer is very close to the reference."
        elif score >= 50:
            return "Good answer, but you could add more details."
        else:
            return "Needs improvement. Please review the core concepts."

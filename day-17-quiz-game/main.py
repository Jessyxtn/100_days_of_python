from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    new_q = Question(q["question"], q["correct_answer"])
    question_bank.append(new_q)

qb = QuizBrain(question_bank)
while qb.still_has_questions():
    qb.next_question()

final_score = qb.get_score()
print(f"Quiz finished. Your final score is {final_score}/{len(question_bank)}.")
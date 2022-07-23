from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for q in question_data:
    q_answer=q["answer"]
    q_text=q["text"]
    new_question=Question(q_answer, q_text)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_q():
    quiz.NextQuestion()

print("Congratulation you complete the quiz")
print(f"Your final score is: {quiz.score}/{quiz.q_number} ")

from question_model import Question
from data import question_data
from quiz_brain import Quizbrain




question_bank = []
for i in question_data:
    q1 = i["question"]
    a1 = i["correct_answer"]
    q = Question(q1,a1)
    question_bank.append(q)
quiz = Quizbrain(question_bank)
for question in question_bank:

    quiz.next_question()

print("You have completed your quiz")
print(f"Your final score was :{quiz.correct}/{len(question_bank)}")

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["question"]
    ans = question["correct_answer"]
    q_bank = Question(text, ans)
    question_bank.append(q_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    print(quiz.next_question())

print(f"You have completed the quiz \n Your final score is {quiz.score}/{len(q_bank)}")




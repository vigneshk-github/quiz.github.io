
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number} : {current_question.text} (True/False):")
        if self.check_answer(user_ans, current_question.ans):
            self.score += 1
        print(f"Your score is {self.score}/{self.question_number}")

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_ans, c_ans):
        return u_ans.lower() == c_ans.lower()



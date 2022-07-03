from msilib.schema import SelfReg


class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.correct_ques = 0
        # self.total_ques = 0
    
    def still_has_question(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, ans, correct_ans):
        print("Checked")
        return ans == correct_ans

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no+=1
        ans = input(f"Q.{self.question_no} : {current_question.ques} (True/False)?")
        if self.check_answer(ans, current_question.ans):
            self.correct_ques+=1
            print("Your Got it right!")
        else:
            print("Wrong Answer")
        print(f"Correct Answer is {current_question.ans}")
        print(f"Your score is {self.correct_ques}/{self.question_no}")
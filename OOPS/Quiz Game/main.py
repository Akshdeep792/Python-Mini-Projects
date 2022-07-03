from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

import random

question_bank = []

for x in question_data:
   
    # print(x)
    ques = x["text"]
    ans = x["answer"]
    obj = Questions(ques, ans)
    question_bank.append(obj)
    
# print(question_bank)
quiz = QuizBrain(question_bank)
 
while quiz.still_has_question():
    quiz.next_question()
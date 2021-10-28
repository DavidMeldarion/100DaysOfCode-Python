"""
A Question and Answer Game
"""
# import random
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank=[]
for item in question_data:
    TEXT  = item["question"]
    ANSWER  = item["correct_answer"]
    new_question=Question(TEXT, ANSWER)
    question_bank.append(new_question)

new_brain=QuizBrain(question_bank)

QUESTIONS_LEFT=True

while QUESTIONS_LEFT:
    new_brain.next_question()
    QUESTIONS_LEFT=new_brain.still_has_questions()
print("You've completed the quiz!")
print(f"Your final score is: {new_brain.score}/{new_brain.question_number}.")

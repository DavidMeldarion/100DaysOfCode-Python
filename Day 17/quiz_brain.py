"""
Quiz Brain Class
"""

class QuizBrain:
    """ Quiz Brain Class """
    def __init__(self,question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.score=0

    def still_has_questions(self):
        """Checks if there are questions left in the list"""
        length = len(self.questions_list)
        return self.question_number < length

    def next_question(self):
        """Method for asking next question"""
        current_question=self.questions_list[self.question_number]
        self.question_number += 1
        user_guess = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        if user_guess=="end":
            return True
        self.check_answer(user_guess, current_question.answer)

    def check_answer(self, user_guess, answer):
        """Method for checking if answer is correct."""
        if user_guess.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")

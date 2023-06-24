import html

class QuizBrain:
  def __init__(self,question_list):
    self.question_number = 0
    self.question_list = question_list
    self.user_score = 0

  def next_question(self):
    current_question = self.question_list[self.question_number]
    current_question.text = html.unescape(current_question.text)
    self.question_number += 1
    user_answer = input(f"{self.question_number}: {current_question.text} (True/False)?: ")
    self.check_answer(user_answer,current_question.answer)

  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
      print(f"You got it right!")
      self.user_score += 1
    else:
      print(f"That's wrong.")
    print(f"The correct answer was: {correct_answer}.")
    print(f"Your current score is: {self.user_score}/{self.question_number}\n")
      
    
    
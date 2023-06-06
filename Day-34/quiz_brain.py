import html


class QuizBrain:
  def __init__(self, question_list):
    """
    Initializes the QuizBrain object.

    Args:
    - question_list (list): List of Question objects.

    Attributes:
    - question_number (int): Current question number.
    - question_list (list): List of Question objects.
    - user_score (int): User's current score.
    """
    self.question_number = 0
    self.question_list = question_list
    self.user_score = 0

  def next_question(self):
    """
    Retrieves the next question and increments the question number.

    Returns:
    - tuple: A tuple containing the formatted question text and the correct answer.
    """
    if self.still_has_questions():
      self.current_question = self.question_list[self.question_number]
      self.current_question.text = html.unescape(self.current_question.text)
      self.question_number += 1
      return (f"Q.{self.question_number}: {self.current_question.text} (True/False)?: ", self.current_question.answer)

  def still_has_questions(self):
    """
    Checks if there are still questions remaining.

    Returns:
    - bool: True if there are more questions, False otherwise.
    """
    return self.question_number < len(self.question_list)

  def check_answer(self, user_answer):
    """
    Checks if the user's answer is correct and updates the user's score.

    Args:
    - user_answer (str): User's answer to the question.

    Returns:
    - bool: True if the answer is correct, False otherwise.
    """
    if user_answer.lower() == self.current_question.answer.lower():
      print(f"You got it right!")
      self.user_score += 1
      return True
    else:
      print(f"That's wrong.")
      return False

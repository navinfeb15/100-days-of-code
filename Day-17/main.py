from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
  question_obj = Question(ques["text"], ques["answer"])
  question_bank.append(question_obj)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
  quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.user_score}/{quiz.question_number}")
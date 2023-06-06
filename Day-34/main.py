from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for ques in question_data:
    question_obj = Question(ques["text"], ques["answer"])
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

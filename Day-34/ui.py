from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        true_pic = PhotoImage(file="images/true.png")
        false_pic = PhotoImage(file="images/false.png")

        self.score_label = Label(text="Score = 0", foreground="white", background=THEME_COLOR,
                                 font=("Arial", 10, "italic"))
        self.question_text = self.canvas.create_text(150, 125, text="", width=280, font=("Arial", 20, "italic"))
        self.true_button = Button(image=true_pic, highlightthickness=0, highlightcolor=THEME_COLOR,
                                  background=THEME_COLOR, command=self.check_true)
        self.false_button = Button(image=false_pic, highlightthickness=0, background=THEME_COLOR,
                                   command=self.check_false)

        self.score_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """
        Displays the next question on the canvas.
        """
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            q_text = self.question[0]
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz...")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        """
        Handles the action when the True button is clicked.
        """
        if self.quiz.check_answer("True"):
            self.score_label.config(text=f"Score = {self.quiz.user_score}")
            self.give_feedback(is_right=True)
        else:
            self.give_feedback(is_right=False)

    def check_false(self):
        """
        Handles the action when the False button is clicked.
        """
        if self.quiz.check_answer("False"):
            self.score_label.config(text=f"Score = {self.quiz.user_score}")
            self.give_feedback(is_right=True)
        else:
            self.give_feedback(is_right=False)

    def give_feedback(self, is_right):
        """
        Provides visual feedback on the canvas based on the correctness of the user's answer.
        """
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

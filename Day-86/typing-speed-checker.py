import tkinter as tk
import tkinter.font as tkFont
import os
import time
from tkinter import messagebox

# Change the working directory to "Day-86"
os.chdir("Day-86")

class TypingSpeedApp:
    def __init__(self, root):
        self.corrected_cpm = 0
        self.wpm = 0
        self.time_left = 0
        self.continue_playing = True

        root.title("Typing Speed Checker")
        root.geometry("600x360+0+0")

        # Create and place the title label
        self.title_label = tk.Label(root)
        self.title_label["font"] = tkFont.Font(family='Helvitica', size=20)
        self.title_label["text"] = "Typing Speed Checker"
        self.title_label.place(x=140, y=0, width=313, height=80)

        # Create and place the instructions label
        self.instructions = tk.Label(root, justify='center')
        self.instructions["font"] = tkFont.Font(family='Helvitica', size=12)
        self.instructions["text"] = "Please start typing..."
        self.instructions.place(x=100, y=100, width=400, height=30)

        # Create and place the first typing text label
        self.typing_text1 = tk.Label(root, anchor="e")
        self.typing_text1["font"] = tkFont.Font(family='Helvitica', size=18)
        self.typing_text1["text"] = ""
        self.typing_text1.place(x=70, y=150, width=125, height=50)

        # Create and place the second typing text label
        self.typing_text2 = tk.Label(root)
        self.typing_text2["font"] = tkFont.Font(family='Helvitica', size=18)
        self.typing_text2["text"] = ""
        self.typing_text2.place(x=230, y=150, width=125, height=50)

        # Create and place the third typing text label
        self.typing_text3 = tk.Label(root, anchor="w")
        self.typing_text3["font"] = tkFont.Font(family='Helvitica', size=18)
        self.typing_text3["text"] = ""
        self.typing_text3.place(x=420, y=150, width=125, height=50)

        # Create and place the entry widget
        self.entry = tk.Entry(root, justify='center')
        self.entry["font"] = tkFont.Font(family='Helvitica', size=10)
        self.entry.place(x=80, y=220, width=471, height=49)

        # Create and place the start button
        self.button = tk.Button(root, text="Start", command=self.start_stop)
        self.button.place(x=250, y=300, width=123, height=30)

        # Start looping through the words
        self.loop_words()

    def score(self):
        # Check if 60 seconds have passed since the start time
        if time.time() - self.start_time > 60:
            self.start_stop()

    def loop_words(self):
        # Bind the space key to pause the typing
        root.bind('<space>', lambda e: self.pause_var.set(1))

        # Read the paragraphs from the file
        with open("paragraphs.txt") as file:
            text = file.readlines()

        data = []
        for line in text:
            data.append(" " + line.rstrip())

        for line in data:
            temp_line = line.split(" ")

            # Check if the user wants to end the test
            if not self.continue_playing:
                break
            else:
                self.button.config(text="End test")

            for word in range(0, len(temp_line)):
                # Create a string variable to pause the typing
                self.pause_var = tk.StringVar()

                # Check if the user wants to end the test
                if not self.continue_playing:
                    break

                try:
                    self.tempword = temp_line[word + 1]
                    self.typing_text1.config(text=temp_line[word])
                    self.typing_text2.config(text=temp_line[word + 1])
                    self.typing_text3.config(text=temp_line[word + 2])
                    self.typing_text1.update()
                    self.typing_text2.update()
                    self.typing_text3.update()

                    # Wait for the pause variable to change
                    root.wait_variable(self.pause_var)

                    self.start_time = time.time()

                    # Get the sentence entered by the user and check the correctness
                    sentence = self.entry.get()
                    last_entered_word = sentence.rstrip().split(" ")[-1]
                    if last_entered_word == self.tempword:
                        self.corrected_cpm += len(self.tempword)
                        self.wpm += 1
                except IndexError as e:
                    pass

    def start_stop(self):
        if self.continue_playing:
            # End the test and display the score
            self.continue_playing = False
            messagebox.showinfo("Your Score", f"Your score: {self.corrected_cpm} CPM (that is {self.wpm} WPM)")
            self.entry.delete(0, 'end')

            # Clear the typing text labels
            self.typing_text1.config(text="")
            self.typing_text2.config(text="")
            self.typing_text3.config(text="")
            self.typing_text1.update()
            self.typing_text2.update()
            self.typing_text3.update()

            # Reset the variables and start a new test
            self.continue_playing = True
            self.loop_words()

        else:
            self.continue_playing = True

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
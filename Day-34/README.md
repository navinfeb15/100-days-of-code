# Day-34
# README




# Quizzler

Quizzler is a simple quiz game implemented using Python and Tkinter. It presents a series of True/False questions to the user and allows them to answer by clicking the corresponding buttons.

## Usage

1. Import the required modules:
```
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
```

2. Prepare the question bank by creating a list of `Question` objects:
```python
question_bank = []
for ques in question_data:
    question_obj = Question(ques["text"], ques["answer"])
    question_bank.append(question_obj)
```

3. Create a `QuizBrain` object by passing the question bank:
```python
quiz = QuizBrain(question_bank)
```

4. Create a `QuizInterface` object, passing the `QuizBrain` object:
```python
quiz_ui = QuizInterface(quiz)
```

5. Run the Tkinter event loop to start the quiz interface:
```python
quiz_ui.window.mainloop()
```

## Files

- `question_model.py`: Contains the `Question` class that represents a single quiz question.
- `data.py`: Provides the question data used to populate the question bank.
- `quiz_brain.py`: Implements the `QuizBrain` class that handles the logic for the quiz.
- `ui.py`: Implements the `QuizInterface` class that provides the graphical user interface for the quiz.

## Dependencies

- Python 3.x
- Tkinter (usually included with Python)


## Acknowledgments

The code for Quizzler is inspired by the "100 Days of Code - The Complete Python Pro Bootcamp for 2021" course on Udemy.

```

Please note that the README file assumes the existence of additional files (`question_model.py`, `data.py`, `quiz_brain.py`, `ui.py`, and `screenshots/quizzler.png`) and their respective implementations. Make sure to provide the complete code and replace the placeholder filenames with the actual filenames used in your project. Additionally, you can include any necessary installation instructions or additional acknowledgments as needed.

## License

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT).
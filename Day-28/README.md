# Day-29

# Pomodoro Timer

A simple Pomodoro Timer application built using Python and Tkinter.

The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.

This application allows you to set the work duration, short break duration, and long break duration. It will automatically switch between work and break intervals based on the predefined durations.

## Features

- Set the duration for work, short breaks, and long breaks
- Automatic switching between work and break intervals
- Visual indication of the current interval
- Reset the timer at any time

## Screenshots

![Pomodoro Timer](screenshot.png)

## How to Use

1. Make sure you have Python installed.
2. Clone this repository to your local machine.
3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
4. Run the application using the following command:
   ```
   python pomodoro_timer.py
   ```

## Customize Durations

You can customize the durations of the work, short breaks, and long breaks by modifying the following constants in the code:

```python
WORK_MIN = 25  # Duration of work interval in minutes
SHORT_BREAK_MIN = 5  # Duration of short break interval in minutes
LONG_BREAK_MIN = 20  # Duration of long break interval in minutes
```

Feel free to adjust these values to suit your preferences.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

# Define a function to turn right by turning left three times
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Keep moving until the goal is reached
while not at_goal():
    # If there is no obstacle to the right, turn right and move forward
    if right_is_clear():
        turn_right()
        move()
    # If there is an obstacle to the right, but not in front, move forward
    elif front_is_clear():
        move()
    # If there is an obstacle to the right and in front, turn left
    else:
        turn_left()

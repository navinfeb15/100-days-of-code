
# Reeborg's World

 
[reeborg's world](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Maze&url=worlds/tutorial_en/maze1.json)

  

This is a Python program that controls a robot in a simulated world. The goal of the robot is to navigate through a maze in the world and reach the finish line.

  

 - The first few lines define a function called turn_right(), which turns the robot 90 degrees to the right by turning left three times.
  - The while loop runs until the robot reaches the finish line. The at_goal() function is used to check if the robot has reached the finish line.
  - Inside the while loop, the robot checks for obstacles using the right_is_clear() and front_is_clear() functions. If there is no obstacle to the right, the robot turns right using the turn_right() function and moves forward using the move() function. If there is an obstacle to the right but not in front, the robot simply moves forward. If there are obstacles to the right and in front, the robot turns left using the turn_left() function.
   
     
   
   By using these functions and conditions, the code is able to guide the robot through the maze and towards the finish line.

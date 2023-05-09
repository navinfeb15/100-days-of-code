from turtle import Turtle,Screen
import random, time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# user_choice = screen.textinput("Turtle reacing ", "Choose the color of turtle you want to bet on :")

# colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
# turtles_list = []
# is_game_on = False


# turtle_count = 0
# class Race():
  
#   def __init__(self, turtle_color):
#     self.turtle_color = turtle_color
#     self.turtle = Turtle(shape="turtle")
    
#     self.turtle.color(turtle_color)
#     self.turtle.penup()
#     self.turtle.speed("fastest")
    
#     global turtle_count
#     turtle_count += 1  
#     self.goto_xy = (-280,90-30*turtle_count)

#   def set_position(self, pos):
#     self.turtle.goto(pos)    

#   def forward(self,distance):
#     self.turtle.forward(distance)
#   def xcor(self):
#     return self.turtle.xcor()


# if user_choice:
#   is_game_on =True
    
#   for color in colors:
#     turtle_name = str(color)+"_turtle"
#     turtle_name = Race(color)
#     # print(color,":", turtle_name.goto_xy)
    
#     turtle_name.set_position(turtle_name.goto_xy)
#     turtles_list.append(turtle_name)
      
#   while is_game_on:

#     for turtle in turtles_list:
#       if turtle.xcor() >= 265:
#         # print(turtle.xcor())
#         is_game_on=False
        
#         if user_choice == turtle.turtle_color:
#           print(f"You won! The {turtle.turtle_color} won the Race ")
#           # is_game_on=False
#         else:
#           print(f"You Lost! The {turtle.turtle_color} won the Race ")
#         break
      
      
#       dist = random.randint(10,20)
#       turtle.forward(dist)
screen.tracer(0)
game_on = True
snake = Snake()
 
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

while game_on:          
    snake.move()
    time.sleep(0.5)
    screen.update()



screen.exitonclick()


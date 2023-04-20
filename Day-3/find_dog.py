print('''
                               _
                           ,--.\`-. __
                         _,.`. \:/,"  `-._
                     ,-*" _,.-;-*`-.+"*._ )
                    ( ,."* ,-" / `.  \.  `.
                   ,"   ,;"  ,"\../\  \:   \
                  (   ,"/   / \.,' :   ))  /
                   \  |/   / \.,'  /  // ,'
                    \_)\ ,' \.,'  (  / )/
                        `  \._,'   `"
                           \../
                           \../
                 ~        ~\../           ~~
          ~~          ~~   \../   ~~   ~      ~~
     ~~    ~   ~~  __...---\../-...__ ~~~     ~~
       ~~~~  ~_,--'        \../      `--.__ ~~    ~~
   ~~~  __,--'              `"             `--.__   ~~~
~~  ,--'                                         `--.
   '------......______             ______......------` ~~
 ~~~   ~    ~~      ~ `````---"""""  ~~   ~     ~~
        ~~~~    ~~  ~~~~       ~~~~~~  ~ ~~   ~~ ~~~  ~
     ~~   ~   ~~~     ~~~ ~         ~~       ~~   
              ~        ~~       ~~~       ~
''')
      
print("Welcome to the Choose Your Own Adventure game! In this game, you'll be faced with different scenarios and choices that will determine your fate. You'll have to use your wit and strategy to navigate through the challenges and reach the end goal. Are you ready to embark on this adventure? Let's begin!")

f_choice = input(
    '\nYou\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')
if f_choice.lower().strip() == "left":
    s_choice = input(
        "\nYou've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if s_choice.lower().strip() == "wait":
        t_choice = input(
            '\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n')
        if t_choice.lower().strip() == "red":
            print("It's a room full of fire. Game Over.")
        elif t_choice.lower().strip() == "yellow":
            print("You found the treasure! You Win!")
        elif t_choice.lower().strip() == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Please enter a correct choice")
    elif s_choice.lower().strip() == "swim":
        print("You get attacked by an angry trout. Game Over.")
if f_choice.lower().strip() == "right":
    print("You chose a door that doesn't exist. Game Over.")

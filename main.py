import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

# TODO 1 (DONE)
# Create a turtle player that starts at the bottom of the screen
# listen for the "Up" keypress to move the turtle north
player = Player()

screen.listen()
screen.onkey(player.move_up, key="Up")

# TODO 2 (DONE)
# Create cars that are 20px high by 40px wide that are randomly generated
# along the y-axis and move to the left edge of the screen
# No cars should be generated in the top and bottom 50px of the screen (a turtle safe zone)
# Hint: generate a new car only every 6th time the game loop runs
# If you get stuck, check the video walk through in Step 4
car_manager = CarManager()

# TODO 3 (DONE)
# Detect when the turtle player collides with a car and stop the game if this happens
# If you get stuck, check the video walk through in Step 5

# TODO 4 (DONE)
# Detect when the turtle player has reached the top edge of the screen
# When this happens, return the turtle to the starting position and increase the speed of the cars
# Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed
# If you get stuck, check the video walk through in Step 6

# TODO 5 (DONE)
# Create a scoreboard that keeps track of which level the user is on
# Every time the turtle player does a successful crossing, the level should increase
# When the turtle hits a car, GAME OVER should be displayed in the centre
# If you get stuck, check the video walk through in Step 7
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.drive()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()


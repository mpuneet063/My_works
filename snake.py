from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 75 #make snake speed up after each food
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "yellow"
FOOD_COLOR = 'red'
BACKGROUND_COLOR = 'black'

is_game_running = True
after_id = None

class Snake:
    

    def __init__(self):

        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y, x+SPACE_SIZE,y+SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.squares.append(square)



class Food:
    
    def __init__(self):

        x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag='food')

def next_turn(snake, food):
    
    x,y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE


    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global SCORE

        SCORE += 1
        
        global SPEED

        SPEED -= 2
        
        label.config(text="Score:{}".format(SCORE))

        canvas.delete('food')

        food = Food()
    else: 
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collision(snake):
        game_over()
 
    global after_id
    after_id = window.after(SPEED, next_turn, snake, food)

    if not is_game_running: 
        return


def change_direction(new_direction):
    
    
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collision(snake):
    
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
        
    return False

def game_over():
    
    global is_game_running
    is_game_running = False

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, 
                       font=('consolas', 70), text="GAME OVER\nMOTHERFUCKER" , 
                             fill="red", tag='game over')


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

SCORE = 0
direction = 'down'

label = Label(window, text="Score:{}".format(SCORE), font=('consolas', '36'))
label.pack()

canvas = Canvas(window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

def restart_game():

    global snake, food, SCORE, direction, SPEED, is_game_running, after_id



    # Reset game variables to initial values
    is_game_running = True

    if after_id is not None:
        window.after_cancel(after_id)
        after_id = None
    canvas.delete(ALL)

    snake = Snake()

    food = Food()

    SCORE = 0

    direction = 'down'

    SPEED = 75

    label.config(text="Score:{}".format(SCORE))


    next_turn(snake, food)

# and add a restart button to the window:

restart_button = Button(window, text="Restart", command=restart_game, font=('consolas', 20))
restart_button.place(x=0, y=0)

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Return>', lambda event: restart_game())

restart_game()

window.mainloop()
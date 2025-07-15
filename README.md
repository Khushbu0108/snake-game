# snake-game
Built a classic Snake Game using Python and the Turtle graphics library. The project uses object-oriented programming with separate classes for the snake, food, and scoreboard. Includes real-time movement, collision detection, and scoring system.
## Features

- Keyboard control with arrow keys
- Real-time snake movement
- Food spawns at random positions
- Snake grows on eating food
- Scoreboard updates automatically
- Game Over on collision with wall or tail

## How It Works

- Snake is made of square segments.
- It moves continuously and changes direction with key input.
- When food is eaten, snake extends and score increases.
- Collision with walls or itself ends the game.

## File Structure

snake-game/
├── main.py # Main game loop and event handling
├── snake.py # Snake class and movement logic
├── food.py # Food class and positioning
├── snakeboard.py # Scoreboard and Game Over display
├── README.md # This file

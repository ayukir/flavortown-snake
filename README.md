# flavortown-snake

A simple Pygame snake game where the snake eats cookies, with a customizable head and cookie editor ready to be extended.

## Features
- Snake movement with arrow keys
- Cookie food that grows the snake when eaten
- On-screen score display
- Start screen prompt
- Simple smiley snake head (customizable sprite logic)

## Requirements
- Python 3.x
- Pygame

## Setup
1. Create and activate a virtual environment (recommended):
```bash
cd path/to/your/project
python3 -m venv .venv
source .venv/bin/activate
```
2. Install dependencies:
```bash
python -m pip install pygame
```

## Run
```bash
python game.py
```

## Controls
- Arrow keys: Move snake
- Q: Quit from game-over screen
- C: Play again from game-over screen

## Notes
- The game runs in a loop and ends when the snake collides with wall or itself.
- Score is the number of cookies eaten.

## Customize
- `draw_snake()` in `game.py` defines head appearance.
- `draw_cookie()` defines cookie appearance.
- You can update these functions to create your own editor interface or sprite builder.

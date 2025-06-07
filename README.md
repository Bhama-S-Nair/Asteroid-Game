# Asteroid Game

A simple arcade-style asteroid shooter game built using Python and Pygame.

---

## Description

In this game, you control a spaceship and must shoot down falling asteroids while avoiding collisions. The game features:

- Multiple levels with increasing asteroid speed.
- Lives system represented by hearts.
- Score tracking and persistent high score saved locally.
- Sound effects for shooting and defeat.
- Congratulatory message for winning after surviving 3 minutes.
- Smooth fade effect for level changes.

---

## How to Play

- Move the spaceship using **W, A, S, D** keys.
- Press **SPACE** to shoot bullets.
- Shoot asteroids to destroy them and increase your score.
- Avoid letting asteroids reach the bottom or collide with your ship.
- The game ends when you lose all lives or collide with an asteroid.
- Try to beat the high score!

---

## Installation

1. Make sure you have Python 3.x installed.

2. Clone the repository:

   git clone https://github.com/yourusername/AsteroidGame.git
   cd AsteroidGame

3. Create and activate a virtual environment (optional but recommended):

   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate

4. Install dependencies:

   pip install -r requirements.txt

5. Run the game:

   python main.py

---

## File Structure

AsteroidGame/
├── assets/
│   ├── images/
│   │   ├── spaceship.png
│   │   ├── asteroid.png
│   │   ├── asteroid_broken.png
│   │   ├── bullet.png
│   ├── sounds/
│       ├── gunfire.mp3
│       ├── defeat.mp3
│       ├── highscore_music.mp3
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── highscore.txt

---

## Dependencies

- Pygame (https://www.pygame.org/) — Used for game development and rendering.

---

## License

This project is open-source and free to use.

---

## Acknowledgments

Thanks to all open-source contributors and the Pygame community.

---

Enjoy the game! 🚀

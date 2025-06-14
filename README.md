# 🚀 Asteroid Game

A simple and exciting 2D asteroid shooting game built using **Python** and **Pygame**. Control your spaceship, blast asteroids, and survive across levels with increasing difficulty. Aim to beat the high score!






https://github.com/user-attachments/assets/224b4e2a-509d-41ce-9780-893848adfcb5




---

## 🕹️ Game Overview

- You control a spaceship that moves freely inside the game window.
- Asteroids fall from the top of the screen.
- Shoot asteroids using bullets by pressing the **space bar**.
- Survive through 3 levels with increasing asteroid speeds.
- Score increases with every asteroid destroyed.
- Lose lives when hit or when asteroids reach the bottom.
- Game ends on losing all lives or surviving for 3 minutes.
- New high scores are saved to a local file.

---

## 🛠️ Installation & Setup

### ✅ Requirements

- Python 3.7+
- Pygame library

### 📦 Install Pygame

```bash
pip install pygame
```

### 📁 Clone or Download the Repository

```bash
git clone https://github.com/Bhama-S-Nair/Asteroid-Game.git
cd asteroid-game
```

---

## 📂 Assets

Make sure the following image and sound files are in the same directory as the main Python script:

### 🎨 Images

- `spaceship.png` — spaceship sprite  
- `asteroid.png` — asteroid sprite  
- `asteroid_broken.png` — broken asteroid sprite  
- `bullet.png` — bullet sprite  

### 🔊 Sounds

- `gunfire.mp3` — shooting sound effect  
- `defeat.mp3` — game over sound  
- `highscore_music.mp3` — high score celebration sound  

---

## 🧠 High Score File

The game will create a file called `highscore.txt` automatically to store the highest score achieved.

---

## 🎯 How to Play

- Move the spaceship using `W`, `A`, `S`, `D` keys.
- Press `SPACE` to shoot bullets at incoming asteroids.
- Avoid letting asteroids reach the bottom or collide with your spaceship.
- Survive through 3 levels with increasing asteroid speeds.
- Try to beat the high score!

---

## ▶️ Running the Game

Run the Python script:

```bash
python asteroid_game.py
```

> Replace `asteroid_game.py` with the filename if different.

---

## 🎮 Controls

| Key       | Action                              |
|-----------|-------------------------------------|
| `W`       | Move up                             |
| `A`       | Move left                           |
| `S`       | Move down                           |
| `D`       | Move right                          |
| `SPACE`   | Shoot bullet                         |
| `Mouse`   | Click "Play Again" button on game over screen |

---

## 🧱 Code Structure (Brief)

- `Player` class: Handles player position, movement, and drawing.
- `Bullet` class: Manages bullets fired by the player.
- `Asteroid` class: Handles asteroid creation, movement, and broken state.
- Game loop manages spawning asteroids, bullet firing, collision detection, scoring, levels, and UI drawing.
- Sound effects and high score handling are included.
- Persistent storage of high score in `highscore.txt`.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgements

- [Pygame](https://www.pygame.org/) – Game development library.
- Sound and image assets by their respective creators.

---


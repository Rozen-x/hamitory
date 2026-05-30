# 🎮 Hamitory

## About the Game

In this game, we have a 6×6 grid (36 cells). Buttons are randomly shuffled into two categories:
- **18 Bomb cells** 💣
- **18 Normal cells** ✅

A monitor displays the game status.

## Game Rules

When you click on a cell:
- If it's a **Bomb** → Monitor shows `--:--` and the bomb counter increases by 1.
- If it's **Normal** → The monitor shows the number of bombs in that cell's row and column.

### Win/Loss Conditions:
- If **18 bombs are clicked** → **You lose** 💀
- If **18 normal cells are clicked** → **You win** 🏆

## Special Items

In each game, you can only choose **2 items**. Choose wisely! 😅

| Item | Description |
|------|-------------|
| **Marker** | Right-click on suspicious cells to mark them. Right-click again to remove the mark. |
| **50/50** | Marks two cells for you – one is a bomb, the other is normal. Guess correctly! (Test your luck) |
| **Kind Key** | This kind key gifts you a guaranteed normal cell. Enjoy this divine gift! ✨ |
| **Revercer** | Pressing this key disables and hides clicked cells, then **reverses** the bomb/normal placement. |

## Rewards

- **Win** → Gold Medal 🥇
- **Lose** → Brown Medal 🟤 (the meaning... you already know!)

> Although these medals have no physical or digital impact on your life, you deserve the best! 😊

## 📸 Game Screenshots

| Main Menu | Item Selection |
|:---:|:---:|
| ![Main Menu](game%20environment/1.png) | ![Item Selection](game%20environment/2.png) |

| Main Game View 1 | Main Game View 2 |
|:---:|:---:|
| ![Main Game 1](game%20environment/3.png) | ![Main Game 2](game%20environment/4.png) |
## Download & Run

To play the game, download and run `Hamitory.exe`, or run `game.py` using Python with Pygame installed.

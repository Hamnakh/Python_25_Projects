# Online Multiplayer Game

A real-time multiplayer game built with Python, Pygame, and socket programming. This project demonstrates how to create an online multiplayer game where players can connect and play together from anywhere in the world.

## Features

- Real-time multiplayer gameplay
- Player movement and shooting mechanics
- Health system with visual health bars
- Score tracking
- Network synchronization
- Multiple player support

## Requirements

- Python 3.6 or higher
- Pygame 2.5.2

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd online-multiplayer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## How to Run

### Starting the Server

1. Open a terminal and run:
```bash
python server.py
```

The server will start and display:
```
Server started, waiting for connections...
```

### Starting the Game Client

1. Open a new terminal and run:
```bash
python game.py
```

2. To play with multiple players, open additional terminals and run `python game.py` in each one.

## Game Controls

- **Arrow Keys**: Move your player
- **Left Mouse Click**: Shoot bullets
- **ESC or Close Window**: Quit the game

## Game Features

- Players are represented by colored squares (blue for local player, red for other players)
- Health bars are displayed above each player
- Bullets are white squares that move in the direction of the mouse click
- Players can move around the game window and shoot at each other

## Network Setup

By default, the game runs on localhost. To play over the internet:

1. Host the server on a machine with a public IP address
2. Modify the `game.py` file to connect to your server's public IP:
```python
self.client.connect(('your-server-ip', 5555))
```
3. Ensure port 5555 is forwarded on your router if hosting from home

## Project Structure

- `server.py`: Handles client connections and game state synchronization
- `game.py`: Implements the game client with Pygame
- `requirements.txt`: Lists project dependencies

## Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving the game mechanics
- Enhancing the network performance
- Creating better graphics
- Adding sound effects

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Inspired by Tech with Tim's tutorial
- Built with Pygame and Python socket programming 
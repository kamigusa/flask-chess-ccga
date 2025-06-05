# Flask Chess Game 🏛️♛

A beautiful, interactive chess game built with Flask backend and rich Tailwind CSS-styled frontend.

## Features

- 🎮 **Interactive Chess Board**: Rich UI with drag-and-drop piece movement
- 🎨 **Beautiful Design**: Tailwind CSS styling with gradients and animations
- ⚡ **Real-time Gameplay**: Instant move validation and board updates
- 🔄 **Game Management**: Reset functionality and move history
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎯 **Chess Logic**: Proper piece movement validation and game rules

## Tech Stack

- **Backend**: Python Flask (lightweight REST API)
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **Styling**: Tailwind CSS with custom chess board styling
- **Icons**: Unicode chess piece symbols

## Quick Start

### Option 1: Using the run script (Recommended)
```bash
python run.py
```

### Option 2: Manual setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Then open your browser and navigate to: `http://localhost:5000`

## Game Controls

- **Select Piece**: Click on any piece of your color
- **Move Piece**: Click on a valid destination square
- **Reset Game**: Click the "Reset Game" button
- **Current Player**: Displayed in the status panel

## Chess Rules Implemented

- ♟️ **Pawn**: Forward movement, diagonal capture, double move from start
- ♜ **Rook**: Horizontal and vertical movement
- ♞ **Knight**: L-shaped movement pattern
- ♝ **Bishop**: Diagonal movement
- ♛ **Queen**: Combined rook and bishop movement
- ♔ **King**: One square in any direction

## API Endpoints

- `GET /`: Main game interface
- `GET /api/board`: Get current board state
- `POST /api/move`: Make a move
- `POST /api/reset`: Reset the game

## Project Structure

```
flask-chess-ccga/
├── app.py              # Flask backend with chess logic
├── run.py              # Simple run script
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Rich frontend interface
└── README.md          # This file
```

## MVP Features Completed

✅ **Backend Implementation**: Complete Flask API with chess game logic  
✅ **Frontend UI**: Rich, interactive chess board with Tailwind styling  
✅ **Piece Movement**: All chess pieces with basic movement validation  
✅ **Game State**: Current player tracking and turn management  
✅ **Visual Feedback**: Selected pieces and valid move highlighting  
✅ **Responsive Design**: Beautiful gradient background and card layouts  

## Future Enhancements

- 🔥 Advanced chess rules (castling, en passant, check/checkmate)
- 💾 Move history and undo functionality
- 🤖 AI opponent
- 🌐 Multiplayer support
- 💬 Chat functionality
- 📊 Game statistics

---

Created by Claude Code Github Actions

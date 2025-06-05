from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 'white'
        self.game_over = False
        self.winner = None

    def initialize_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Place pawns
        for col in range(8):
            board[1][col] = {'piece': 'pawn', 'color': 'black'}
            board[6][col] = {'piece': 'pawn', 'color': 'white'}
        
        # Place other pieces
        piece_order = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        for col in range(8):
            board[0][col] = {'piece': piece_order[col], 'color': 'black'}
            board[7][col] = {'piece': piece_order[col], 'color': 'white'}
        
        return board

    def is_valid_move(self, from_row, from_col, to_row, to_col):
        # Basic validation
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            return False
        
        piece = self.board[from_row][from_col]
        if not piece or piece['color'] != self.current_player:
            return False
        
        target = self.board[to_row][to_col]
        if target and target['color'] == self.current_player:
            return False
        
        # Basic piece movement validation (simplified)
        piece_type = piece['piece']
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        
        if piece_type == 'pawn':
            direction = -1 if piece['color'] == 'white' else 1
            start_row = 6 if piece['color'] == 'white' else 1
            
            if from_col == to_col and not target:
                if to_row == from_row + direction:
                    return True
                if from_row == start_row and to_row == from_row + 2 * direction:
                    return True
            elif abs(from_col - to_col) == 1 and to_row == from_row + direction and target:
                return True
        
        elif piece_type == 'rook':
            return row_diff == 0 or col_diff == 0
        
        elif piece_type == 'knight':
            return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)
        
        elif piece_type == 'bishop':
            return row_diff == col_diff
        
        elif piece_type == 'queen':
            return row_diff == 0 or col_diff == 0 or row_diff == col_diff
        
        elif piece_type == 'king':
            return row_diff <= 1 and col_diff <= 1
        
        return False

    def make_move(self, from_row, from_col, to_row, to_col):
        if not self.is_valid_move(from_row, from_col, to_row, to_col):
            return False
        
        # Make the move
        piece = self.board[from_row][from_col]
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        
        # Switch players
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        
        return True

    def get_board_state(self):
        return {
            'board': self.board,
            'current_player': self.current_player,
            'game_over': self.game_over,
            'winner': self.winner
        }

# Global game instance
game = ChessGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/board')
def get_board():
    return jsonify(game.get_board_state())

@app.route('/api/move', methods=['POST'])
def make_move():
    data = request.json
    from_row = data['from_row']
    from_col = data['from_col']
    to_row = data['to_row']
    to_col = data['to_col']
    
    success = game.make_move(from_row, from_col, to_row, to_col)
    
    return jsonify({
        'success': success,
        'board_state': game.get_board_state()
    })

@app.route('/api/reset', methods=['POST'])
def reset_game():
    global game
    game = ChessGame()
    return jsonify(game.get_board_state())

if __name__ == '__main__':
    app.run(debug=True)
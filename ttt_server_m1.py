# Simple Networked Tic-Tac-Toe Server

from flask import Flask, jsonify

# Create the Flask web application.
app = Flask(__name__)


# Create the game board.
# The board is a one-dimensional list containing 9 positions.
# The positions are indexed from 0 to 8.
# An empty string "" means that the position is empty.
board = ["", "", "", "", "", "", "", "", ""]


# X will be the first player.
# This variable keeps track of whose turn it is.
current_player = "X"


# This function returns the current game state as JSON.
# A client can request this information using HTTP GET /game/state.
@app.route("/game/state", methods=["GET"])
def get_state():

    return jsonify({
        "board": board,
        "current_player": current_player
    })


# Start the server on port 5000.
if __name__ == "__main__":
    app.run(port=5000)

#To stop the application once it is running press Control and C together on the keyboard.
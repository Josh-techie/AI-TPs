def evaluate(node):
    # Evaluate the current state of the Tic-Tac-Toe board
    # Return 1 for a win, -1 for a loss, and 0 for a draw

    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if node[i*3] == node[i*3 + 1] == node[i*3 + 2] != ' ':
            return 1 if node[i*3] == 'X' else -1

        if node[i] == node[i + 3] == node[i + 6] != ' ':
            return 1 if node[i] == 'X' else -1

    if node[0] == node[4] == node[8] != ' ' or node[2] == node[4] == node[6] != ' ':
        return 1 if node[4] == 'X' else -1

    return 0  # No win, loss, or draw


def game_over(node):

    # Check if the game is over in the current state
    # Return True if the game is over, False otherwise
    return evaluate(node) != 0 or ' ' not in node


def get_children(node):
    # Get a list of valid moves or game states for the given node
    # Return a list of children nodes
    children = []
    for i, cell in enumerate(node):
        if cell == ' ':
            child = node.copy()
            child[i] = 'X'  # Assume AI is 'X' for evaluation
            children.append(child)
    return children


def minmax(node, depth, maximizingPlayer):
    if depth == 0 or game_over(node):
        return evaluate(node)
    if maximizingPlayer:
        best_value = -float('inf')
        for child in get_children(node):
            value = minmax(child, depth-1, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for child in get_children(node):
            value = minmax(child, depth-1, True)
            best_value = min(best_value, value)
        return best_value

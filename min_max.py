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

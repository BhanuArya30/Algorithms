# Time O(n) | Space O(n)
def tournamentWinner(competitions, results):
    scores = {}
    for idx, (team1, team2) in enumerate(competitions):
        # create teams dict
        scores.setdefault(team1, 0)
        scores.setdefault(team2, 0)

        # update score
        winning_team = team2 if results[idx] == 0 else team1
        scores[winning_team] += 3

    # get max score
    return max(scores, key=scores.get)

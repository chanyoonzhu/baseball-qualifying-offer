def avg_best125(salaries):
    if len(salaries) >= 125:
        avg = sum(sorted(salaries, reverse=True)[:125]) / 125
    else:
        avg = sum(sorted(salaries, reverse=True)) / len(salaries)
    return avg

print(avg_best125([i for i in range(1, 11)]))
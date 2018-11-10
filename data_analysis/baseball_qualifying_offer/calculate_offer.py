def avg_salary(salaries):
    return sum(salaries) / len(salaries)

def best_to_range(table, limit):
    rows = table[1:]
    ordered = sorted(rows, reverse=True, key=lambda x: x[1])
    if len(ordered) >= limit:
        return [table[0]] + ordered[:limit]
    else:
        return [table[0]] + ordered
        
def calc_qualifying_offer(table, limit):
    best = best_to_range(table, limit)
    salaries = [i for i in table[1]][1:]
    return round(avg_salary(salaries),2)
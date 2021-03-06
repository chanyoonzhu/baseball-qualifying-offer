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
    salaries = [i[1] for i in best][1:]
    return round(avg_salary(salaries))

def find_close_offers(sortedTable, offer):
    neighborCount = 10
    # start from second row (first row is header)
    i = 1
    while i < len(sortedTable):
        if sortedTable[i][1] <= offer:
            break
        i += 1
    # shift i if exceed index range
    while i - neighborCount // 2 < 1:
        i += 1
    while i + neighborCount // 2 + 1 > len(sortedTable):
        i -= 1
    start = i - neighborCount // 2
    end = i + neighborCount // 2 + 1
    return [sortedTable[0]] + sortedTable[start:end]
            
    
def avg_best125(nums):
    if len(nums) >= 125:
        avg = sum(sorted(nums, reverse=True)[:125]) / 125
    else:
        avg = sum(sorted(nums, reverse=True)) / len(nums)
    return avg

def calc_qualifying_offer(salaries):
    return round(avg_best125(salaries),2)
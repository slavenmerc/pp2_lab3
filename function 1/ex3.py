def solve(numheads, numlegs):
    num_rabbits = (numlegs - 2 * numheads) / 2
    num_chickens = numheads - num_rabbits
    
    if num_chickens >= 0 and num_rabbits >= 0 and num_chickens.is_integer() and num_rabbits.is_integer():
        return {int(num_chickens)}, {int(num_rabbits)}
    else:
        return "No solution"
numheads = 35
numlegs = 94
print(solve(numheads, numlegs))

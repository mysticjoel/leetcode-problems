counts[(char, length)] += 1
if length > 1:
    counts[(char, length-1)] += 2
    if length > 2:
        counts[(char, length-2)] += 3
def ft_count_harvest_iterative():
    day = int(input("Days until harvest: "))
    day = day + 1
    display = range(1, day)
    for n in display:
        print(f"Day {n}")

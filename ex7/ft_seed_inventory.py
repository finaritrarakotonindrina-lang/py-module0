def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"Tomato seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"Carrot seeds: {quantity} grams total")
    elif unit == "area":
        print(f"Lettuce seeds: cover {quantity} square meters")

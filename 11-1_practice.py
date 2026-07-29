for gugu in range(2, 10, 2):
    if gugu % 2 == 0:
        print(f"=== {gugu}단 ===")
        for num in range(1, 10):
            print(f"{gugu} x {num} = {gugu * num}")
        print()

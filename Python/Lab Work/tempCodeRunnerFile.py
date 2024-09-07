for i in range(5):
    for j in range(1, 5-i):
        print(" ", end="")
    for k in range(i + 1):
        time.sleep(0.3)
        print("*", end="")
    print()

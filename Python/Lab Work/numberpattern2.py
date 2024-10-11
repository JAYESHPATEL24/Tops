# 4     4
#  3   3
#   2 2
#    1
#   2 2
#  3   3
# 4     4

n = int(input("Enter a Number: "))

s = 2 * n - 1

for i in range(s):
    for j in range(s):
        if i == j or i + j == s - 1:
            print(n - min(i, s - 1 - i), end=" ")
        else:
            print("- ", end="")
    print()
    
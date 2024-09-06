import time

print("Square Pattern")
print()

# square pattern
for i in range(6):
    for j in range(6):
        time.sleep(0.3)
        print("*", end="")
    print()
    
print()
print("Hollow Square Pattern")
print()

# Hollow square pattern
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            time.sleep(0.3)
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
print()
print("Left triangle Pattern")
print()

# Left Triangle Pattern

for i in range(5):
    for j in range(i+1):
        time.sleep(0.3)
        print("*",end="")
    print()

print()
print("Right triangle Pattern")
print()

# Right Triangle Pattern

for i in range(5):
    for j in range(1, 5-i):
        print(" ", end="")
    for k in range(i + 1):
        time.sleep(0.3)
        print("*", end="")
    print()

print()
print("Left Downward triangle Pattern")
print()

# Left Downward Triangle Pattern

for i in range(5):
    for j in range(5 - i):
        time.sleep(0.3)
        print("*", end="")
    print()

print()
print("Right Downward triangle Pattern")
print()

# Right Downward triangle  pattern
for i in range(5):
    for j in range(i):
        print(" ", end="")
    for j in range(5, i, -1):
        time.sleep(0.3)
        print("*", end="")
    print()
    
print()
print("Right Downward triangle Pattern")
print()

# hollow triangle star pattern

for i in range(1, 7):
    for j in range(i):
        if j == 0 or j == i-1:
            print("*", end="")
        else:
            if i != 6:
                print(" ", end="")
            else:
                time.sleep(0.3)
                print("*", end="")
    print()
    
print()
print()

for i in range(5):
    for j in range(5 - i):
        time.sleep(0.3)
        print("*", end="")
    for j in range(i):
        print(" ", end="")
    for j in range(i):
        print(" ", end="")
    for j in range(5, i, -1):
        time.sleep(0.3)
        print("*", end="")
    print()


for i in range(5):
    for j in range(i+1):
        time.sleep(0.3)
        print("*",end="")
    for j in range(1, 5-i):
        print(" ", end="")
    for j in range(1, 5-i):
        print(" ", end="")
    for k in range(0, i + 1):
        time.sleep(0.3)
        print("*", end="")
    print()

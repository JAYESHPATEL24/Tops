import time

patterns = [
    [" *****  ", " *   *  ", " *   *  ", " *   *  ", " *   *  ", " *   *  ", " *****  "],  # 0
    ["   *    ", "  **    ", " * *    ", "   *    ", "   *    ", "   *    ", " *****  "],  # 1
    [" *****  ", "     *  ", "     *  ", " *****  ", " *      ", " *      ", " *****  "],  # 2
    [" *****  ", "     *  ", "     *  ", " *****  ", "     *  ", "     *  ", " *****  "],  # 3
    [" *   *  ", " *   *  ", " *   *  ", " *****  ", "     *  ", "     *  ", "     *  "],  # 4
    [" *****  ", " *      ", " *      ", " *****  ", "     *  ", "     *  ", " *****  "],  # 5
    [" *****  ", " *      ", " *      ", " *****  ", " *   *  ", " *   *  ", " *****  "],  # 6
    [" *****  ", "     *  ", "     *  ", "     *  ", "     *  ", "     *  ", "     *  "],  # 7
    [" *****  ", " *   *  ", " *   *  ", " *****  ", " *   *  ", " *   *  ", " *****  "],  # 8
    [" *****  ", " *   *  ", " *   *  ", " *****  ", "     *  ", "     *  ", " *****  "]   # 9
]

# Input: Assume user input is a string of digits.
n = input("Enter your mobile number: ")

# Prepare lines for horizontal display
lines = [""] * 7

# Loop through each digit in the input number
for digit in n:
    for row in range(7):
        lines[row] += patterns[int(digit)][row] + "  "  # Add two spaces between each digit's pattern

# Print the final horizontal pattern
for line in lines:
    print(line)
    time.sleep(0.5)  # Add a delay for better viewing

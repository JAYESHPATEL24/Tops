import time

patterns = [
    " *****  \n"
    " *   *  \n"
    " *   *  \n"
    " *   *  \n"
    " *   *  \n"
    " *   *  \n"
    " *****  ",
    "   *    \n"
    "  **    \n"
    " * *    \n"
    "   *    \n"
    "   *    \n"
    "   *    \n"
    " *****  ",
    " *****  \n"
    "     *  \n"
    "     *  \n"
    " *****  \n"
    " *      \n"
    " *      \n"
    " *****  ",
    " *****  \n"
    "     *  \n"
    "     *  \n"
    " *****  \n"
    "     *  \n"
    "     *  \n"
    " *****  ",
    " *   *  \n"
    " *   *  \n"
    " *   *  \n"
    " *****  \n"
    "     *  \n"
    "     *  \n"
    "     *  ",
    " *****  \n"
    " *      \n"
    " *      \n"
    " *****  \n"
    "     *  \n"
    "     *  \n"
    " *****  ",
    " *****  \n"
    " *      \n"
    " *      \n"
    " *****  \n"
    " *   *  \n"
    " *   *  \n"
    " *****  ",
    " *****  \n"
    "     *  \n"
    "     *  \n"
    "     *  \n"
    "     *  \n"
    "     *  \n"
    "     *  ",
    " *****  \n"
    " *   *  \n"
    " *   *  \n"
    " *****  \n"
    " *   *  \n"
    " *   *  \n"
    " *****  ",
    " *****  \n"
    " *   *  \n"
    " *   *  \n"
    " *****  \n"
    "     *  \n"
    "     *  \n"
    " *****  "
]

for number, pattern in enumerate(patterns,):
    print(f"{number}:\n{pattern}\n")

# Input: Assume user input is a string of digits.
n = input("Enter your mobile number: ")

# Loop through each digit in the input number and print the corresponding pattern
for i in n:
    time.sleep(1)
    print(patterns[int(i)], end="\n\n")
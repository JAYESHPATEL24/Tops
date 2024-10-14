#  given n pairs of parentheses, write a function to generate all combination of well-formed parentheses.
# input : n = 3
# output : ["((()))","(()())","(())()","()(())","()()()"]

n = int(input("Enter a Number : "))
l = []
stack = [("", 0, 0)]

while stack:
    s, left, right = stack.pop()
    if len(s) == 2 * n:
        l.append(s)
    if left < n:
        stack.append((s + "(", left + 1, right))
    if right < left:
        stack.append((s + ")", left, right + 1))

print(l)

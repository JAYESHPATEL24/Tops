# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring  with 'good'. Return the resulting string.  

s = input("Enter a string: ")

    # Find the first occurrence of 'not' and 'poor'
s1 = s.find('not')
s2 = s.find('poor')

    # Check if 'not' appears before 'poor'
if s1 != -1 and s2 != -1 and s1 < s2:
        # Replace the 'not'...'poor' substring with 'good'
    result = s[:s1] + 'good' + s[s2 + 4:]
else:
        # If the condition is not met, return the original string
    result = s

    # Print the resulting string
print(f"The resulting string is: {result}")

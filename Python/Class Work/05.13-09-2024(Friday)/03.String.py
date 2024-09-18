s = " Python PrograMMing "

print(s)
print()
print("Len()")
# find Length of object 
# use for strings, lists, tuples, and dictionaries to find out the number of elements.
# len(object)
print(len(s))   

print()
print("capitalize()")
# convert the first character of a string to uppercase and the rest of the characters to lowercase.
print(s.capitalize())    

print()
print("lower()")
# convert all the characters in a string to lowercase
print(s.lower())     

print()
print("swapcase()")
# convert all uppercase characters in a string to lowercase and all lowercase characters to uppercase
print(s.swapcase()) 

print()
print("center()")
# center-align a string within a specified width, padding it with a specified character (default is a space). 
# string.center(width, fillchar)
# width: The total width of the resulting string.
# fillchar (optional): The character used for padding. If not specified, spaces are used by default.
print(s.center(30,"$")) 

print()
print("count()")
# count the number of occurrences of a substring within a string.
# string.count(substring, start, end)
# substring: The substring you want to count.
# start (optional): The starting index from where the search begins.
# end (optional): The ending index where the search ends.
print(s.count("P"))  

print()
print("endswith()")
# suffix: The suffix you want to check.
# start (optional): The starting index from where the search begins.
# end (optional): The ending index where the search ends.
# string.endswith(suffix, start, end)
print(s.endswith("ng ")) 

print()
print("find()")
# Locate the first occurrence of a specified substring within a string. 
# "use for conditional Statements for String."
# If the substring is found, it returns the index of the first character of the first occurrence. 
# If the substring is not found, it returns -1.
# string.find(substring, start, end)
# substring: The substring you want to search for.
# start (optional): The starting index from where the search begins. Default is 0.
# end (optional): The ending index where the search ends. Default is the end of the string.
print(s.find("P",2))  

print()
print("index()")
# Find the first occurrence of a specified substring within a string. 
# If the substring is found, it returns the index of the first character of the first occurrence. \
# If the substring is not found, it raises a ValueError exception.
# "use for strings, lists and tuples."
# string.index(substring, start, end)
# substring: The substring you want to search for.
# start (optional): The starting index from where the search begins. Default is 0.
# end (optional): The ending index where the search ends. Default is the end of the string.
print(s.index("P"))  

print()
print("replace()")
# replace occurrences of a specified substring with another substring. 
# It returns a new string with the replacements made, leaving the original string unchanged.
# string.replace(old, new, count)
# old: The substring you want to replace.
# new: The substring to replace the old substring with.
# count (optional): The number of times you want to replace the old substring. If not specified, all occurrences are replaced.
print(s.replace("P","R")) 

print()
print("isalnum()")
# checks whether all the characters in a string are alphanumeric (i.e., letters and numbers) and returns True if they are. 
# If the string contains any non-alphanumeric characters (such as spaces, punctuation, etc.), it returns False.
print(s.isalnum()) 

print()
print("isalpha()")
# checks whether all the characters in a string are alphabetic (i.e., letters) and returns True if they are. 
# If the string contains any non-alphabetic characters (such as numbers, spaces, punctuation, etc.), it returns False.
print(s.isalpha())

print()
print("title()")
# convert the first character of each word in a string to uppercase and the remaining characters to lowercase. 
print(s.title()) 

print()
print("upper()")
# convert all the characters in a string to uppercase. 
print(s.upper()) 

print("\"Python\"")

print('''"Python"''')

print()
print("casefold()")
# convert all characters in a string to lowercase, similar to the lower() method. 
# casefold() is more aggressive in its conversion, making it suitable for caseless matching.
print(s.casefold())

print()
print("split()")
# divide a string into a list of substrings based on a specified separator. 
# If no separator is specified, the method splits the string at any whitespace.
# string.split(separator, maxsplit)
# separator (optional): The delimiter at which the string is split. The default is any whitespace.
# maxsplit (optional): The maximum number of splits to perform. The default is -1, which means “all occurrences.”
print(s.split())


print()
print("join()")
# concatenate the elements of an iterable (like a list, tuple, or set) into a single string, 
# with a specified separator between each element.
# separator.join(iterable)
# separator: The string that will be placed between each element of the iterable.
# iterable: The iterable whose elements you want to join.
print("-".join(s))

print()
print("zfill()")
# pad a string with zeros on the left, until it reaches a specified length. 
# This is particularly useful for formatting numbers as strings with leading zeros.
# string.zfill(width)
# width: The total length of the resulting string after padding.
print(s.zfill(30))

str="Hello\tbhai" 
print()
print("expandtabs()")
# replace tab characters (\t) in a string with a specified number of spaces. 
# This method is particularly useful for formatting text where tab characters need to be expanded into spaces.
# string.expandtabs(tabsize)
# tabsize (optional): Specifies the number of spaces to replace each tab character. The default value is 8.
print(str.expandtabs(20))

print()
print("maketrans() & translate()")
# create a translation table that maps characters in a string to other characters. 
# This translation table is then used with the translate() method to replace specified characters in a string efficiently.
# str.maketrans(x, y, z)
# x: If only one parameter is specified, it must be a dictionary describing how to perform the replacements. If two or more parameters are specified, this parameter must be a string specifying the characters you want to replace.
# y (optional): A string with the same length as x. Each character in the first parameter will be replaced with the corresponding character in this string.
# z (optional): A string describing which characters to remove from the original string.
# string.translate(table)
# table: A translation table created by the str.maketrans() method.
# replace characters in a string based on a translation table created by the maketrans() method. 
# This method is efficient for character-level replacements and deletions.
table = s.maketrans("Py","ij","ing")
print(s.translate(table))

print()
print("removeprefix()")
# remove a specified prefix from a string.
print(s.removeprefix(" Pyth"))

print()
print("partition()")
# split a string into three parts based on the first occurrence of a specified separator. 
# It returns a tuple containing three elements: the part before the separator, the separator itself, and the part after the separator.
# string.partition(separator)
# separator: The string to search for within the original string
print(s.partition("Pro"))


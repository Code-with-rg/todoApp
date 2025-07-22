# import re

# # match = re.search(r'iii', 'piiig') # found, 
# # match.group() == "iii"
# # match = re.search(r'igs', 'piiig') # not found, 
# # match == None

# #   ## . = any char but \n
# # match = re.search(r'..g', 'piiig') # found, 
# # match.group() == "iig"

# #   ## \d = digit char, \w = word char
# # match = re.search(r'\d\d\d', 'p123g') # found, 
# # match.group() == "123"
# # match = re.search(r'\w\w\w', '@@abcd!!') # found, 
# # match.group() == "abc"

# # text = """Hello this is ganesh rajput, this is mine email please check this and mail me the report please , ganesh@bitcodingsolutions.com"""

# # mail = re.search(r'\w+@\w+.\w+',text)


# # str = 'kiiiiiing is kiiiing, do not tell any one'
# # match = re.search(r'([\w.a-zA-Z0-9]*)\s*([\w.a-zA-Z0-9]*)',str)

# # if match:
# #     print(match.group())
# #     print(match.group(1))
# #     print(match.group(2))
# #     # print(match.group(3))

# import re

# text = "The quick brown fox jumps over the lazy dog."

# # Replace "quick" with "fast"
# new_text = re.sub(r"quick", "fast", text)
# print(new_text)

# # Replace all vowels with '*'
# vowels_replaced = re.sub(r"[aeiouAEIOU]", "*", text)
# print(vowels_replaced)

# # Replace only the first occurrence of "the"
# first_the_replaced = re.sub(r"the", "a", text, count=1)
# print(first_the_replaced)

# # Using a callable for replacement (e.g., to uppercase matched words)
# def uppercase_match(match):
#     return match.group(0).upper()

# uppercase_words = re.sub(r"\b\w+\b", uppercase_match, text)
# print(uppercase_words)

import re

a = "ganesh, Yashwant, Ayan, Harsh, Abhay"

# Match name and age
pattern = r"(\w+)" 

# Use age first, then name
repl = r"A computer Engineer-  \1" 

# Swap names and ages
result = re.sub(pattern, repl, a) 

print(result)
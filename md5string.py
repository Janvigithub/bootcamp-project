# Write a Program in python to generate MD5 of string data.


import hashlib

str = "HelloWorld"
result = hashlib.md5(str.encode())
print("The MD5 string of", str, "is : ", end="")
print(result.hexdigest())

# Output :-
# The MD5 string of HelloWorld is : 68e109f0f40ca72a15e05cc22786f8e6

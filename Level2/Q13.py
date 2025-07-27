#Python program to find if a given string starts with a given character using Lambda.

# Sample input
input_string = "Hello, World!"
given_char = "H"

# Lambda function to check if the string starts with the given character
starts_with = lambda s, c: s.startswith(c)

# Output
print(starts_with(input_string, given_char))

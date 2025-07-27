
#write a function that returns the run length encoded string for the input string
def run_length_encode(input_string):
    if not input_string:
        return ""

    result = ""
    count = 1

    # Iterate through characters
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            result += input_string[i - 1] + str(count)
            count = 1  # reset counter

    # Add the last character and its count
    result += input_string[-1] + str(count)
    return result

# Example usage
input_str = "wwwwaaadebbbbbw"
encoded = run_length_encode(input_str)
print("Encoded output:", encoded)

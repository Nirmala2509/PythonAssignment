Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

# Initialize empty dictionary
freq_dict = {}

# Count frequencies
for item in Input_list:
    if item in freq_dict:
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1

# Print the frequency dictionary
print("Frequency count:", freq_dict)

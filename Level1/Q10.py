#Python program to reverse the order of words

#Input_sentence = "Hello, World! Welcome to Python programming."
Input_sentence=input("Enter the string to reverse: ")
Output_sen=Input_sentence.split()

#Reversing the sentence
Output_sen.reverse()

#Converting back to string from list

Final_sentence=' '.join(Output_sen)
print(Final_sentence)




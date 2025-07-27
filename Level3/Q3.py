'''Write a function definition for JtoI() in Python that would display
the corrected version of the entire content of the file WORDS.TXT
with all the alphabet "J" to be displayed as an alphabet "I" on the
screen.'''

with open("words.txt","w") as f:
    f.write("Thjs is a demo fjle. Fjle name js words")

def Jtol():
    with open("words.txt","r")  as f:
        for words in f:
            new_text=words.replace('j','i')
            print(new_text)
          
Jtol()
  

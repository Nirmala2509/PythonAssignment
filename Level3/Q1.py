

#return only the even length string from the file
f=open("Testfile.txt",'w')    
f.write("This is a test file. hi again.This is a demo file.")  
f.close()

with open("Testfile.txt", "r") as f:
   for line in f:
        words = line.split()
   for word in words:  
       if len(word)%2==0:
           even_words=word
           print(''.join(even_words))
   
      

    
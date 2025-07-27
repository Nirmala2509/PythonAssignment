'''Create the custom Python classes which have methods and
attributes and implement single inheritance, multiple inheritance,
and multilevel inheritance'''

class Grand_parent():
    def __init__(self,fname,lname):
     self.fname=fname
     self.lname=lname

    def display_name(self):
       print(f"Name is {self.fname}{self.lname}") 

#Single inheritance
class Parent(Grand_parent):
    def display_age(self,age):
       print(f"Age is {age}")
   
#Mulitlevel Inheritance    
class child(Parent): 
  def display_greet(self,name):
     print(f"Name in Parent class is  {name}")
   
#Multiple Inheritnace
class Sports:
   def display_SportsGreet(self,sname):
      print(f"Name in sports class is {sname}")

class super_child(Sports,child):
   def display_childGreet(self,super_name):
      print(f"Name in super_child class is {super_name}")



obj=super_child("John","Smith")      
obj.display_name()
obj.display_age(12)
obj.display_greet("Sam")
obj.display_SportsGreet("Football")
obj.display_childGreet("Tom")
   



   
          


#First program20
print("Hello world")
import math
#Assignment of variables 
name="Michael"

pie_value=("Pie is ",math.pi)
print(pie_value)
#print(type(name)) #type shows us what type of the variable we are handling
#print(name)
#del name   #deletes name


#Accepting user input 
#user_input=input("what is your name?")
#print(user_input) 

#if statements
#number1 = input("what is your age? ")
#number1=float(number1)

#number1=int(number1)
#age_in_5_years=5;

#Functions
def age_in_5_years(number1,age_in_5_year):
    if number1 != 0:
     new_age=number1+age_in_5_year
     print("you will be ",new_age," years old")
    else:
     print("Age is < 0")

number1 = input("what is your age? ")
number1=int(number1)
age_in_5_year=5;
age_in_5_years(number1,age_in_5_year)



def nothing():
    print("There's nothing here , you are getting there, bit by bit")    
nothing()  


#Funtion that returns
def cal_new_sal(salary,tax):
    tax_perc=(tax/100)
    temp_sal=salary*tax_perc
    new_sal=salary-temp_sal
    return(new_sal)



salary=2500.30
tax=15
new_salary=cal_new_sal(salary,tax)
print("Your new salary is R",new_salary)
    
 
 
#loops

days=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]   

for day in days:
  if(day =="Thur"):continue
  print(day)
  
  

for x in range(1,5):
      print(x)
  
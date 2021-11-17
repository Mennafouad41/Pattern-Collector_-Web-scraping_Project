from Pattern_class  import Email_pattern_function
from Pattern_class  import All_Emails__pattern_function
from Pattern_class  import Phone_pattern_function
from Pattern_class  import All_Phones_pattern_function
from Pattern_class  import IPV4_pattern_function
from Pattern_class  import All_IPsV4_pattern_function

#from  Pattern_class import SaveFile_All_pattern_function

String = """ This is my Email = mennamony@gmail.com
             and my number is : +02 123 456 789
             but there is other email for testing the function, which is 
             Email_test : test.account@yahoo.com
             the ipv4 : 123.345.12.456
             good bye """ 
              
print("Please enter string to test this script")  

print("After entering the string please enter number as follow :") 

print(" Number-1 -> Indicates that you want to extract the first email in the text")

print(" Number-2 -> Indicates that you want to extract the all emails in the text")

print(" Number-3 -> Indicates that you want to extract the first phone number in the text")

print(" Number-4 -> Indicates that you want to extract the all phones numbers in the text")

print(" Number-5 -> Indicates that you want to extract the first IP-V4 in the text")

print(" Number-6 -> Indicates that you want to extract the all IPs-V4 in the text")

print("For example, The string like this :") 

print(String)

print("For example, The number like this :") 

print("3")

User_String = input("Enter string : ")

User_number = int(input("Enter number: ")) 

if User_number == 1 :
    
  Email_pattern_function("\S{1,}\@\S{1,}.\S{1,}",User_String)
  
elif User_number == 2 :
    
  All_Emails__pattern_function("\S{1,}\@\S{1,}.\S{1,}",User_String)   

elif User_number == 3 :
   
  Phone_pattern_function("\+\d{1,}\s{1,}\d{1,}\s\d{1,}\s\d{1,}",User_String)
  
elif User_number == 4 :
   
  All_Phones_pattern_function("\+\d{1,}\s{1,}\d{1,}\s\d{1,}\s\d{1,}",User_String)

elif User_number == 5 :
   
  IPV4_pattern_function("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",User_String) 

elif User_number == 6 :
   
  All_IPsV4_pattern_function("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",User_String)       

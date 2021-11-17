import re

# This function to print the first email that founded in a given text 
def Email_pattern_function(pattern,string_value):
    
    reg = re.search(pattern,string_value)
    print("The target pattern with it is location is :")
    print(reg)
    print("The target pattern is :")
    print(reg.group())
    print("The location of target pattern is :")
    print(reg.span())
    
# This function to print all emails that founded in a given text     
def All_Emails__pattern_function(pattern,string_value):
    
    reg = re.findall(pattern,string_value)
    print("The all target patterns are :")
    for target in reg :
       print(target)
       
    
# This function to print the first phone that founded in a given text 
def Phone_pattern_function(pattern,string_value):
    
    reg = re.search(pattern,string_value)
    print("The target pattern with it is location is :")
    print(reg)
    print("The target pattern is :")
    print(reg.group())
    print("The location of target pattern is :")
    print(reg.span())
    
# This function to print all phones that founded in a given text     
def All_Phones_pattern_function(pattern,string_value):
    
    reg = re.findall(pattern,string_value)
    print("The all target patterns are :")
    for target in reg :
       print(target)
       
      
        
# This function to print the first IP-V4 that founded in a given text 
def IPV4_pattern_function(pattern,string_value):
    
    reg = re.search(pattern,string_value)
    print("The target pattern with it is location is :")
    print(reg)
    print("The target pattern is :")
    print(reg.group())
    print("The location of target pattern is :")
    print(reg.span())
    
# This function to print all IPs-V4 that founded in a given text     
def All_IPsV4_pattern_function(pattern,string_value):
    
    reg = re.findall(pattern,string_value)
    print("The all target patterns are :")
    for target in reg :
       print(target)
       

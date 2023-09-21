b=['a','e','i','o','u']
def solution(my_string):
    for z in my_string:
        if z in b:
            my_string =my_string.replace(z,"")
            
    
    
    return my_string
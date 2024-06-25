def generate_pair(num):#this is a function 
    num1=1
    my_list =[]

    while num1<num:
        my_list.append(num1*2)

        num1 += 1
    
    return my_list


print(generate_pair(20))

print("#####################################")

def generate_pair1(num):#this is a generator
    num1=1
    while num1<num:
        yield num1*2
        num1 += 1

return_pair = generate_pair1(20)  
print(next(return_pair))
print("#####################################")
print(next(return_pair))
print("#####################################")
print(next(return_pair))
print("#####################################")
    
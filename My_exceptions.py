def what_age(age):
    if age<0:
        raise TypeError("No neg ages") #thi is my personalized except
    
    if age < 20:
        return "young"
    elif age < 40:
        return 'young for'
    elif age < 65:
        return "your are an adult"
    elif age < 100:
        return "take care of yourselft"

print(what_age(-15))
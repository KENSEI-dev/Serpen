Issue=[]
def has_Space(str):
    for char in str:
        if char==" ":
            return True
    return False

def has_Identical(str):
    for i in range(len(str)-2):
        char1=str[i]
        char2=str[i+1]
        char3=str[i+2]
        if char1 == char2 == char3:
            return True
    return False

def has_UpperCase(str):
    count=0
    for char in str:
        if char.isupper():
            count+=1
    if count>=1:
        return True
    else:
        Issue.append("No uppercase")
        return False

def has_LowerCase(str):
    count=0
    for char in str:
        if char.islower():
            count+=1
    if count>=1:
        return True
    else:
        Issue.append("No Lower Case")
        return False

def has_Digit(str):
    count=0
    for char in str:
        if char.isdigit():
            count+=1
    if count>=1:
        return True
    else:
        Issue.append("Has no digits")
        return False
    
def has_Special_char(str):
    special='!@#$%^&*()_+-=[]{}|;:,.<>?'
    count=0
    for char in str:
        if char in special:
            count+=1
    if count>=1:
        return True  
    else: 
        Issue.append("No special character")
        return False


bool=True

while(bool):
    password=input("Input: ")
    Issue.clear()
    pass_scored=0
    if has_Space(password):
        Issue.append("Has Space")
    if has_Identical(password):
        Issue.append("Consecutive identical characters")
    if len(password)>=8:
        pass_scored+=1
    if has_UpperCase(password):
        pass_scored+=1
    if has_LowerCase(password):
        pass_scored+=1
    if has_Digit(password):
        pass_scored+=1
    if has_Special_char(password):
        pass_scored+=1
    if len(password)>=12:
        pass_scored+=1
    if pass_scored<=2:
        strength="Weak"
    elif 2<pass_scored<=4:
        strength="Moderate"
    else:
        strength="Strong"

    print(f"Strength: {strength}")
    print(f"Score: {pass_scored}/6")
    print(f"Issues: {','.join(Issue) if Issue else None}")
    
    user_control=input("Would you like to continue? (y/n)")
    if user_control[0] =='y':
        bool=True
    else:
        bool=False
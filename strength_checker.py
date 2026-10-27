def password_strength_checker(password):
    length = len(password)
    
    has_upper = False
    has_digit = False
    has_symbol = False
    has_lower = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_symbol = True
            
    variety_score = 0
    if has_upper:
        variety_score += 1
    if has_lower:
        variety_score += 1
    if has_digit:
        variety_score += 1
    if has_symbol:
        variety_score += 1
        
    for char in password:
        if char.isspace():
            return "Invalid Password"
    
    if length < 6:
        return "weak"
    elif length >= 8 and variety_score >= 3:
        return "strong"
    else:
        return "medium"
    
        
            
            


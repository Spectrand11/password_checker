import strength_checker

print("=====PASSWORD STRENGTH CHECKER======")
password = input("Enter a password: ")

verdict = strength_checker.password_strength_checker(password)


print("PASSWORD STRENGTH >>>",verdict.upper())


import strength_checker
from getpass import getpass

print("=====PASSWORD STRENGTH CHECKER======")
password = getpass("Enter a password: ")

verdict = strength_checker.password_strength_checker(password)


print("PASSWORD STRENGTH >>>",verdict.upper())


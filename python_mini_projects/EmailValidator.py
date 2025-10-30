import re

while True:
    user_email = input("Enter your email address:\n <<< Valid Email is : user_email[@]domain[dot][example] >>>\n >>>  ").lower()
    match = re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", user_email)
    if match:
        print(">>> Valid email. :>")
        break

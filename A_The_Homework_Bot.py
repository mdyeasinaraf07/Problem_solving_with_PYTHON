def check_pass(marks):
    """Return ture if the student passes the quiz, otherwise false"""
    if(marks >= 40):
        return True
    else:
        return False

marks = int(input())
ans = check_pass(marks)
if(ans == True):
    print("Pass")
else:
    print("Fail")
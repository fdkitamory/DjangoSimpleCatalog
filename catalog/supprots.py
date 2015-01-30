
def stringCodesSum(string):
    number = 0
    for i in string:
        number += ord(i)

    return number

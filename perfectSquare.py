def ValidPerfectSquare(number):
    i=1
    while i*i<= number:
        if i*i== number:
            return "perfect Square"
        i+=1
    return "Not a Perfect Square"
num = int(input())
print(ValidPerfectSquare(num))
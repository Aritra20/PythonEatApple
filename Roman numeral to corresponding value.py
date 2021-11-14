def value(roman):
    if (roman == 'I'):
        return 1 
    if (roman == 'V' ):
        return 5 
    if (roman == 'X'):
        return 10
    if (roman == 'L'):
        return 50
    if (roman == 'C'):
        return 100
    if (roman == 'D'):
        return 500
    if (roman == 'M'):
        return 1000
roman_num = input("Enter the roman number: ")
length = len(roman_num)
ans = 0
for i in range (0,length):
    s1 = roman_num[i]
    ans1=value(s1)
    if (i+1 < length):
        s2 = roman_num [i+1]
        ans2=value(s2)
        if (ans1 >= ans2):
            ans= ans +ans1
        else:
            ans= ans+ans2-ans1
            break
    else:
        ans=ans+ans1
print("The roman equivalent is:",ans)
day = input("Enter the day: ")
hours=int(input("Enter the hours: "))
minute=int(input("Enter the minutes: "))

#creating a list of days
daylist=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
i=0
flag=False
while flag == False:
    if day == daylist[i]:
        idx=i
        flag= True
    i=i+1
#Adding 30 minutes to existing minutes
newminute = minute + 30
extra_hour = 0
if(newminute >= 60):
    extra_hour = 1 
    newminute = newminute - 60
#Adding 5 hours to existing hours
newhours=hours + extra_hour + 5 
if(newhours>24):
    newday=daylist[idx+1]
    newhour = newhours -24
else:
    newday=day
print("IST Time:",newday,newhours,":",newminute)
    
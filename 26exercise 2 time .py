#EXERCISE 2
import time
#time is a module which is used to get the current time and date
timestamp=time.strftime("%I:%M:%S %p")
print(timestamp)
# here time.strftime("%I:%M:%S") is used to get the current time in hours, minutes and seconds
timeh=int(time.strftime("%I")) # here time.strftime("%I") is used to get the current hour in 12 hour format
timem=int(time.strftime("%M")) # here time.strftime("%M") is used to get the current minute
timeS=int(time.strftime("%S")) # here time.strftime("%S") is used to get the current second
zone=time.strftime("%p") # here time.strftime("%p") is used to get AM AND PM
if(timeh>1 and  timeh<12 and zone=="AM"):
    print("GOOD MORNING SIR")
elif(timeh>=12 and timeh < 5 and zone=="PM"):
    print("GOOD AFTERNOON SIR")
elif(timeh>=5 and timeh<12 and zone=="PM"):
    print("GOOD EVENING SIR")
else:
    print("GOOD NIGHT SIR")

# %a Locale’s abbreviated weekday name.
# %A Locale’s full weekday name.
# %b Locale’s abbreviated month name.
# %B Locale’s full month name.
# %c Locale’s appropriate date and time representation.
# %d Day of the month as a decimal number [01,31].
# %H Hour (24-hour clock) as a decimal number [00,23].
# %I Hour (12-hour clock) as a decimal number [01,12].
# %m Month as a decimal number [01,12].
# %M Minute as a decimal number [00,59].
# %p Locale’s equivalent of either AM or PM.
# %S Second as a decimal number [00,61].
# %U Week number of the year (Sunday as the first day of the week) as a decimal number [00,53].
# %w Weekday as a decimal number [0(Sunday),6].
# %W Week number of the year (Monday as the first day of the week) as a decimal number [00,53].
# %x Locale’s appropriate date representation.
# %X Locale’s appropriate time representation. 
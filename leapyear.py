def isleapyear(year):
    if type(year) != int:
        return 0
    elif year%4 == 0 and year%100 != 0: 
        str = "true"
        return str
    elif year%100 == 0 and year%400 !=0:
        str = "false"
        return str
    elif year%400 == 0:
        str = "true"
        return str
    else:
        str = "false"
        return str
def isleapyear(year):
    if type(year) != int:
        return 0
    elif year%4 == 0 and year%100 != 0: 
        str = "true"
        return str
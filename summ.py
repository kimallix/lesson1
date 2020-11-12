def get_summ(one, two, delimiter='&'):
    a = str(one)
    b = str(two)

    return "{} {} {}".format(a, delimiter, b).upper()
    
print(get_summ("Learn","Python"))
def comp(principle,rate,time):
    Amount=principle*(pow((1+rate/100),time))
    ci=Amount-principle
    print(ci)
comp(10000,10.25,5)

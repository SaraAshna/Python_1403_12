def salary(exp,job,edu,base_slary):
    salary = base_slary
    salary = salary + .2*exp*salary
    if job ==1: #if job is programmer
        salary += 0.2* salary
    match edu:
        case 'phd':
            salary += .3*salary
        case 'master':
            salary += .2*salary
        case 'bachelor':
            salary += 0.1*salary
        case _:
            pass
        #_ is default
"""
    if edu == 'phd'"
    ""
    =
    return salary

print("18,1,'master',12500000",salary(18,1,"master",12500000))
print("5,0,'bachelor',12500000",salary(5,0,"bachelor",12500000))


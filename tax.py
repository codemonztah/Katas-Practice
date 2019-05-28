monthlySalary=int(input("Enter monthly salary"))
annualSalary=monthlySalary*12
tax=0

tier1=50000000
tier2=25000000000
tier3=50000000000

if annualSalary <=50000000:
    tax=0.05*annualSalary
    print(tax)

elif annualSalary>50000000 and annualSalary<=250000000:
    tax=(0.05*50000000)+(annualSalary-50000000)*0.15
    print(tax)
elif annualSalary>250000000 and annualSalary<=5000000000:
    tax=(0.05*50000000)+(200000000*0.15)+((annualSalary-250000000)*0.25)
    # tax=((annualSalary-250000000)*0.25)
    print(tax)
elif annualSalary>=5000000000:
    tax=(0.05*50000000)+(200000000*0.15)+(250000000*0.25)+((annualSalary-500000000)*0.25)





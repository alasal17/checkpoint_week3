customers = ['James', 'John', 'Robert', 'Mary', 'Patricia', 'Jennifer']
salarys = [155000, 755000,  455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]
customer_salary_tax={}

def fraud_detection():
    fraud_list=[]
    if taxes[0]/salarys[0] <= 0.30:
        fraud_list.append(customers[0])
        print(taxes[0]/salarys[0])
    if taxes[1]/salarys[1] <= 0.30:
        fraud_list.append(customers[1])
        print(taxes[1]/salarys[1])
    if taxes[2]/salarys[2] <= 0.30:
        fraud_list.append(customers[2])
        print(taxes[2]/salarys[2])
    if taxes[3]/salarys[3] <= 0.30:
        fraud_list.append(customers[3])
        print(taxes[3]/salarys[3])
    if taxes[4]/salarys[4] <= 0.30:
        fraud_list.append(customers[4])
        print(taxes[4]/salarys[4])
    if taxes[5]/salarys[5] <= 0.30:
        fraud_list.append(customers[5])
        print(taxes[5]/salarys[5])

    print(fraud_list)

fraud_detection()

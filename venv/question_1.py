customers = ['James', 'John', 'Robert', 'Mary', 'Patricia', 'Jennifer']
salarys = [155000, 755000,  455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]
zipped_lists = zip(taxes,salarys)

def fraud_detection():
    taxe_rate = [taxes / salarys for (taxes, salarys) in zipped_lists]


    for rate, name  in zip(taxe_rate, customers):
        if rate <= 0.30:
            print(name, rate)





fraud_detection()

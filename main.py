from tabulate import tabulate

table = [['First Name','Last Name','Age'],['Aayushi','Agrawal',20],['Vivek','Agrawal',50],['Archana','Agrawal',48]]
print(tabulate(table), headers='firstrows')
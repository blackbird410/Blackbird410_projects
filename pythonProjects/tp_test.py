import numpy as np
import pandas as pd


def data_entry():
    name = []
    f_name = []
    age = []
    n = []
    c = 1
    i = 0
    while c:
        i += 1
        print('__________(' + str(i) + ')__________\n')
        name.append(input('Nom : '))
        f_name.append(input('Prenom : '))
        age.append(int(input('Age : ')))
        n.append(i)
        c = 2
        while c > 1 or c < 0:
            c = int(input('Autre personne ?\n1-Oui  0-Non\n\n'))

    data = {'No': n, 'Nom': name, 'Prenom': f_name, 'Age': age}
    return pd.DataFrame(data)


df = data_entry()
print(df)

import re
import pandas as pd

# a = '222 23 4,5 sdhshda'
# coincidencia = re.findall(r'\d+(?:,\d+)?', a)

# if coincidencia:
#     print(coincidencia)

# a = ['1', '2', '3']
# b = ' '.join(a) + ' '
# c = '1 2 3 fsjkfsdjfs'

# c = c.replace(b,'')
# print(c)

# d = {1:['a','b','hola']}
# c = 'sapo'
# d[1][2] = d[1][2] + ' ' + c

# print(d)

# x = 'hola, mucho, gusto, sapo'
# a = x.split()
# print(a)

b = (
        "maximum power point tracking, "
        "fuzzy-logic based control, "
        "photo voltaic (pv), "
        "photo-voltaic system, "
        "differential evolution algorithm, "
        "evolutionary algorithm, "
        "double-fed induction generator (dfig), "
        "ant colony optimisation, "
        "photo voltaic array, "
        "firefly algorithm, "
        "partial shade"
    )
# Convertir la lista en una sola cadena
cadena_concatenada = ''.join(b)

# Crear un DataFrame con una columna 'prueba'
df = pd.DataFrame({'prueba': [cadena_concatenada]})

datos = df.prueba.to_list()
print(datos)
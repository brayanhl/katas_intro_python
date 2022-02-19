# ------------Problema 1---------------
asteroide = 49
if asteroide > 25:
    print('¡Cuidado, se acerca un asteroide a gran velocidad!')
else:
    print('Todo está bien')

# ------------Problema 2---------------
asteroide = 25
if asteroide >= 20:
    print('Mira, hay una luz en el cielo')
else:
    print('¡No hay nada que ver!')

# ------------Problema 3---------------
velocidad_asteroide = 28
tamano_asteroide = 80
if velocidad_asteroide > 25 and tamano_asteroide > 25 and tamano_asteroide < 1000:
    print('¡Cuidado, un asteroide se dirige directo a la tierra')
elif velocidad_asteroide >= 20:
    print('Mira, hay una luz en el cielo')
elif tamano_asteroide < 25:
    print('Nada que ver aquí :)')
else:
    print('Nada que ver aquí :)')
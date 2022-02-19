#--------------Ejercicio 1---------------
planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno']

print('En total hay', len(planetas), 'planetas')
planetas.append('Plutón')
print(planetas[-1], 'es el último planeta, considerado planeta enano')

#--------------Ejercicio 2---------------
planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno']
otro_planeta = input('Ingrese el nombre de un planeta')
planeta_index = planetas.index(otro_planeta)
print('Estos con los planetas más cercanos al Sol que ' + otro_planeta)
print(planetas[0:planeta_index])
print('estos son los planetas más lejanos al Sol que ' + otro_planeta)
print(planetas[planeta_index + 1:])
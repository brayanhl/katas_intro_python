#---------Ejercicio 1----------
planeta = {
    'nombre': 'Marte',
    'lunas': 2
}
print(f'{planeta["nombre"]} tien {planeta["lunas"]} lunas')
# Agrega la clave circunferencia con los datos proporcionados previamente

planeta['circunferencia (km)'] = {
    'polar': 6752,
    'ecuatorial': 6792
}

print(f'{planeta["nombre"]} tiene una circunferencia polar de {planeta["circumferencia (km)"]["polar"]}')

#------------Ejercicio 2--------------
planet_moons=planeta.get('lunas')
moons = planet_moons.values()
planets = len(planet_moons.keys())
total_moons = 0
for moon in moons:
    total_moons = total_moons + moon
average = total_moons / planets
print(average)
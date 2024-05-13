from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value

# Crear el modelo
model = LpProblem("Optimizacion_de_Transporte_Maritimo", LpMinimize)

# Definir las variables
x = LpVariable("x", lowBound=0, cat='Continuous')
y = LpVariable("y", lowBound=0, cat='Continuous')
z = LpVariable("z", lowBound=0, cat='Continuous')
t = LpVariable("t", lowBound=0, cat='Continuous')
w = LpVariable("w", lowBound=0, cat='Continuous')

# Función objetivo
model += lpSum([x, y, z, t, w])

# Restricciones
model += 50*x + 20*y + 40*z + 40*t + 20*w == 4500
model += 30*x + 50*y + 30*z + 20*t + 60*w == 4400
model += 40*x + 50*y + 60*z + 10*t + 30*w == 5800

# Resolver el problema
model.solve()

# Mostrar resultados
print("Status:", LpStatus[model.status])
print("Valores de las variables:")
print(f"x = {value(x)}")
print(f"y = {value(y)}")
print(f"z = {value(z)}")
print(f"t = {value(t)}")
print(f"w = {value(w)}")
print("Total de viajes minimizados:", value(model.objective))

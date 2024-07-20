import numpy as np
import matplotlib.pyplot as plt


print("Hello World")

a: int = 3
b: int = 9

add = a + b
sub = a - b
div = a / b
mul = a * b

x = np.linspace(1, 100, 1000)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y, '-o', label="Seno(x)")
plt.xlabel("Valores de x")
plt.ylabel("Seno de x")
plt.title("Gráfico do Seno de x")
plt.show()

plt.plot(x,z)


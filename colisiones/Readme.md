# Robot Collisions

Este proyecto contiene una función `robot_collisions` que calcula cuántas veces colisiona cada robot en una secuencia dada. 
La secuencia está compuesta por los símbolos "R" (robots moviéndose hacia la derecha) y "L" (robots moviéndose hacia la izquierda).

## Uso

```python
from robot_collisions import robot_collisions

result = robot_collisions('RRL')
print(result)  # Debería mostrar '1 2 1'

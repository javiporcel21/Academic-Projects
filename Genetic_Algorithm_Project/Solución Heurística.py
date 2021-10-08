import numpy as matriz
# Definir variables
soluciones = matriz.zeros((100, 8))
x0grua = matriz.array([5, 0, 5])
xgrua = matriz.array([5, 0, 5])
iotierra = matriz.array([5, 43, 2])
iomar = matriz.array([5, 0, 1])
procedencia =matriz.array([2, 2, 2, 1, 1, 1, 2, 2])
tllegada = matriz.array([158, 144, 69, 158, 196, 9, 34, 95])
huecos = matriz.array([[7, 41, 4],
                       [9, 12, 3],
                       [8, 38, 1],
                       [7, 9, 2],
                       [2, 23, 3],
                       [2, 21, 4],
                       [3, 15, 1],
                       [6, 24, 4],
                       [9, 1, 4],
                       [10, 6, 3],
                       [1, 38, 2],
                       [5, 31, 2],
                       [2, 34, 1],
                       [1, 3, 3],
                       [3, 18, 3],
                       [10, 19, 2]])
huecosoriginales = huecos
#####
# Ordenar contenedores en orden de llegada
orden = matriz.array([0, 0, 0, 0, 0, 0, 0, 0]) 
orden = matriz.argsort(tllegada)
soluciones[0] = orden
distancias = matriz.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#####
#Mover contenedores
movimientos = 0
def distancia(x, y):
    return max(abs(x[0] - y[0]), abs(x[1] - y[1])) + (5 - x[2]) + (5 - y[2])
 
if procedencia[orden[0]] == 1:
    movimientos = max([distancia(xgrua, iomar), tllegada[orden[0]]])
    xgrua = iomar
else:
    movimientos = max([distancia(xgrua, iotierra), tllegada[orden[0]]])
    xgrua = iotierra
    
for i in range(0, 16):
    distancias[i] = distancia(xgrua, huecos[i])

dvecino = min(distancias)
movimientos = movimientos + dvecino
vecino = matriz.where(distancias == dvecino)
vecinocercano = matriz.array(vecino[0])
soluciones[1][0] = matriz.array(vecinocercano[0])
xgrua = matriz.array(huecos[vecinocercano[0]])
huecos[vecinocercano[0]] = [1000, 0, 5]

if procedencia[orden[1]] == 1:
    movimientos = max([movimientos + distancia(xgrua, iomar), tllegada[orden[1]]])
    xgrua = iomar
else:
    movimientos = max([movimientos + distancia(xgrua, iotierra), tllegada[orden[1]]])
    xgrua = iotierra
    
for i in range(0, 16):
    distancias[i] = distancia(xgrua, huecos[i])

dvecino = min(distancias)
movimientos = movimientos + dvecino
vecino = matriz.where(distancias == dvecino)
vecinocercano = matriz.array(vecino[0])
soluciones[1][1] = matriz.array(vecinocercano[0])
xgrua = matriz.array(huecos[vecinocercano[0]])
huecos[vecinocercano[0]] = [1000, 0, 5]

if procedencia[orden[2]] == 1:
    movimientos = max([movimientos + distancia(xgrua, iomar), tllegada[orden[2]]])
    xgrua = iomar
else:
    movimientos = max([movimientos + distancia(xgrua, iotierra), tllegada[orden[2]]])
    xgrua = iotierra
    
for i in range(0, 16):
    distancias[i] = distancia(xgrua, huecos[i])

dvecino = min(distancias)
movimientos = movimientos + dvecino
vecino = matriz.where(distancias == dvecino)
vecinocercano = matriz.array(vecino[0])
soluciones[1][2] = matriz.array(vecinocercano[0])
xgrua = matriz.array(huecos[vecinocercano[0]])
huecos[vecinocercano[0]] = [1000, 0, 5]

if procedencia[orden[3]] == 1:
    movimientos = max([movimientos + distancia(xgrua, iomar), tllegada[orden[3]]])
    xgrua = iomar
else:
    movimientos = max([movimientos + distancia(xgrua, iotierra), tllegada[orden[3]]])
    xgrua = iotierra
    
for i in range(0, 16):
    distancias[i] = distancia(xgrua, huecos[i])

dvecino = min(distancias)
movimientos = movimientos + dvecino
vecino = matriz.where(distancias == dvecino)
vecinocercano = matriz.array(vecino[0])
soluciones[1][3] = matriz.array(vecinocercano[0])
xgrua = matriz.array(huecos[vecinocercano[0]])
huecos[vecinocercano[0]] = [1000, 0, 5]

if procedencia[orden[4]] == 1:
    movimientos = max([movimientos + distancia(xgrua, iomar), tllegada[orden[4]]])
    xgrua = iomar
else:
    movimientos = max([movimientos + distancia(xgrua, iotierra), tllegada[orden[4]]])
    xgrua = iotierra
    
for i in range(0, 16):
    distancias[i] = distancia(xgrua, huecos[i])

dvecino = min(distancias)
movimientos = movimientos + dvecino
vecino = matriz.where(distancias == dvecino)
vecinocercano = matriz.array(vecino[0])
soluciones[1][4] = matriz.array(vecinocercano[0])
xgrua = matriz.array(huecos[vecinocercano[0]])
huecos[vecinocercano[0]] = [1000, 0, 5]

if procedencia[orden[5]] == 1:
    movimientos = max([movimientos + distancia(xgrua, iomar), tllegada[orden[5]]])
    xgrua = iomar
else:
    movimientos = max([movimientos + distancia(xgrua, iotierra), tllegada[orden[5]]])
    xgrua = iotierra
    
for i in range(0, 16):
    distancias[i] = distancia(xgrua, huecos[i])

dvecino = min(distancias)
movimientos = movimientos + dvecino
vecino = matriz.where(distancias == dvecino)
vecinocercano = matriz.array(vecino[0])
soluciones[1][5] = matriz.array(vecinocercano[0])
xgrua = matriz.array(huecos[vecinocercano[0]])
huecos[vecinocercano[0]] = [1000, 0, 5]

if procedencia[orden[6]] == 1:
    movimientos = max([movimientos + distancia(xgrua, iomar), tllegada[orden[6]]])
    xgrua = iomar
else:
    movimientos = max([movimientos + distancia(xgrua, iotierra), tllegada[orden[6]]])
    xgrua = iotierra
    
for i in range(0, 16):
    distancias[i] = distancia(xgrua, huecos[i])

dvecino = min(distancias)
movimientos = movimientos + dvecino
vecino = matriz.where(distancias == dvecino)
vecinocercano = matriz.array(vecino[0])
soluciones[1][6] = matriz.array(vecinocercano[0])
xgrua = matriz.array(huecos[vecinocercano[0]])
huecos[vecinocercano[0]] = [1000, 0, 5]

if procedencia[orden[7]] == 1:
    movimientos = max([movimientos + distancia(xgrua, iomar), tllegada[orden[7]]])
    xgrua = iomar
else:
    movimientos = max([movimientos + distancia(xgrua, iotierra), tllegada[orden[7]]])
    xgrua = iotierra
    
for i in range(0, 16):
    distancias[i] = distancia(xgrua, huecos[i])

dvecino = min(distancias)
movimientos = movimientos + dvecino
vecino = matriz.where(distancias == dvecino)
vecinocercano = matriz.array(vecino[0])
soluciones[1][7] = matriz.array(vecinocercano[0])
xgrua = matriz.array(huecos[vecinocercano[0]])
huecos[vecinocercano[0]] = [1000, 0, 5]

##############################################################################
for i in range(1, 7):
    if procedencia[orden[i]] == 1:
        movimientos = max([movimientos + distancia(xgrua, iomar), tllegada[orden[i]]])
        xgrua = iomar
    else:
        movimientos = max([movimientos + distancia(xgrua, iotierra), tllegada[orden[i]]])
        xgrua = iotierra
    for k in range (0, 16):
        distancias[k] = distancia(xgrua, huecos[i])
    dvecino = min(distancias)
    movimientos = movimientos + dvecino
    vecino = matriz.where(distancias == dvecino)
    vecinocercano = matriz.array(vecino[0])
    soluciones[1][i] = matriz.array(vecinocercano[0])
    xgrua = matriz.array(huecos[vecinocercano[0]])
    huecos[vecinocercano[0]] = [1000, 0, 5]

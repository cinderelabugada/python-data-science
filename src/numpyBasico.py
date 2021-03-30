import numpy as np

"""
1. Tipos de dados (declaração de vetores)
"""

# Declaração utilizando listas
arrList = np.array([1, 2, 3])
print('arrList', arrList)
print(type(arrList))

# Declaração utilizando tuplas
arrTuple = np.array((1, 2, 3))
print('arrTuple', arrTuple)

# Declarações com dimensões:

# Declaração de escalar 0D
arrEscalar = np.array(42)
print('arrEscalar', arrEscalar)
print(type(arrEscalar))

# Declaração de vetores com 1D
arr1D = np.array([6, 7, 8, 9])
print('arr1D', arr1D)

# Declaração de vetores com 2D (Matrizes)
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print('arr2D', arr2D)

# Declaração de vetores com 3D
arr3D = np.array([ [[1, 2, 3]], [[3,2,1]] ])
print('arr3D', arr3D)
print(arr3D.ndim)

# Declaração de vetores com n dimensões
arr5D = np.array([1, 2, 3], ndmin=5)

"""
2. Índices
"""
# Os índices descem cada nível de dimensão
print('arr1D[1]', arr1D[1])
print('arr2D[0, 1]', arr2D[1, 1])
print('arr3D[1, 0, 2]', arr3D[1, 0, 2])
print('arr3D[1]', arr3D[1])
print('arr3D[1][0][2]', arr3D[1][0][2])

# índices negativos:
print('\níndices negativos')
print('arr1D[-1]', arr1D[-1])

"""
3. Slicing
"""
print('\n 3.Slicing')
print('arr1D[1:3]', arr1D[1:3])
print('arr1D[1:]', arr1D[1:])
print('arr1D[:3]', arr1D[:3])
print('arr1D[-3:-1]', arr1D[-3:-1])

arrStep = np.array([9, 8, 7, 6, 5, 4])
print('arrStep[1:5:2]', arrStep[1:6:2])

# primeiro : significa do inicio ao fim do vetor
# segundo : demarca o step (salto)
print('arrStep[::2]', arrStep[::2])

print('arr2D[0, 1:3]', arr2D[0, 1:3])
print('arr2D[0:2, 2]', arr2D[0:2, 1])

# Tipos de dados
arrInt = np.array([1, 2, 3, 4])
print('dtype', arrInt.dtype)

arrString = np.array([1, 2, 3, 4], dtype='f')
print('arrString', arrString)
print('arrString', arrString.dtype)

# Dado estruturado
dt = np.dtype([('name', np.unicode_, 16),
                    ('age', np.int64)])

print('dt["name"]', dt['name'])

pessoas = np.array([('cinderela', 10), ('bugada', 15)], dtype=dt)
print('pessoas[0]["name"]', pessoas[0]['name'])
print('pessoas["name"]', pessoas['name'])

"""
4. Propriedades de vetor
"""

# Shape: retorna uma tupla com formato do vetor, sendo que cada
# elemento representa o número de elementos em cada dimensão
arrShape = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('shape', arrShape.shape)
print('ndim', arrShape.ndim)

print('arr5D', arr5D)
print('shape5D', arr5D.shape)
print('shape5D', arr5D.ndim)

# Reshape: altera o formato de um vetor para o especificado
# Obs: o vetor de origem deve comportar o novo shape
arrLongo = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
)

print('arrLongo shape', arrLongo.shape)
arrReshape = arrLongo.reshape(5, 3)
print('arrReshape (5, 3)', arrReshape)

# reshape permite reduzir o número de dimensões para 1
print('unReshape', arrReshape.reshape(-1))

# percorre cada dimensão do array
print('percorre elementos das dimensões com for')
for x in arrReshape: # percorre primeira dimensão
    print('1a dim', x)
    for y in x: # percorre segunda dimensão
        print('2a dim', y)

print('percorre elementos das dimensões com iter')
for x in np.nditer(arrReshape):
    print(x)

print('percorre vetore com saltos')
arrIterStep = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arrIterStep[:, ::2]):
    print(x)

# concatena duas matrizes por linha
print('concatenação')
arrConc1 = np.array([[1, 2], [3, 4]])
arrConc2 = np.array([[5, 6], [7, 8]])
print('arrConc1, arrConc2, axis=1',
      np.concatenate((arrConc1, arrConc2), axis=1))

arrConc1 = np.array([[[1, 2]], [[3, 4]]])
arrConc2 = np.array([[[5, 6]], [[7, 8]]])
print('arrConc1, arrConc2, axis=2',
      np.concatenate((arrConc1, arrConc2), axis=2))

# stack: concatena dois vetores e armazena o resultado em
# um novo eixo, semelhante ao zip
arrStack1 = np.array([1, 2, 3])
arrStack2 = np.array([4, 5, 6])

print('stack')
print('arrStack1, arrStack2',
      np.stack((arrStack1, arrStack2), axis=1))

print('stack ao longo das linhas')
print('arrStack1, arrStack2',
      np.hstack((arrStack1, arrStack2)))

print('stack ao longo das colunas')
print('arrStack1, arrStack2',
      np.vstack((arrStack1, arrStack2)))

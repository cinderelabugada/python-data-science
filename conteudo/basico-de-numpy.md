# Básico sobre NumPy

Nesse tópico serão abordados aspectos básicos sobre numpy, como tipo de dados e algumas funções de suas funções mais simples.

### Conteúdo

1. Tipos de Dados

   O numpy introduz o tipo array próprio, que como o nome já sugere, é utilizado para representar vetores. Apesar de parecer uma estrutura simples, o array é bastente poderoso, de forma que através dele é possível declara não apenas vetores mas também matrizes, além de objetos mais complexos ainda. Para isso o numpy trabalha o conceito de dimensões, que a primeira vista pode ser um conceito um pouco confuso.

| Valor | Dimensão | Descrição | Numpy |
| :--- | :--- | :--- | :--- |
| $$25$$  | 0D | Escalar | np.array\(25\) |
| $$[1, 2, 3]$$  | 2D | Vetor | np.array\(\[1, 2, 3\]\) |
| $$[[ 1, 2, 3], [4, 5, 6 ]]$$  | 3D | Matriz | np.array\(\[\[1, 2, 3\], \[4, 5, 6\]\]\) |
|  $$[[[[[1, 2, 3]]]]]$$  | 5D | - | np.array\(\[1, 2, 3\], ndmin=5\) |



1. Declaração \(0D, 1D, 3D, ndmin\)
2. Índices
3. Slicing
4. [Tipos básicos e vetores com tipo pré-definido](https://www.geeksforgeeks.org/numpy-data-type-objects/?ref=lbp)
5. Operações com vetores
   * [Copy & View, Shape, Reshape, Iterating, Join, Split, Search, Sort, Filter](https://www.w3schools.com/python/numpy)
   * [Álgebra Linear](https://www.geeksforgeeks.org/numpy-linear-algebra/?ref=lbp)
6. Vetorização com ufunc

### Referências:

[W3School NumPy Tutorial](https://www.w3schools.com/python/numpy/default.asp)

[GeeksForGeeks](https://www.geeksforgeeks.org/python-numpy-tutorial)


# NLP

## Processamento de Linguagem Natural

O processamento de linguagem natural permite que o os computadores interpretem os diversos aspectos que compreendem a linguagem dos seres humanos. Dessa forma, essa área tenta resolver diversas tarefas que envolvem a comunicação humana que vão desde verificação ortográfica à análise semântica de textos.

### Representação

Um ponto comum de todas as tarefas que envolvem o processamento de linguagem natural é a representação das palavras. Ao contrário do censo comum na computação de se pensar a representação de palavras como cadeia de caracteres, para o processamento de linguagem natural essa representação é realizada através de vetores \(word vectors\). Isso ocorre pois, parte fundamental dessa área consiste em analisar a relação entre as palavras, em geral utilizando métricas de distância como Jaccard, Cosseno e Euclidiana.  Ao longo dos anos essa forma de representação foi evoluindo a fim otimizar  o espaço utilizado pela representação quanto seu tempo de criação, além de melhor se adaptarem as tarefes a serem realizadas.

#### Exemplos de Word Vectors \(Word Embenddings\)

1. **One-Hot:** Nessa representação o "espaço" das palavras da língua com um todo é considerado na representação de uma palavra. Assim, cada componente \(ou coluna\) dos vetores de palavras corresponde à uma palavra do vocabulário. Dessa forma para se representar uma palavra basta que nesse vetor a coluna correspondente à palavra seja atribuído o valor 1, e as demais colunas sejam iguais à 0. O principal problema dessa representação é que a mesma não atribui informação de similaridade entre as palavras, como gênero, tempo verbal, contagem \(singular e plural\).
2. **Baseados em SVD:** Esses métodos utilizam a decomposição por valor sigular \(SVD\) para criar os vetores de representação \($$M = USV^T$$\) . A matriz $$M$$ a ser decomposta, pode ser criada de duas formas, a primeira é através da contagem da coocorrência de cada palavra em cada documento \( $$|M| = |v| *|d|$$ \), e a segunda considera a coocorrência apenas em uma janela de palavras \( $$|M| = |v|*|v|$$ \). Ambas as abordagens produzem resultados que podem contêm as relações semânticas entre as palavras do vocabulário, sendo nesse sentido um método melhor que o One-Hot. Por outro lado existem outros diversos problemas como matrizes esparsas, atualização do vocabulário pela adição de novos documentos requer o recalculo da decomposição, dentre outros problemas.
3. **Métodos Iterativos:** Como o nome sugere, esse método utiliza uma série de iterações sobre um conjunto de textos, no qual a cada iteração o mesmo aprende as probabilidades da representação em vetor em relação às palavras coocorrem em seu contexto \(janela de palavras\). Um dos métodos mais populares ẃ o word2vec com o CBOW e skip-gram.

### Referências

[CS224n: Natural Language Processing with Deep Learning](http://web.stanford.edu/class/cs224n/)


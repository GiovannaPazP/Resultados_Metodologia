# Resultados_Metodologia
Códigos e resultados obtidos para os casos de teste usados nos algoritmos quickSort, insertionSort, selectionSorte e bubbleSort.

A pasta contém, além desse readme, os códigos (quickSort.c, insertionSort.c, selectionSort.c e bubbleSort.c), uma pasta 'dados' contendo as pastas 'valgring' e 'graficos' dentro e o makefile.
Existem duas pastas extras, cuja explicação se encontra mais abaixo.

Segue abaixo a lista de comandos e o que fazem.
(Esses comandos devem ser rodados dentro do diretório codigos).

make
|-> compila o código.
make testes
|-> executa o código para n=10, 100, 1000, 10000, 100000, 1000000 e 10000000. Sem valgrind.
make testesValgrind
|-> executa o código para n=10, 100, 1000, 10000, 100000, 1000000 e 10000000. Com valgrind.
make clean
|-> remove todos os arquivos gerados com a compilação e a execução.

Os resultados obtidos com a execução vão para a pasta dados.

Sobre os resultados.
Os resultados usados para a comparação dos três algoritmos foram feitos rodando o comando make testes. Porém, devido a questões de tempo hábil de computação, é possível notar que não há resultados para a ordenação de vetores de tamanho 10000000 além do quickSort ordenado.
    Isso aconteceu devido a sequência de algoritmos utilizada, ou seja, a execução para o vetor de tamanho 10000000 ficou presa ao selectionSort.
    Devido a isso, foi gerado novos resultados com um arquivo makefile modificado, nesse arquivo as linhas 36 a 40 da regra testes, referentes a execução dos demais algoritmos, foi comentada. Isso foi o que permitiu gerar os dados completos do quickSort para todos os casos.
Foi feita também uma outra leva de testes considerando o pior caso do quickSort, que ocorre quando o pivô escolhido é de uma das extremidades. Para fazer isso, dentro de quickSort.c foi comentada a linha 15 da função partição e descomentada a linha 14, essas linhas eram referentes a, respectivamente, a seleção do pivô pelo meio do vetor [(ini+fim)/2] e a seleção do pivô pelo primeiro elemento [ini].
    Com isso, obtemos resultados para vetores de até 100000, em todos os tipos (ordenado, reversamente ordenaedos e aleatórios). Os resultados com 1000000 e 10000000 não foram possíveis de obter pois resultou em falha de segmentação.

Obs: O algoritmo quickSort implementado aqui ordena o vetor em ordem decrescente.
Obs2: Os dados gerados estão todos destinados a mesma pasta, ou seja, ao rodar os outros testes, irá sobreescrever os dados anteriores. Devido a isso, os dados extras acima foram salvos com nomes diferentes após rodarem.

Para gerar os gráficos, é necessário ter o Python3 instalado, assim como as bibliotecas pandas, matplotlib e seaborn.
Feito isso, basta rodar o comando:
python3 grafico.py
O script gera os gráficos e os salva na pasta dados/graficos.

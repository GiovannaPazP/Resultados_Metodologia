CXX = gcc
CXXFLAGS = -Wall

SRC_QUICK = quickSort.c
SRC_SELECT = selectionSort.c
SRC_INSERT = insertionSort.c
SRC_BUBBLE = bubbleSort.c

EXEC_QUICK = quickSort
EXEC_SELECT = selectionSort
EXEC_INSERT = insertionSort
EXEC_BUBBLE = bubbleSort

all: $(EXEC_QUICK) $(EXEC_SELECT) $(EXEC_INSERT) $(EXEC_BUBBLE)
$(EXEC_QUICK): $(SRC_QUICK)
	$(CXX) $(CXXFLAGS) -o $(EXEC_QUICK) $(SRC_QUICK)

$(EXEC_SELECT): $(SRC_SELECT)
	$(CXX) $(CXXFLAGS) -o $(EXEC_SELECT) $(SRC_SELECT)

$(EXEC_INSERT): $(SRC_INSERT)
	$(CXX) $(CXXFLAGS) -o $(EXEC_INSERT) $(SRC_INSERT)

$(EXEC_BUBBLE): $(SRC_BUBBLE)
	$(CXX) $(CXXFLAGS) -o $(EXEC_BUBBLE) $(SRC_BUBBLE)

testes:
	for n in 10 100 1000 10000 100000 1000000 10000000; do \
		for tipo in 0 1 2; do \
			if [ $$tipo -eq 0 ]; then nome="ordenado"; fi; \
			if [ $$tipo -eq 1 ]; then nome="aleatorio"; fi; \
			if [ $$tipo -eq 2 ]; then nome="reverso"; fi; \
			echo "==== Tamanho $$n ($$nome) ====" >> ../dados/quick_$$nome\_$$n.txt; \
			./quickSort $$n $$tipo >> ../dados/quick_$$nome\_$$n.txt; \
			#echo "==== Tamanho $$n ($$nome) ====" >> ../dados/selection_$$nome\_$$n.txt; \
			#./selectionSort $$n $$tipo >> ../dados/selection_$$nome\_$$n.txt; \
			#echo "==== Tamanho $$n ($$nome) ====" >> ../dados/insertion_$$nome\_$$n.txt; \
			#./insertionSort $$n $$tipo >> ../dados/insertion_$$nome\_$$n.txt; \
			#echo "==== Tamanho $$n ($$nome) ====" >> ../dados/bubble_$$nome\_$$n.txt; \
			#./bubbleSort $$n $$tipo >> ../dados/bubble_$$nome\_$$n.txt; \
		done \
	done

testesValgrind:
	for n in 10 100 1000 10000 100000 1000000 10000000; do \
		for tipo in 0 1 2; do \
			if [ $$tipo -eq 0 ]; then nome="ordenado"; fi; \
            if [ $$tipo -eq 1 ]; then nome="aleatorio"; fi; \
            if [ $$tipo -eq 2 ]; then nome="reverso"; fi; \
            echo "==== Tamanho $$n ($$nome) ====" >> ../dados/valgrind/quick_$$nome\_$$n.txt; \
            valgrind --tool=massif --stacks=yes --massif-out-file=../dados/quick_mem_$$n_$$nome.out ./quickSort $$n $$tipo >> ../dados/valgrind/quick_$$nome\_$$n.txt; \
            ms_print ../dados/quick_mem_$$n_$$nome.out | awk '/n *time\(i\) *total\(B\)/, /^$$/' >> ../dados/valgrind/quick_$$nome\_$$n.txt; \
            rm -f ../dados/quick_mem_$$n_$$nome.out; \
			echo "==== Tamanho $$n ($$nome) ====" >> ../dados/valgrind/selection_$$nome\_$$n.txt; \
            valgrind --tool=massif --stacks=yes --massif-out-file=../dados/selection_mem_$$n_$$nome.out ./selectionSort $$n $$tipo >> ../dados/valgrind/selection_$$nome\_$$n.txt; \
            ms_print ../dados/selection_mem_$$n_$$nome.out | awk '/n *time\(i\) *total\(B\)/, /^$$/' >> ../dados/valgrind/selection_$$nome\_$$n.txt; \
            rm -f ../dados/selection_mem_$$n_$$nome.out; \
			echo "==== Tamanho $$n ($$nome) ====" >> ../dados/valgrind/insertion_$$nome\_$$n.txt; \
            valgrind --tool=massif --stacks=yes --massif-out-file=../dados/insertion_mem_$$n_$$nome.out ./insertionSort $$n $$tipo >> ../dados/valgrind/insertion_$$nome\_$$n.txt; \
            ms_print ../dados/insertion_mem_$$n_$$nome.out | awk '/n *time\(i\) *total\(B\)/, /^$$/' >> ../dados/valgrind/insertion_$$nome\_$$n.txt; \
            rm -f ../dados/insertion_mem_$$n_$$nome.out; \
			echo "==== Tamanho $$n ($$nome) ====" >> ../dados/valgrind/bubble_$$nome\_$$n.txt; \
            valgrind --tool=massif --stacks=yes --massif-out-file=../dados/bubble_mem_$$n_$$nome.out ./bubbleSort $$n $$tipo >> ../dados/valgrind/bubble_$$nome\_$$n.txt; \
            ms_print ../dados/bubble_mem_$$n_$$nome.out | awk '/n *time\(i\) *total\(B\)/, /^$$/' >> ../dados/valgrind/bubble_$$nome\_$$n.txt; \
            rm -f ../dados/bubble_mem_$$n_$$nome.out; \
        done \
    done
		

clean:
	rm -f $(EXEC_BUBBLE) $(EXEC_INSERT) $(EXEC_SELECT) $(EXEC_QUICK) ../dados/*.out ../dados/*.txt ../dados/valgrind/*.out ../dados/valgrind/*.txt

.PHONY: all clean testes testesValgrind
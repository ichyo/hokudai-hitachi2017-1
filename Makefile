all: ./bin/graph_generator ./bin/score_evaluator ./input

./bin/graph_generator: ./scripts/graph_generator.cpp
	g++ -std=gnu++11 -O2 -o ./bin/graph_generator ./scripts/graph_generator.cpp

./bin/score_evaluator: ./scripts/score_evaluator.cpp
	g++ -O2 -o ./bin/score_evaluator ./scripts/score_evaluator.cpp

./input: ./bin/graph_generator
	./generate_input.sh

clean:
	rm -f ./bin/*
	rm -rf ./input/*

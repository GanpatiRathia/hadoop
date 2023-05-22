import sys

def mapper(_, line):
    words = line.strip().split()
    for word in words:
        yield word, None

def reducer(word, _):
    yield word

if __name__ == '__main__':
    # Read input file
    input_file = sys.argv[1]

    # Mapper phase
    with open(input_file, 'r') as file:
        mapper_output = [pair for line in file for pair in mapper(None, line)]

    # Sort the mapped output
    sorted_output = sorted(mapper_output, key=lambda x: x[0])

    # Reducer phase
    for word, _ in sorted_output:
        for result in reducer(word, None):
            print(result)
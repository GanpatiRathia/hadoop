import sys

def mapper(_, line):
    target_string = sys.argv[2]  # Get the target string from command line argument
    longest_common_substring = ""
    for i in range(len(line) - len(target_string) + 1):
        substring = line[i:i + len(target_string)]
        if substring == target_string and len(substring) > len(longest_common_substring):
            longest_common_substring = substring
    yield longest_common_substring, None

def reducer(longest_common_substring, _):
    yield longest_common_substring

if __name__ == '__main__':
    # Read input file
    input_file = sys.argv[1]

    # Mapper phase
    with open(input_file, 'r') as file:
        mapper_output = [pair for line in file for pair in mapper(None, line)]

    # Reducer phase
    longest_substring = ""
    for substring, _ in mapper_output:
        if len(substring) > len(longest_substring):
            longest_substring = substring

    print("Longest common substring:", longest_substring)

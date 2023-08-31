import re
import sys

def process_file(input_filename, output_filename):
    # Define the regex pattern
    pattern = re.compile(r'^[A-Z][a-z][a-z]\s\d+')

    with open(input_filename, 'r') as infile:
        lines = infile.readlines()

    with open(output_filename, 'w') as outfile:
        for line in lines:
            # If the line matches the regex pattern, write a newline before it
            if pattern.match(line):
                outfile.write('\n')
            outfile.write(line)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py input_filename output_filename")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    process_file(input_filename, output_filename)

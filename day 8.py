def analyze_file(file_name):
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            total_words = sum(len(line.split()) for line in lines)
            print(f"Number of lines: {len(lines)}")
            print(f"Number of words: {total_words}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")

analyze_file('notes.txt')

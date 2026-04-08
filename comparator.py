import sys

def get_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def main(file1, file2):
    content1 = get_file_content(file1)
    content2 = get_file_content(file2)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
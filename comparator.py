import sys

def get_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def compare_lines(set1, set2):
    same = sorted(list(set1.intersection(set2)))
    diff = sorted(list(set1.symmetric_difference(set2)))
    return same, diff        

def save_to_file(lines, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def main(file1, file2):
    content1 = get_file_content(file1)
    content2 = get_file_content(file2)

    same, diff = compare_lines(content1, content2)

    save_to_file(same, "same.txt")
    save_to_file(diff, "diff.txt")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
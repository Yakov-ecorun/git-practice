import sys

if len(sys.argv) < 2:
    print("Usage: python3 app.py <file>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)

line_count = len(lines)
word_count = 0

for line in lines:
    word_count += len(line.split())

print(f"File: {file_path}")
print(f"Lines: {line_count}")
print(f"Words: {word_count}")

sys.exit(0)

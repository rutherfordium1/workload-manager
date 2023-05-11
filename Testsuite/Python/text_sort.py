with open("unsorted.txt", "r") as f:
    lines = f.readlines()

sorted_lines = sorted(lines)

with open("sorted.txt", "w") as f:
    for line in sorted_lines:
        f.write(line)

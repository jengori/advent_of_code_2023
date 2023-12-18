def get_matching(rows_or_columns):
    return [i for i in range(len(rows_or_columns) - 1) if rows_or_columns[i] == rows_or_columns[i + 1]]


def is_line_of_reflection(row_or_col_index, rows_or_cols):
    if row_or_col_index == 0 or row_or_col_index == len(rows_or_cols)-2:
        return True
    i = 1

    while True:
        if rows_or_cols[row_or_col_index - i] == rows_or_cols[row_or_col_index + i + 1]:
            i += 1
            if row_or_col_index - i < 0 or row_or_col_index + i + 1 > len(rows_or_cols)-1:
                return True

        else:
            return False


def get_summary(rows):
    cols = ["".join([line[n] for line in rows]) for n in range(len(rows[0]))]
    matching_rows = get_matching(rows)
    matching_cols = get_matching(cols)

    for row in matching_rows:
        if is_line_of_reflection(row, rows):
            return (row+1)*100
    for col in matching_cols:
        if is_line_of_reflection(col, cols):
            return col+1


def read_patterns(file):
    with open(file) as f:
        data = [line.strip() for line in f.readlines()]

    blank_lines = [i for i, line in enumerate(data) if line == ""]
    blank_lines.append(len(data))

    patterns = [[data[i] for i in range(len(data)) if 0 <= i < blank_lines[0]]]
    for i in range(len(blank_lines) - 1):
        patterns.append([data[j] for j in range(len(data)) if blank_lines[i] < j < blank_lines[i + 1]])

    return patterns


def solve(patterns):
    result = 0
    for rows in patterns:
        result += get_summary(rows)
    return result


my_patterns = read_patterns("input.txt")
print(solve(my_patterns))

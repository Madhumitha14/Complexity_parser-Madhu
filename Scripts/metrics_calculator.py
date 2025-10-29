import radon.metrics
import radon.complexity

def count_lines_of_code(file_path):
    with open(file_path, "r", encoding = "utf-8") as f:
        lines = f.readlines()

    code_lines = [line for line in lines if line.strip() != ""]
    return len(code_lines)

def calculate_cyclomatic_complexity(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    result = radon.complexity.cc_visit(content)
    total_complexity = sum([entry.complexity for entry in result])
    return total_complexity
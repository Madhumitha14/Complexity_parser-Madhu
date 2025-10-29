import os
import ast
import csv
import radon.metrics
import radon.complexity

from metrics_calculator import count_lines_of_code, calculate_cyclomatic_complexity
from List_of_python_files import list_python_files
from extract_and_count import extract_functions,count_function_calls

project_directory = "C:/Users/DELL/robotframework"  #project directory
python_files = list_python_files(project_directory) #get the list of python files

csv_file_path = "combined_function_metrics.csv"

with open(csv_file_path, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Python File", "Function Name", "Lines of Code", "Cyclomatic Complexity", "Number of Calls",
                         "Functions Called"])

    # Loop through Python files
    for python_file in python_files:
        functions = extract_functions(python_file)
        for function_name in functions:
            lines_of_code = count_lines_of_code(python_file)
            complexity = calculate_cyclomatic_complexity(python_file)

            with open(python_file, "r", encoding="utf-8") as f:
                code = f.read()
                parsed_tree = ast.parse(code)
                function_node = None
                for node in ast.walk(parsed_tree):
                    if isinstance(node, ast.FunctionDef) and node.name == function_name:
                        function_node = node
                        break

                call_dict = count_function_calls(function_node) if function_node else {}

                num_calls = len(call_dict)
                functions_called_str = ', '.join(call_dict.keys())

                csv_writer.writerow(
                    [python_file, function_name, lines_of_code, complexity, num_calls, functions_called_str])

print("Function metrics and function calls have been saved to combined_function_metrics.csv")
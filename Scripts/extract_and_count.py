#Function to extract function names from a file
import ast
def extract_functions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    tree = ast.parse(content)
    function_names = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_names.append(node.name)

    return function_names

def count_function_calls(node, caller_function_name=None, call_dict=None):
    if caller_function_name is None:
        caller_function_name = node.name
        call_dict = {}

    if isinstance(node, ast.FunctionDef):
        function_name = node.name
        function_calls = [n for n in ast.walk(node) if isinstance(n, ast.Call)]

        for call in function_calls:
            if isinstance(call.func, ast.Name):
                called_function_name = call.func.id
                if called_function_name not in call_dict:
                    call_dict[called_function_name] = [caller_function_name]
                else:
                    call_dict[called_function_name].append(caller_function_name)

    for child_node in node.body:  # Only traverse the body of the function
        if isinstance(child_node, ast.FunctionDef):
            count_function_calls(child_node, caller_function_name, call_dict)

    return call_dict

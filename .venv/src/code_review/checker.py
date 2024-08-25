import ast


class SecurityChecker:
    def __init__(self, code):
        self.code= code

    def check_Insecure_Imports(self):
        insecure_imports = ['pickle', 'eval']
        for line_num , line in enumerate(self.code.split('\n')):
            if any(insecure_import in line for insecure_import in insecure_imports):
                print(f"Insecure import found at line {line_num + 1}: {line.strip()}")


class PerformanceChecker:
    def __init__(self, code):
        self.code= code

    def check_heavy_loops(self):
        tree = ast.parse(self.code)
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                if len(node.body) > 5:
                    print(f"Heavy loop at line {node.lineno}")


if __name__ == "__main__":
    with open('path_to_your_code_file.py', 'r') as file:
        code = file.read()
    sec_checker = SecurityChecker(code)
    perf_checker = PerformanceChecker(code)
    sec_checker.check_insecure_imports()
    perf_checker.check_heavy_loops()


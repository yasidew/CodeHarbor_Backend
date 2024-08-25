# in this file we are going to implement the code analyzer class which will be responsible for running the pylint and custom rules check
#Runs pylint for general coding standards. Checks for custom rules, such as function length.

import pylint.lint
import ast

class CodeAnalyzer:
    def __init__ (self, code): #constructor
        self.code = code

    def run_pylint(self):
        pylint_opts = ['--disable=all', '--enable=E,W,C,R', '--output-format=json'] #setting the pylint options
        pylint.lint.Run(pylint_opts)

    def custom_rules_check(self):
        tree =  ast.parse(self.code) #in here we are parsing the code to an abstract syntax tree
        self._check_function_length(tree)  #calling the function to check the function length

    def _check_function_length(self, tree):
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 10:  #checking if the function length is greater than 10
                    print(f"Function {node.name} is too long at line {node.lineno}") #printing the function name and the line number


if __name__ == '__main__':
    with open('path_to_your_file.py', 'r') as file: #reading the file
        code = file.read()
    analyzer = CodeAnalyzer(code)
    analyzer.run_pylint()
    analyzer.custom_rules_check()
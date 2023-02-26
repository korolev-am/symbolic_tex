import sys
import os
import subprocess
import argparse

class PyCode:

    code_exec = '\\code'
    code_print = '\\codep'
    code_inline = '\\codei'
    code_print_inline = '\\codepi'

    def __init__(self, beg, code_start, end, type_, text):

        self.offset = beg
        self.code_start = code_start - beg      #относительно текста в локальной копии
        self.len = end - beg                    #не включая '}'

        self.type = type_

        self.printable = (type_ == self.code_print) | (type_ == self.code_print_inline)
        self.code = text[beg:end]
        self.code_ori = text[beg:end + 1]

        if self.printable == 1:

            tmp = 'from sympy import latex'

            if tmp not in self.code:
                self.code += '\n' + tmp + '\n'

            self.code += 'print(' + '\n' + 'latex(' + list(filter(None, self.code[self.code_start : self.len].split('\n')))[-1] + '))'


    def get_code(self):

        return self.code[self.code_start :]

    def get_code_ori(self):

        return self.code_ori[self.code_start : self.len]

    def get_section(self):

        return self.code_ori

    def get_end_pos(self):

        return self.offset + self.len

    def get_type(self):

        return self.type


def balance(text):

    s = 1

    for i in range(len(text)):

        if text[i] == '{':

            s += 1

        elif text[i] == '}':

            s -= 1

        if s == 0: 

            return i

    return -1


def find_pycode(text):

    imp = text.find(PyCode.code_exec)

    if text[imp + len(PyCode.code_exec)] == 'p' and text[imp + len(PyCode.code_exec) + 1] == 'i':

        type_ = PyCode.code_print_inline

    elif text[imp + len(PyCode.code_exec)] == 'i':

            type_ = PyCode.code_inline

    elif text[imp + len(PyCode.code_exec)] == 'p':

            type_ = PyCode.code_print

    else:

        type_ = PyCode.code_exec

    beg = text[imp:].find('{') + imp 

    end = balance(text[beg + 1:]) + beg + 1

    return PyCode(imp, beg + 1, end, type_, text) 

def delete_coms_def(text):

    text = text.replace('\\long\\def\\code#1{}', '')
    text = text.replace('\\long\\def\\codep#1{}', '')
    text = text.replace('\\long\\def\\codei#1{}', '')
    text = text.replace('\\long\\def\\codepi#1{}', '')

    return text

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Python to latex parser.')
    parser.add_argument('file', metavar='LatexCode.tex', type=str, help='path to .tex file to be parsed')
    args = parser.parse_args()

    tex_f = args.file

    with open(tex_f) as f:
        text = f.read()

    text = delete_coms_def(text)

    cur_code = []

    size = 0

    output = []

    all_code = ''

    for i in range(text.count(PyCode.code_exec)):

        cur_code.append(find_pycode(text[size:]))

        with open('run_prog.py', 'w') as f:

            f.write(all_code + cur_code[i].get_code())
            f.close()


        res = subprocess.check_output(['python3', 'run_prog.py'], text=True)
        output.append(res)

        all_code += cur_code[i].get_code_ori()
        size += cur_code[i].get_end_pos()
    
    new_text = text

    for i in range(len(output)):

        mode = '$$'

        if 'p' not in cur_code[i].get_type():

            mode = ''

        elif 'i' in cur_code[i].get_type():

            mode = '$'


        new_text = new_text.replace(cur_code[i].get_section(), mode + output[i] + mode)

    new_name = tex_f.replace('.', '_new.')

    with open(new_name, 'w') as f:

        f.write(new_text)
        f.close()

    os.remove('run_prog.py')
    

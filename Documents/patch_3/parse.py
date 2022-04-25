import sys
import os
import subprocess
import argparse
import re
import numpy as np

class PyCode:

    code_exec = '\\code'
    code_print = '\\codep'

    def __init__(self, beg, code_start, end, type_, text):

        self.offset = beg
        self.code_start = code_start - beg      #относительно текста в локальной копии
        self.len = end - beg                    #не включая '}'

        self.type = type_

        self.printable = (type_ == self.code_print)
        self.code = text[beg:end]
        self.code = '\nimport traceback\ntry:\n    exec(\'\'\'\n' + self.code[self.code_start :]
        self.code_ori = text[beg:end + 1]
        self.section = self.code_ori
        self.code_ori = self.code_ori[self.code_start : self.len]
        #print(self.code)
        #print(self.code_ori)
        #print(self.section)

        if self.printable == 1:

            tmp = 'from sympy import latex'

            if tmp not in self.code:
                self.code += '\n' + tmp + '\n'

            self.code += 'print(' + '\'!\',' '\n' + 'latex(' + list(filter(None, self.code.split('\n')))[-2] + '))'

        self.code += '\n\'\'\')'

        self.code += '\nexcept:\n    print(traceback.format_exc())'



    def get_code(self):

        return self.code

    def get_code_ori(self):

        return self.code_ori

    def get_section(self):

        return self.section

    def get_end_pos(self):

        return self.offset + self.len

    def get_type(self):

        return self.type

    def get_line_no(self, n, text, size):

        a = text[:size + self.offset].count('\n')

        return a + n




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

    if text[imp + len(PyCode.code_exec)] == 'p':

            type_ = PyCode.code_print

    else:

        type_ = PyCode.code_exec

    beg = text[imp:].find('{') + imp 

    end = balance(text[beg + 1:]) + beg + 1

    return PyCode(imp, beg + 1, end, type_, text) 

def delete_coms_def(text):

    text = text.replace('\\long\\def\\code#1{}', '')
    text = text.replace('\\long\\def\\codep#1{}', '')

    return text


def check_exec_result(res, text, cur_code, size, file_name):

    if res[0] != '!':           #=> ошибка

        r = res.split()

        #print(res)

        offset = 0

        for i in range(len(r)):

            if r[i] == '\"run_prog.py\",':

                offset = int(r[i + 2].replace(',', ''))

        for i in range(len(r)):

            if r[i] == '\"<string>\",':

                tmp = int(r[i + 2].replace(',', ''))

                line_n = cur_code.get_line_no(tmp - 1, text, size)

                r[i + 2] = str(line_n)

                r[i] = file_name

        #print(''.join(r))

        trb = ''

        sp = ''
        
        j = 0

        for i in res: 

            if i != ' ' and i != '\n' and sp != '':

                if j < len(r):
                    trb += r[j] + sp
                else:
                    trb += sp
                sp = ''
                j += 1

            elif i == ' ' or i == '\n': 

                sp += i

        if j == len(r) - 1:

            trb += r[-1]

        trb = trb.replace('  File \"run_prog.py\", line ' + str(offset) + ', in <module>\n    exec(\'\'\'\n', '')
        print(trb)

        exit(1)

    else:

        return res[2:]

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

        if len(res) != 0:
            res = check_exec_result(res, text, cur_code[i], size, tex_f)

        output.append(res)

        all_code += cur_code[i].get_code_ori()
        size += cur_code[i].get_end_pos()
    
    new_text = text

    for i in range(len(output)):

        new_text = new_text.replace(cur_code[i].get_section(), output[i])

    new_name = tex_f.replace('.', '_new.')

    with open(new_name, 'w') as f:

        f.write(new_text)
        f.close()

    #os.remove('run_prog.py')
    

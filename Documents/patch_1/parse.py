import sys
import os

class PyCode:

    start_w = '\\iffalse'
    end_w = '\\fi'

    def __init__(self, beg, end, code):

        self.beg = beg
        self.end = end

        self.code = code

def find_pycode(text, start_w, end_w):

     beg = text.find(start_w)

     end = text.find(end_w)

     if end == -1 and beg != -1:

        print('no \\fi found')

     return (beg, end)


def find_import(text):

    imp = text.rfind('\\import')

    beg = text[imp:].find('{') + imp 
    end = text[beg + 1:].find('}') + beg + 1          #пусть пока в импортах не будет конструкций со скобочками {}

    return text[beg + 1 : end]



if __name__ == '__main__':
	
    tex_f = sys.argv[1]

    with open(tex_f) as f:
        text = f.read()

    imports = find_import(text)

    all_code = []               #тут будет список со всеми объектами типа PyCode

    beg, end = find_pycode(text, '\\iffalse', '\\fi')

    size = 0

    while (beg != -1 or end != -1):

        cur = PyCode(size + beg, size + end, text[size + beg + len('\\iffalse ') : size + end])

        with open('run_prog.py', 'w') as f:

            f.write(imports + '\n' + cur.code)
            f.close()

        os.system("python3 run_prog.py")

        size += end + len('\\fi')    
        all_code.append(cur)

        beg, end = find_pycode(text[size:], '\\iffalse', '\\fi')

    os.remove('run_prog.py')

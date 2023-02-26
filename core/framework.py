import sympy
import itertools
from sympy import latex
from multipledispatch import dispatch

class TexMathOp(object):
    """basic math ops for symbolic objects"""
    def __init__(self, arg):

        if type(arg) == TexMathOp:
            arg = arg.base_name
        else:
            pass
        
        self.base_name = arg
        import sympy
        self.sym = sympy.symbols(self.base_name)

    def __add__(self, other):

        if type(other) in classes:
            return TexExpr(self.get_val() + other.get_val(), 
                           self.get_str() + other.get_str() + ['+'])
        else:
            return TexExpr(self.get_val() + sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['+'])

    def __pow__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() ** other.get_val(), 
                           self.get_str() + other.get_str() + ['**'])
        else:
            return TexExpr(self.get_val() ** sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['**'])

    def __sub__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() - other.get_val(), 
                           self.get_str() + other.get_str() + ['-'])
        else:
            return TexExpr(self.get_val() + sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['-'])

    def __mul__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() * other.get_val(), 
                           self.get_str() + other.get_str() + ['*'])
        else:
            return TexExpr(self.get_val() * sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['*'])

    def __truediv__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() / other.get_val(), 
                           self.get_str() + other.get_str() + ['/'])
        else:
            return TexExpr(self.get_val() / sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['/'])

    def __floordiv__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() // other.get_val(), 
                           self.get_str() + other.get_str() + ['//'])
        else:
            return TexExpr(self.get_val() // sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['//'])

    def __mod__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() % other.get_val(), 
                           self.get_str() + other.get_str() + ['%'])
        else:
            return TexExpr(self.get_val() % sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['%'])

    def __rshift__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() >> other.get_val(), 
                           self.get_str() + other.get_str() + ['>>'])
        else:
            return TexExpr(self.get_val() >> sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['>>'])

    def __lshift__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() << other.get_val(), 
                           self.get_str() + other.get_str() + ['<<'])
        else:
            return TexExpr(self.get_val() << sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['<<'])

    def __and__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() & other.get_val(), 
                           self.get_str() + other.get_str() + ['&'])
        else:
            return TexExpr(self.get_val() & sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['&'])

    def __or__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() | other.get_val(), 
                           self.get_str() + other.get_str() + ['|'])
        else:
            return TexExpr(self.get_val() | sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['|'])

    def __xor__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() ^ other.get_val(), 
                           self.get_str() + other.get_str() + ['^'])
        else:
            return TexExpr(self.get_val() ^ sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['^'])

    def __lt__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() < other.get_val(), 
                           self.get_str() + other.get_str() + ['<'])
        else:
            return TexExpr(self.get_val() < sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['<'])

    def __le__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() <= other.get_val(), 
                           self.get_str() + other.get_str() + ['<='])
        else:
            return TexExpr(self.get_val() <= sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['<='])

    def __gt__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() > other.get_val(), 
                           self.get_str() + other.get_str() + ['>'])
        else:
            return TexExpr(self.get_val() > sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['>'])

    def __ge__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() >= other.get_val(), 
                           self.get_str() + other.get_str() + ['>='])
        else:
            return TexExpr(self.get_val() >= sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['>='])

    def __eq__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() == other.get_val(), 
                           self.get_str() + other.get_str() + ['=='])
        else:
            return TexExpr(self.get_val() == sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['=='])

    def __ne__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() != other.get_val(), 
                           self.get_str() + other.get_str() + ['!='])
        else:
            return TexExpr(self.get_val() != sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['!='])

    def __neg__(self):
        return TexExpr(-self.get_val(), self.get_str() + ['-u'])

    def __pos__(self):
        return TexExpr(+self.get_val(), self.get_str() + ['+u'])

    def __invert__(self):
        return TexExpr(~self.get_val(), self.get_str() + ['~u'])

class TexSymbol(TexMathOp):
    """
    inheritance from TexMathOp - math ops for symbols
    """

    def hat(self):
        #return sympy.symbols(self.base_name + 'hat')
        #self.base_name += 'hat'
        self.sym = sympy.symbols(self.base_name + 'hat')
        return self

    def check(self):
        self.sym = sympy.symbols(self.base_name + 'check')
        return self

    def tilde(self):
        self.sym = sympy.symbols(self.base_name + 'tilde')
        return self

    def acute(self):
        self.sym = sympy.symbols(self.base_name + 'acute')
        return self

    def grave(self):
        self.sym = sympy.symbols(self.base_name + 'grave')
        return self

    def dot(self):
        self.sym = sympy.symbols(self.base_name + 'dot')
        return self

    def ddot(self):
        self.sym = sympy.symbols(self.base_name + 'ddot')
        return self

    def dddot(self):
        self.sym = sympy.symbols(self.base_name + 'dddot')
        return self

    def ddddot(self):
        self.sym = sympy.symbols(self.base_name + 'ddddot')
        return self

    def breve(self):
        self.sym = sympy.symbols(self.base_name + 'breve')
        return self

    def bar(self):
        self.sym = sympy.symbols(self.base_name + 'bar')
        return self

    def vec(self):
        self.sym = sympy.symbols(self.base_name + 'vec')
        return self

    def get_str(self):
        return [self.base_name]

    def get_val(self):
        return self.sym

    def __repr__(self):
        return self.sym.__repr__()

    def __str__(self):
        return self.sym.__str__()


class TexExpr(TexMathOp):
    """docstring for TexExpr"""
    def __init__(self, arg, str=None):
        #super(TexExpr, self).__init__()

        if type(arg) == str:
            self.expr = sympy.sympify(arg)

        self.expr = arg
        self.polis = str

    def get_str(self):
        return self.polis

    def get_val(self):
        return self.expr

    def __repr__(self):
        return self.expr.__repr__()

    def __str__(self):
        return self.expr.__str__()

class TexNumber(TexMathOp):
    """docstring for TexNumber"""
    def __init__(self, arg):
        #super(TexNumber, self).__init__()

        self.num = sympy.sympify(arg)
        self.str = str(self.num)

    def get_str(self):
        return [self.str]

    def get_val(self):
        return self.num

    def float(self, lim=None):
        if lim == None:
            return float(self.num)
        else:
            return float("{:.2f}".format(self.num, lim=lim))

    def __repr__(self):
        return self.num.__repr__()

    def __str__(self):
        return self.num.__str__()

class TexFraction(TexMathOp):
    """docstring for TexFraction"""
    def __init__(self, arg):
        #super(TexNumber, self).__init__()

        self.num = sympy.sympify(arg)
        self.str = str(self.num)
        self._slash = False

    def get_str(self):
        return [self.str]

    def get_val(self):
        return self.num

    def slash(self):
        """требует подключения \\usepackage{xfrac}"""
        self._slash = True
        return self

    def float(self, lim=None):
        if type(self.num) != sympy.core.numbers.Rational:
            # сделать нормальное сообщение об ошибке
            print('TexFraction.float(): incompatible type, expected Rational, got: ', type(self.num))
            exit(1)
        if lim == None:
            return float(self.num)
        else:
            return float("{:.2f}".format(self.num, lim=lim))

    def line(self):
        self._slash = False
        return self

    def __repr__(self):
        return self.num.__repr__()

    def __str__(self):
        return self.num.__str__()

classes = [TexFraction, TexNumber, TexExpr, TexSymbol]

"""
to do:
для выражений, сделать так: по полису строить само выражение
пока нельзя влиять на вывод latex(TexExpr) (не учитывается например TexFraction.slash())
пока нельзя делать int + TexObject (не определены мат. операции для int и др типов), наоборот можно
наверное, надо сделать класс TexExprStrict(TexExpr), который будет содержать выражение в строгом порядке,
    причем генерить код латеха надо будет вручную скорее всего
"""

@dispatch(object)
def latex(x):
    return sympy.latex(x)

@dispatch(TexSymbol)
def latex(x):
    return sympy.latex(x.sym)

@dispatch(TexExpr)
def latex(x):
    text = sympy.sympify(x.get_val())
    return sympy.latex(text)

@dispatch(TexFraction)
def latex(x):
    text = sympy.latex(x.num)
    if x._slash:
        text = text.replace('\\frac', '\\sfrac')
    return text


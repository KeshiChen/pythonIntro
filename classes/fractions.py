
class Fraction:
    def __init__(self,*args):
        try:
            if len(args) !=2:
                raise ValueError
            if not self._validate(*args):
                raise TypeError
        except ValueError:
            print('Provide exactly two arguments.')
        except TypeError:
            print('Provide an integer and a nonzero integer as arguments.')
        else: # This else is necessary! the pair with try-except-else!
            self._construct(*args)

    def _validate(self,fenzi,fenmu):
        if type(fenzi) is int and type(fenmu) is int:
            if fenmu != 0:
                return True
        else:
            return False
        
    def _construct(self,fenzi,fenmu):
        positive = 1
        if fenzi*fenmu <0:
            positive = -1
        # the most mistakable, when found fenzi,fenmu bigger divisor
        # must pass abs
        self.fenzi = abs(fenzi)
        self.fenmu = abs(fenmu)
        divisor = self.get_both_dividable(abs(fenzi),abs(fenmu))

        if fenzi == 0:
            self.fenmu = 1
            return
        self.fenzi = positive*int(self.fenzi/divisor)
        self.fenmu = int(self.fenmu/divisor)

    # gcd dafa!!!
    # 
    def get_both_dividable(self,x,y):
        if y ==0:
            return x
        else :
            return self.get_both_dividable(y,x%y)

    def __str__(self):
        str_1 = str(self.fenzi)+' / '+str(self.fenmu)
        return str_1

    def __repr__(self):
        str_1 = 'Fraction(numerator = '+str(self.fenzi)+', denominator '+str(self.fenmu)+')'
        return str_1

    def __add__(self,fraction):
        fenmu = self.fenmu*fraction.fenmu
        fenzi_sum = self.fenzi*fraction.fenmu+fraction.fenzi*self.fenmu
        return Fraction(fenzi_sum,fenmu)

    def __sub__(self,fraction):
        fenmu = self.fenmu*fraction.fenmu
        fenzi_difference = self.fenzi*fraction.fenmu-fraction.fenzi*self.fenmu
        return Fraction(fenzi_difference,fenmu)

    def __truediv__(self,fraction):
        try:
            if fraction.fenzi == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print('Cannot divide by 0.')
        else:
            new_fenzi = self.fenzi*fraction.fenmu
            new_fenmu = self.fenmu*fraction.fenzi
            return Fraction(new_fenzi,new_fenmu)

    def __mul__(self,fraction):
        return Fraction(self.fenzi*fraction.fenzi,self.fenmu*fraction.fenmu)

    def __lt__(self,fraction):
        new_fenzi_1 = self.fenzi*fraction.fenmu
        new_fenzi_2 = self.fenmu*fraction.fenzi
        return new_fenzi_1<new_fenzi_2

    def __gt__(self,fraction):
        new_fenzi_1 = self.fenzi*fraction.fenmu
        new_fenzi_2 = self.fenmu*fraction.fenzi
        return new_fenzi_1>new_fenzi_2

    def __ge__(self,fraction):
        new_fenzi_1 = self.fenzi*fraction.fenmu
        new_fenzi_2 = self.fenmu*fraction.fenzi
        return new_fenzi_1>=new_fenzi_2


    def __le__(self,fraction):
        new_fenzi_1 = self.fenzi*fraction.fenmu
        new_fenzi_2 = self.fenmu*fraction.fenzi
        return new_fenzi_1<=new_fenzi_2

    def __eq__(self,fraction):
        if self.fenzi == fraction.fenzi and self.fenmu == fraction.fenmu:
            return True
        return False

    def __nq__(self,fraction):
        if self.fenzi == fraction.fenzi and self.fenmu == fraction.fenmu:
            return False
        return True
    
def gcd(x,y):
        if y ==0:
            return x
        else :
            return gcd(y,y%x)

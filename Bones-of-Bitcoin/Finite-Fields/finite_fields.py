class FiniteFields:
    def __init__(self,num,prime):
        if num>=prime or num<0:
            raise ValueError(f"The given number {num} is not in the range of 0 - {prime-1}")
            
        self.num=num
        self.prime=prime

    def __repr__(self):
        return f'({self.num},{self.prime})'
    def __eq__(self,other):
        if other is None:
            return False
        return self.num==other.num and self.prime==other.prime
    def __ne__(self, other):
        if other is None:
            return True
        return not self.__eq__(other)
    def field_check(self,other):
            if self.prime != other.prime:
                raise TypeError("\nBoth the numbers are in differnt fields. Cannot add two number in differnt fields")
        
    def __add__(self,other):
        self.field_check(other)
        num=(self.num+other.num)%self.prime
        return self.__class__(num,self.prime)
    def __sub__(self,other):
        self.field_check(other)
        num=(self.num-other.num)%self.prime
        return self.__class__(num,self.prime)
    def __mul__(self,other):
        self.field_check(other)
        num=(self.num*other.num)%self.prime
        return self.__class__(num,self.prime)
    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)
    def __truediv__(self,other):
        self.field_check(other)
        inv=other**(self.prime-2)
        num=(self.num*inv.num)%self.prime
        return self.__class__(num,self.prime)


        
def main():
    x,y=map(int,input('Enter the number and the prime of your choosing for the Finite field (seperated by space): ').split())
    field=FiniteFields(x,y)
    print(field)

if __name__=='__main__':
    main()
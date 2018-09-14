class Sieve(object):
    def __init__(self, limit):
        # step 1
        self.seive = [1] * limit
        # step 2
        self.index = 1
    def __next__(self):
        # step 4-5
        self.index += 1
        while self.index < len(self.seive) and not self.seive[self.index]:
            self.index += 1
        # step 6
        if self.index == len(self.seive):
            raise StopIteration
        # step 3
        for i in range(self.index ** 2, len(self.seive), self.index):
            self.seive[i] = 0
        return self.index
    def __iter__(self):
        return self
numero=int(input('Digite um número para teste: '))
print(list(Sieve(numero)))
print('Total de números primos encontrados:',len(list(Sieve(numero))))

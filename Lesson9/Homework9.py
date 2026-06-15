class Romb:
    def __init__(self, storona_a, kut_a):
        self.kut_a = kut_a
        self.storona_a = storona_a

    def __setattr__(self, key, value):
        if key=='kut_a':
            super().__setattr__('kut_b', 180 - value)
        if key =='kut_a' and (value >= 180 or value <= 0):
            raise AttributeError
        if 'kut_a' in self.__dict__:
            if key == 'kut_b' and (value != 180 - self.kut_a):
                raise AttributeError
        if key == 'storona_a' and value <=0:
            raise AttributeError
        super().__setattr__(key, value)

romb1 = Romb(storona_a = 10, kut_a = 120)
print(romb1.storona_a, romb1.kut_a, romb1.kut_b)



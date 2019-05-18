class Bird:
    def fly(self):
        raise NotImplementedError
        # print('run flay method')

class Eagle(Bird):
    pass

e = Eagle()
e.fly()

class Pizza:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    @classmethod
    def margarita(cls):
        return Pizza('Margarita' ,['mozarella', 'tomatos', 'olives'])
    
    @staticmethod
    def calculate_area(radius):
        pi = 3.14
        area = pi*radius**2
        print(area)
        

marg = Pizza.margarita()
print(marg.name)
print(marg.ingredients)
marg.calculate_area(radius=50)

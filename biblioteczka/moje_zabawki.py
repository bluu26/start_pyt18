class Car:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def __str__(self):
        return f"{self.model} {self.marka}"


lst = [
    Car(marka='BMW', model='x3'),
    Car(marka='Audi', model='A4'),
    Car(marka='Mercedes', model='E-Class')
]

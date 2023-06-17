class Chair:
    
    def __init__(self, name):
        self.name = name

    def sit(self):
        pass

class Sofa:
    
    def __init__(self, name):
        self.name = name

    def sit(self):
        pass

class LeatherChair(Chair):
    
    def sit(self):
        print(f"Кожанный стул ({self.name})")

class LeatherSofa(Sofa):
    
    def sit(self):
        print(f"Кожаный диван ({self.name})")

class MetalChair(Chair):
    
    def sit(self):
        print(f"Металический стул ({self.name})")

class MetalSofa(Sofa):
    
    def sit(self):
        print(f"Металический диван ({self.name})")

class FurnitureFactory:
    
    def create_chair(self):
        pass

    def create_sofa(self):
        pass

class LeatherFurnitureFactory(FurnitureFactory):
    
    def create_chair(self, name):
        return LeatherChair(name)

    def create_sofa(self, name):
        return LeatherSofa(name)

class MetalFurnitureFactory(FurnitureFactory):
    
    def create_chair(self, name):
        return MetalChair(name)

    def create_sofa(self, name):
        return MetalSofa(name)


Leather_factory = LeatherFurnitureFactory()
Leather_chair = Leather_factory.create_chair("Стул КожСтрой")
Leather_sofa = Leather_factory.create_sofa("Диван КожСтрой")
Leather_chair.sit()  
Leather_sofa.sit()

Metal_factory = MetalFurnitureFactory()
Metal_chair = Metal_factory.create_chair("Стул матовый, Металическийй")
Metal_sofa = Metal_factory.create_sofa("Диван глянцевый, Металический")
Metal_chair.sit()  
Metal_sofa.sit()
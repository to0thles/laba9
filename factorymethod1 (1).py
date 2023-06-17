class Furniture:
    
    def __init__(self, name):
        self.name = name

    def sit(self):
        pass

class Chair(Furniture):
    
    def sit(self):
        print(f"Стул ({self.name})")

class Sofa(Furniture):
    
    def sit(self):
        print(f"Диван ({self.name})")

class FurnitureFactory:
    
    def create_furniture(self, name):
        pass

class LeatherFurnitureFactory(FurnitureFactory):
    
    def create_furniture(self, name):
        return Chair(name)

class MetalFurnitureFactory(FurnitureFactory):
    
    def create_furniture(self, name):
        return Sofa(name)


leather_factory = LeatherFurnitureFactory()

leather_chair = Leather_factory.create_furniture("Кожанные и металические")

leather_chair.sit()  

metal_factory = MetalFurnitureFactory()

metal_sofa = metal_factory.create_furniture("Кожанные и металические")

metal_sofa.sit()  

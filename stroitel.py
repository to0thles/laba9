class Furniture:
    
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def display_parts(self):
        for part in self.parts:
            print(part)

class FurnitureBuilder:
    
    def build_frame(self):
        pass

    def build_seat(self):
        pass

    def build_rest(self):
        pass

    def get_furniture(self):
        pass

class ChairBuilder(FurnitureBuilder):
    
    def __init__(self):
        self.furniture = Furniture()

    def build_legs(self):
        self.furniture.add_part("Ножки стула")

    def build_seat(self):
        self.furniture.add_part("Сиденье стула")

    def build_rest(self):
        self.furniture.add_part("Спинка стула")

    def get_furniture(self):
        return self.furniture

class SofaBuilder(FurnitureBuilder):
    
    def __init__(self):
        self.furniture = Furniture()

    def build_legs(self):
        self.furniture.add_part("Ножки дивана")

    def build_seat(self):
        self.furniture.add_part("Сидушки дивана")

    def build_rest(self):
        self.furniture.add_part("Спинка дивана")
    def get_furniture(self):
        return self.furniture

class Director:
    
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        
        self.builder.build_legs()
        self.builder.build_seat()
        self.builder.build_rest()
        

        return self.builder.get_furniture()


chair_builder = ChairBuilder()
director = Director(chair_builder)

print ("------Стул------")

chair = director.construct()
chair.display_parts()

sofa_builder = SofaBuilder()
director = Director(sofa_builder)

print ("------Диван------")

sofa = director.construct()
sofa.display_parts()
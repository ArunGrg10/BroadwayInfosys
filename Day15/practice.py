###

class hem():
    def __init__(self,study, height):
        self.study = study
        self.height = height

    def get_details(self):
        return f"his height is {self.height} and studies at {self.study}"

class sudesh(hem):
    def __init__(self, study, height, color, weight):
        super().__init__(study,height)
        self.color = color
        self.weight = weight

    def get_inf(self):
        print(super().get_details())
        return f" the skin color of sudesh is {self.color}. and weight is {self.weight}"



H = sudesh("grade twelve", 3, "brown", 80)

result = H.get_inf()
print(result)


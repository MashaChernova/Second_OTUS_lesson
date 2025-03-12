class Sides :
    def __init__(self,side_lenth):
        self.side_lenth = side_lenth

    @property
    def isCorrectSide(self) :
        if not (isinstance(self.side_lenth,int) or isinstance(self.side_lenth,float)) :
            raise ValueError("Введено не число")
        if self.side_lenth < 0 :
            raise ValueError("Число меньше нуля")
        return self.side_lenth




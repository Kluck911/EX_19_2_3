from app.calculator import Calculator


class Test_Calc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 15, 3) == 5

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 10, 2) == 8

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 3) == 5

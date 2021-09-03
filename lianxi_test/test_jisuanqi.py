from pydemo.jisuanqi import Calculator


class TestCalc:
    def test_add(self):
        calc = Calculator()
        result = calc.add(1, 2)
        assert result == 3

    def test_sub(self):
        sub = Calculator()
        result = sub.sub(3, 1)
        assert result == 2

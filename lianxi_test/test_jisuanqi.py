from pydemo.jisuanqi import Calculator


def test_a():
    print("test case a")


class TestCalc:
    def test_add(self):
        calcs = Calculator()
        result = calcs.add(1, 2)
        assert result == 3

    def test_sub(self):
        subs = Calculator()
        result = subs.sub(3, 1)
        assert result == 2
    def test_chengfa(self):
        chenfas = Calculator()
        result = chenfas.chengfa(2, 5)
        assert result == 10
        return result

    def test_chufa(self):
        chufas = Calculator()
        result = chufas.chufa(10, 5)
        assert result == 2
        return result

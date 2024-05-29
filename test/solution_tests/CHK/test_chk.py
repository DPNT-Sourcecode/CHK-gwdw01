from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("EEEEEEEBBBBBBAAAAAAAAA") == (7 * 40) + 45 + 30 + 200 + 130 + 50
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("ZZYYYXTTSS") == 45*3 + 17


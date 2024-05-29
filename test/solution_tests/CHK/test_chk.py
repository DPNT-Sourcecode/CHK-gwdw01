from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("AAAABBBCD") == (130 + 50 + 45 + 30 + 20 + 15)

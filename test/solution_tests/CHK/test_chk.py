from solutions.CHK import checkout


class TestChk():
    def test_chk(self):
        assert checkout("AAAABBBCD") == (130 + 50 + 45 + 30 + 20 + 15)

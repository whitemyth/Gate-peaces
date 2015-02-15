from lib.gate import Gate


def test_run_returns_zero():
    gate = Gate()
    assert gate.run() == 0


def test_addition():
    assert 1 + 1 == 2

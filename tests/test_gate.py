from lib.gate import Gate

def test_run_returns_zero():
    gate = Gate()
    assert gate.run() == 0

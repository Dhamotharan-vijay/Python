import inc_dec    # The code to test

def test_1():
    assert inc_dec.perfect_number(6) ==6

# This test is designed to fail for demonstration purposes.
def test_2():
    assert inc_dec.decrement(3) == 4
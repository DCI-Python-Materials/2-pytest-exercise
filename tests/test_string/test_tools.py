from text.tools import upper_case, revers

def test_upper_case1():
    assert upper_case("python") == "PYTHON"

# why this test will fail 
def test_upper_case2():
    assert upper_case("lion") == "LOIN"

# why this test will fail ?
# how to fix the function so the test will pass ?
def test_upper_case2():
    assert upper_case() == ""

# why this test will fail?
# how to fix the function so the test will pass?
def test_upper_case2():
    assert upper_case(10) == "10"

def test_revers1():
    assert revers("lion") == "noil"

# why this test will fail?
def test_revers2():
    assert revers("LION") == "noil"
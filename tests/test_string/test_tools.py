from text.tools import upper_case, revers
# test1
def test_upper_case1():
    assert upper_case("python") == "PYTHON"

# test2
def test_upper_case2():
    assert upper_case("lion") == "LOIN"

# test3
def test_upper_case2():
    assert upper_case() == ""

# test4
def test_upper_case2():
    assert upper_case(10) == "10"

# test5
def test_revers1():
    assert revers("lion") == "noil"

# test6
def test_revers2():
    assert revers("LION") == "noil"
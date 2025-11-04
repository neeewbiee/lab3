import lab2.bmi as bmi

def test_bmi_normal_weight():
    height = 1.73
    weight = 24
    test = -1
    result = bmi.calculate_bmi(height, weight)

    assert (result == test)
    
def test_bmi_over_weight():
    height = 1.73
    weight = 64
    test = 0
    result = bmi.calculate_bmi(height, weight)

    assert (result == test)

def test_bmi_under_weight():
    height = 1.73
    weight = 240
    test = 1
    result = bmi.calculate_bmi(height, weight)

    assert (result == test)

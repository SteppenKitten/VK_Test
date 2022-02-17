import pytest

#TUPLE

def if_rgb(pixel):
    if len(pixel) == 3 and type(pixel) == tuple:
        res = all(0 <= i <= 255 for i in pixel)
        return res
    elif type(pixel) != tuple:
        return 'Please, enter a tuple'
    else:
        return False


def test_tuple_1():
    assert if_rgb((255,255,255))
    assert if_rgb((0,0,0))


def test_tuple_2():
    try:
        assert if_rgb(255,255,255)
    except TypeError:
        pass

      
@pytest.mark.parametrize('tuple_input,expected', [((125,125,125), True), ('(255,255,255)', 'Please, enter a tuple'), ((255,255), False)])
def test_tuple_3(tuple_input, expected):
    assert if_rgb(tuple_input) == expected
    
    
#DICTIONARIES

def reverse_elements_dict(dct):
    return {v: k for k, v in dct.items()}

def test_dict_1():
    assert reverse_elements_dict({'VK':1, 'Mail.ru':2}) == {1:'VK', 2:'Mail.ru'}


def test_dict_2():
    try:
        assert reverse_elements_dict(('VK:1', 'Mail.ru:2'))
    except AttributeError:
        pass
        

@pytest.mark.parametrize('dct_input,expected', [({'VK':1, 'Mail.ru':2}, {1:'VK', 2:'Mail.ru'}), ({}, {}), ({1:1, 'Testing':'Testing'}, {1:1, 'Testing':'Testing'})])
def test_dict_3(dct_input, expected):
    assert reverse_elements_dict(dct_input) == expected

from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], -1, "test") == "test"
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([1, 2, 3], 3, "test3") == "test3"
    assert arrs.get([1, 2, 3], 100) is None
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([2, 3, 4]) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], -1) == [4]
    assert arrs.my_slice([1, 2, 3, 4], -4) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], -5) == [1, 2, 3, 4]

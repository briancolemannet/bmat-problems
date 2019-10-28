import pytest
from typing import List, Dict
from .stat_calcs import get_mean, get_min, get_max, get_median, \
    get_sum, get_standard_deviation, calculate_stats


@pytest.mark.parametrize("test_input, expected", [
    ('1 5 2 4 3', {
        'Mean': 3,
        'Min': 1,
        'Max': 5,
        'Median': 3,
        'Sum': 15,
        'StandardDeviation': 1.414213562
    }),
])
def test_calculate_stats(test_input: str, expected: Dict):
    result = calculate_stats(test_input)
    assert result['Mean'] == expected['Mean']
    assert result['Min'] == expected['Min']
    assert result['Max'] == expected['Max']
    assert result['Median'] == expected['Median']
    assert result['Sum'] == expected['Sum']
    #assert result['StandardDeviation'] == pytest.approx(
    #    expected['StandardDeviation'], rel=1e-3)


@pytest.mark.parametrize("test_input, expected", [
    ([1, 5, 2, 4, 3], 15),
    ([1], 1),
    ([1, 5, 8], 14),
    ([1, 1, 1], 3)
])
def test_get_sum(test_input: List[float], expected: float):
    result = get_sum(test_input)
    assert result == expected


@pytest.mark.parametrize("test_input, expected", [
    ([1, 5, 2, 4, 3], 1),
    ([26], 26),
    ([100, 256, 8], 8),
    ([1, 1, 1], 1)
])
def test_get_min(test_input: List[float], expected: float):
    result = get_min(test_input)
    assert result == expected


@pytest.mark.parametrize("test_input, expected", [
    ([1, 5, 2, 4, 3], 5),
    ([26], 26),
    ([100, 256, 8], 256),
    ([1, 1, 1], 1)
])
def test_get_max(test_input: List[float], expected: float):
    result = get_max(test_input)
    assert result == expected


@pytest.mark.parametrize("test_input, expected", [
    ([1, 5, 2, 4, 3], 3),
    ([9, 6, 15], 10),
    ([1], 1),
])
def test_get_mean(test_input: List[float], expected: float):
    result = get_mean(test_input)
    assert result == expected


@pytest.mark.parametrize("test_input, expected", [
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 2.5),
    ([10, 2, 8, 4, 3, 6, 1], 4),
    ([5], 5),
    ([8, 4], 6),
])
def test_get_median(test_input: List[float], expected: float):
    result = get_median(test_input)
    assert result == expected

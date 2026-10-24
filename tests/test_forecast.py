import pytest

from intern.forecast import predict_next_close


def test_flat_prices_predict_same_price():
    assert predict_next_close([10, 10, 10, 10, 10]) == pytest.approx(10)


def test_steady_trend_is_extended_one_step():
    assert predict_next_close([1, 2, 3, 4, 5]) == pytest.approx(6)


def test_only_last_window_prices_are_used():
    assert predict_next_close([100, 1, 2, 3], window=3) == pytest.approx(4)


def test_too_few_prices_raises():
    with pytest.raises(ValueError):
        predict_next_close([1, 2], window=5)


def test_window_below_two_raises():
    with pytest.raises(ValueError):
        predict_next_close([1, 2, 3], window=1)

def predict_next_close(prices, window=5):
    """Estimate the next closing price by extending the recent linear trend.

    Fits a least-squares line through the last `window` prices and
    extrapolates it one step ahead. This is a naive baseline for learning,
    not a reliable forecast: daily prices behave close to a random walk.
    """
    if window < 2:
        raise ValueError("window must be at least 2")
    if len(prices) < window:
        raise ValueError(f"need at least {window} prices, got {len(prices)}")

    recent = list(prices[-window:])
    x_mean = (window - 1) / 2
    y_mean = sum(recent) / window
    slope = sum((x - x_mean) * (y - y_mean) for x, y in enumerate(recent)) / sum(
        (x - x_mean) ** 2 for x in range(window)
    )
    return y_mean + slope * (window - x_mean)

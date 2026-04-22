def validate_input(symbol, side, order_type, quantity, price, stop_price=None):

    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side! Choose BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Invalid order type! Choose MARKET, LIMIT or STOP_LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")

    if order_type == "STOP_LIMIT":
        if price is None or stop_price is None:
            raise ValueError("Both price and stop_price are required for STOP_LIMIT")
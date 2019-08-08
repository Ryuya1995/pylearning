from queue import PriorityQueue
sell_market = {}
buy_market = {}
sell_limit = {}
buy_limit = {}

def execute(order, quantity, price):
    print(order, quantity, price)

def put_order_back(fixed_order, type):
    """
    >>> sell_market["abcd"]= PriorityQueue()
    >>> fixed_order = [1,2,{"side":"buy","symbol:abcd"}]
    >>> type = "sell_market"
    >>> put_order_back(fixed_order, type)
    >>> sell_market["abcd"].get()
    [1,2,{"side":"buy","symbol:abcd"}]
    """
    # sell_market[symbol].put(fixed_order)
    symbol = fixed_order[2]["symbol"]
    eval("{}[symbol].put(fixed_order)".format(type))

def compute_quantity(buy_quantity, sell_quantity, ex_price, type, fixed_order1, type2, fixed_order2=None):
    order1 = fixed_order1[2]
    if fixed_order2 and len(fixed_order2)> 1:
        order2 = fixed_order2[2]
    else:
        order2 = None
    ex_quantity = min(buy_quantity, sell_quantity)
    execute(order1, ex_quantity, ex_price)
    if order2 is not None:
        execute(order1, ex_quantity, ex_price)
    # if "buy" in type:
    #     if buy_quantity > sell_quantity:
    #         order1["quantity"] = buy_quantity - sell_quantity
    #         new_order_matching(order1, type)
    #     elif buy_quantity < sell_quantity:
    #         order2["quantity"] = -buy_quantity + sell_quantity
    #         put_order_back(fixed_order2,type2)
    # elif "sell" in type:
    #     if buy_quantity > sell_quantity:
    #         order2["quantity"] = buy_quantity - sell_quantity
    #         put_order_back(fixed_order2, type2)
    #     elif buy_quantity < sell_quantity:
    #         order1["quantity"] = -buy_quantity + sell_quantity
    #         new_order_matching(order1, type)
    dif_quantity = abs(buy_quantity - sell_quantity)
    if ("buy" in type and buy_quantity > sell_quantity) or ("sell" in type and buy_quantity > sell_quantity):
        order1["quantity"] = dif_quantity
        new_order_matching(order1, type)
    elif dif_quantity > 0:
        fixed_order2[2]["quantity"] = order2["quantity"] - ex_quantity
        put_order_back(fixed_order2, type2)



def get_market_price(symbol, type):
    return 0


def get_price_quantity(order):
    if "price" in order and "quantity" in order:
        return order["price"], order["quantity"]
    else:
        return None, None


def get_ex_price(buy_price, sell_price, symbol):
    if not buy_price:
        if not sell_price:
            ex_price = get_market_price(symbol, "average")
        else:
            ex_price = get_market_price(symbol, "ask")
    else:
        if not sell_price:
            ex_price = buy_price
        elif buy_price >= sell_price:
            ex_price = sell_price
        else:  # put this order back
            return None
    return ex_price


def new_order_matching(fixed_order, type):
    """
    :param fixed_order: [price, index, dict of order information]
    :param type: "buy/sell limit/market"
    :return:
    """
    order = fixed_order[2]
    matched = False
    buy_quantity = sell_quantity = ex_price = type2 = fixed_order2 = None
    symbol = order["symbol"]
    if 'buy' in type:
        buy_price, buy_quantity = get_price_quantity(order)  # the price should be None or "" if it is a market order
        # try to get sell price and quantity from sell_market
        if symbol in sell_market:
            fixed_order2 = sell_market[symbol].get()
            type2 = "sell_market"
            sell_price, sell_quantity = get_price_quantity(fixed_order2[2])
            ex_price = get_ex_price(buy_price, sell_price, symbol)
        # otherwise get sell price and quantity from sell_limit
        elif symbol in sell_limit:
            fixed_order2 = sell_limit[symbol].get()
            type2 = "sell_limit"
            sell_price, sell_quantity = get_price_quantity(fixed_order2[2])
            ex_price = get_ex_price(buy_price, sell_price, symbol)
            if not ex_price:
                sell_limit[symbol][2].put(fixed_order2)

        else:
            sell_price, sell_quantity = None, None

        if sell_quantity and buy_quantity:
            # if we get the sell and buy quantity, then we have two orders, so we can do the check and get the execution price now!
            ex_price = get_ex_price(buy_price, sell_price, symbol)
            if ex_price:
                matched = True
        # if the above matching is failed and the cross is auto, then we do the trade with the market
        if matched == False and order["cross"] == "auto":
            #  get sell price from market
            ex_price = get_market_price(symbol, "ask")
            sell_quantity = None
            fixed_order2 = None
            if ex_price:
                matched = True
    elif "sell" in type:
        sell_price, sell_quantity = get_price_quantity(order)  # the price should be None or "" if it is a market order
        # try to get buy price and quantity from buy_market
        if symbol in buy_market:
            fixed_order2 = buy_market[symbol].get()
            type2 = "buy_market"
            buy_price, buy_quantity = get_price_quantity(fixed_order2[2])
            ex_price = get_ex_price(buy_price, sell_price, symbol)
        # otherwise get buy price and quantity from buy_limit
        elif symbol in buy_limit:
            fixed_order2 = buy_limit[symbol].get()
            type2 = "buy_market"
            buy_price, buy_quantity = get_price_quantity(fixed_order2[2])
            ex_price = get_ex_price(buy_price, sell_price, symbol)
            if not ex_price:
                buy_limit[symbol][2].put(fixed_order2)
        else:
            buy_price, buy_quantity = None, None
        if sell_quantity and buy_quantity:
            # if we get the sell and buy quantity, then we have two orders, and do the check and get the execution price now!
            matched, ex_price = get_ex_price(buy_price, sell_price, symbol)
        if matched == False and order["cross"] == "auto":
            #  get buy price from market
            ex_price = get_market_price(symbol, "ask")
            buy_quantity = None
            fixed_order2 = None
            if ex_price:
                matched = True
    if matched and (buy_quantity or sell_quantity) and ex_price:
        compute_quantity(buy_quantity, sell_quantity, ex_price, type, fixed_order, type2, fixed_order2)
    else:
        put_order_back(fixed_order, type)



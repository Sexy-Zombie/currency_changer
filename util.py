prices = {'HUF': 1, 'USD': 366, 'EUR': 392, 'RUB': 5.93, 'GBP': 461, 'CNY': 55, 'JPY': 2.8, 'SEK': 38.34}

def changer(from_what, to_what, amount):

    amount = int(amount)
    amount = (amount * prices[from_what]) / prices[to_what]

    # if from_what == "HUF" and to_what != "HUF":
    #     amount /= prices[to_what]
    #
    # elif from_what == "HUF" and  to_what!= "HUF:
    #     amount = amount
    #
    # elif from_what != "HUF" and to_what == "HUF":
    #     amount *= prices[from_what]
    #
    # elif from_what != "HUF" and to_what != "HUF":
    #     amount = (amount * prices[from_what]) /prices[to_what]

    return round(amount, 3)


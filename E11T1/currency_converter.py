#!/usr/bin/env python3
# add imports, if necessary
from exchange_rates import EXCHANGE_RATES

def convert(amount, from_currency, to_currency):
    if not isinstance(amount, int) and not isinstance(amount, float):
        raise Warning("not a number")
    if amount < 0:
        raise Warning("Can only convert positive amounts")
    if from_currency not in EXCHANGE_RATES:
        raise Warning("Currency not available")
    if to_currency not in EXCHANGE_RATES:
        raise Warning("Currency not available")
    if from_currency == to_currency:
        return amount
    try:
        return amount * EXCHANGE_RATES[from_currency][to_currency]
    except:
        return amount / EXCHANGE_RATES[to_currency][from_currency]
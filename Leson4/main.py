
class PurchasePcError(Exception):
    def __str__(self):
        return f"Цієї кількості грошей не достатньо для покупки пк!"
def check_money(amount_of_money, limit_Vaule):
    if amount_of_money>limit_Vaule:
        return " Грошей достатньо"
    else:
        raise PurchasePcError(amount_of_money)
money=10
check_money(money, 500)




class PurchaseMonitorError(Exception):
    def __str__(self):
        return f"Цієї кількості грошей не достатньо для покупки монітора!"
def check_money(amount_of_money, limit_Vaule):
    if amount_of_money>limit_Vaule:
        return " Грошей достатньо"
    else:
        raise PurchaseMonitorError(amount_of_money)
money=100
check_money(money, 150)

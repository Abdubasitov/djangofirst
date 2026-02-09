from django.shortcuts import render
from .currency import get_rates

def valuta_page(request):
    rates = get_rates()
    rates["KGS"] = 1.0  # Сом к самому себе

    result = None

    amount = request.GET.get("amount")
    from_currency = request.GET.get("from_currency")
    to_currency = request.GET.get("to_currency")

    if amount and from_currency and to_currency:
        try:
            amount = float(amount)
            # Перевод из выбранной валюты в сомы, потом в целевую валюту
            amount_in_kgs = amount * rates[from_currency]
            result = round(amount_in_kgs / rates[to_currency], 2)
        except (ValueError, KeyError):
            result = "Ошибка ввода"

    context = {
        "usd": rates["USD"],
        "eur": rates["EUR"],
        "rub": rates["RUB"],
        "kzt": rates["KZT"],
        "result": result,
    }

    return render(request, "page/valuta.html", context)

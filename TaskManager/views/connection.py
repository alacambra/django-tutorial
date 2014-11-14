__author__ = 'alacambra'
from django.http import HttpResponse
from django.shortcuts import render


def page(request):

    my_variable = "Hello Connections !"
    years_old = 15
    array_city_capital = ["Paris", "London", "Washington"]

    return render(request, 'en/public/connection.html', {
        "my_var": my_variable, "years": years_old, "array_city": array_city_capital
    })

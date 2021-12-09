from django.shortcuts import render

def home(request):

    return render(request, 'home.html')

def add_value(request):
    num1 = int(request.GET["number1"])
    num2 = int(request.GET["number2"])
    result = num1 + num2
    context = {
        'result' : result,
    }

    return render(request, 'result.html', context)

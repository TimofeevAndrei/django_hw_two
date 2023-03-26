from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def omlet(request):
    servings = int(request.GET['servings'])
    omlet = {}
    for k, i in DATA.items():
        if k == 'omlet':
            if servings > 0:
                omlet_serv = {}
                for key, value in i.items():
                    ser = value * servings
                    print(ser)
                    omlet_serv[key] = ser
                omlet[k] = omlet_serv
            else:
                omlet[k] = i
    context = omlet
    print(context)
    return render(request, 'omlet.html', context)

def pasta(request):
    servings = int(request.GET['servings'])
    pasta = {}
    for k, i in DATA.items():
        if k == 'pasta':
            if servings > 0:
                pasta_serv = {}
                for key, value in i.items():
                    ser = value * servings
                    print(ser)
                    pasta_serv[key] = ser
                pasta[k] = pasta_serv
            else:
                pasta[k] = i
    context = pasta
    print(context)
    return render(request, 'pasta.html', context)

def buter(request):
    servings = int(request.GET['servings'])
    buter = {}
    for k, i in DATA.items():
        if k == 'buter':
            if servings > 0:
                buter_serv = {}
                for key, value in i.items():
                    ser = value * servings
                    print(ser)
                    buter_serv[key] = ser
                buter[k] = buter_serv
            else:
                buter[k] = i
    context = buter
    print(context)
    return render(request, 'buter.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
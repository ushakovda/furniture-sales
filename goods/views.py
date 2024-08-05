from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Home - Каталог",
        "goods": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик и три стула",
                "description": "Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.",
                "price": 150.00,
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "Чайный столик и два стула",
                "description": "Набор из стола и двух стульев в минималистическом стиле.",
                "price": 95.00,
            },
            {
                "image": "deps/images/goods/double bed.jpg",
                "name": "Двухспальная кровать",
                "description": "Двухспальная кровать с изголовьем и ортопедическим матрасом в комплекте.",
                "price": 680.00,
            },
            {
                "image": "deps/images/goods/kitchen table.jpg",
                "name": "Кухонный стол с раковиной",
                "description": "Кухонный стол для обеда с встроенной раковиной и комплектом стильных стульев — идеальное решение для удобного и функционального обеденного пространства.",
                "price": 465.00,
            },
            {
                "image": "deps/images/goods/kitchen table 2.jpg",
                "name": "Кухонный стол с встроенной плитой и раковиной",
                "description": "Изысканный кухонный стол с встроенной плитой и раковиной, оснащённый множеством полок, чтобы каждый элемент вашей кухни был под рукой и выглядел безупречно.",
                "price": 530.00,
            },
            {
                "image": "deps/images/goods/corner sofa.jpg",
                "name": "Угловой диван для гостинной",
                "description": "Элегантный угловой диван, который раскладывается в удобную двухспальную кровать, идеально подойдёт для гостиной и удобного приёма гостей.",
                "price": 720.00,
            },
            {
                "image": "deps/images/goods/bedside table.jpg",
                "name": "Прикроватный столик",
                "description": "Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).",
                "price": 55.00,
            },
            {
                "image": "deps/images/goods/sofa.jpg",
                "name": "Офисный диван",
                "description": "Простой и элегантный офисный диван, который легко дополнит любой интерьер. Идеален для создания комфортабельной зоны отдыха или для неформальных встреч.",
                "price": 190.00,
            },
            {
                "image": "deps/images/goods/office chair.jpg",
                "name": "Офисный стул",
                "description": "Эргономичный офисный стул с простым дизайном, обеспечивающий комфорт и поддержку для вашего рабочего дня.",
                "price": 30.00,
            },
            {
                "image": "deps/images/goods/plants.jpg",
                "name": "Цветок в горшке",
                "description": "Цветок для украшения вашего интерьера подарит свежесть и безмятежность обстановке.",
                "price": 10.00,
            },
            {
                "image": "deps/images/goods/flower.jpg",
                "name": "Цветок стилизированный",
                "description": "Стильный дизайнерский цветок, который придаст вашему интерьеру утончённость и оригинальность. Отличный выбор для яркого декора.",
                "price": 15.00,
            },
            {
                "image": "deps/images/goods/strange table.jpg",
                "name": "Прикроватный столик",
                "description": "Классический прикроватный столик для комфортного доступа к вещам и добавления стиля в вашу спальню.",
                "price": 35.00,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")

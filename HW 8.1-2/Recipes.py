def cook_book():
    with open('recipes.txt', 'rt', encoding='utf8') as file:
        cook_book = {}
        for lines in file:
            list_ingredients_dish = []
            list_ingredients = []
            name_dish = lines
            quantity_ingredients = int(file.readline())
            for ingredients in range(quantity_ingredients):
                list_ingredients_dish.append(file.readline().strip().split('|'))
                for i in list_ingredients_dish:
                    ingredients_dict = dict(zip(['ingredient_name', 'quantity', 'measure'], i))

                list_ingredients.append(ingredients_dict)
            cook_book[name_dish.strip()] = list_ingredients
            file.readline()
        return cook_book

cook_book = cook_book()
#print(f'cook_book = {cook_book}')

def get_shop_list_by_dishes(dishes, person_count):
    my_dict = {}
    shop_dict = {}
    new_list = []
    for x in dishes:
        new_list.append(cook_book[x])

    for shop_list in new_list:
        for ingredient in shop_list:
            product = ingredient['ingredient_name']
            quantity_composition = int(ingredient['quantity']) * person_count
            measure_composition = ingredient['measure']
            if product not in my_dict:
                my_dict[product] = quantity_composition
            else:
                my_dict[product] += int(quantity_composition)
            comp = dict(zip(['quantity', 'measure'], [my_dict[product], measure_composition]))
            shop_dict[product] = comp
    print('Новый запрос:')
    for key, value in shop_dict.items():
        print(key, value)
    print()

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
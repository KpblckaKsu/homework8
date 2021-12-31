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
    for dish, composition in cook_book.items():
        if dish in dishes:
            for ingr in composition:
                composition_key = ingr['ingredient_name']
                quantity_composition = int(ingr['quantity']) * person_count
                measure_composition = ingr['measure']
                comp = dict(zip(['quantity', 'measure'], [quantity_composition, measure_composition]))
                my_dict[ingr['ingredient_name']] = comp
    print(len(my_dict))
    print(my_dict)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

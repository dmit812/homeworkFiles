from pprint import pprint


def get_cookbook(recipes):
    with open(recipes, 'r', encoding='utf8') as file:
        cook_book = {}
        for line in file:
            name_dish = line.strip()
            cook_book[name_dish] = []
            ingredients_count = file.readline()
            for ing in range(int(ingredients_count)):
                ingredients_name = file.readline()
                ingredient_name, quantity, measure = ingredients_name.split(' | ')
                ingredients_list = {"ingredient_name": ingredient_name,
                                    "quantity": int(quantity),
                                    "measure": measure.strip()}
                cook_book[name_dish].append(ingredients_list)
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    ingredients_dict = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            measure_qty = {"measure": ing["measure"], "quantity": int(ing["quantity"]) * person_count}
            if ing["ingredient_name"] not in ingredients_dict:
                ingredients_dict[ing["ingredient_name"]] = measure_qty
            else:
                ingredients_dict[ing["ingredient_name"]]["quantity"] += measure_qty["quantity"]
    return ingredients_dict


def unification_files(file1, file2, file3):
    count_line = []
    for file in (file1, file2, file3):
        name = file
        with open(file, encoding='utf8') as files:
            file_lines = files.readlines()
            count_line.append([name, file_lines])
    count_line.sort(key=lambda x: len(x[1]))
    with open('new_file.txt', 'w', encoding='utf8') as fw:
        for file in count_line:
            res = f'{file[0]}\n{len(file[1])}\n{"".join(file[1])}\n'
            fw.writelines(res)
    with open('new_file.txt', 'r', encoding='utf8') as result:
        text = result.read()
        print(text)


print(f'{"*" * 10} Задание №1 {"*" * 10}\n')
pprint(get_cookbook('recipes.txt'), indent=2, width=160)
print(f'{"*" * 10} Задание №2 {"*" * 10}\n')
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3, get_cookbook('recipes.txt')), indent=2, width=160)
print(f'{"*" * 10} Задание №3 {"*" * 10}\n')
unification_files('1.txt', '2.txt', '3.txt')

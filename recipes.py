
def recipes():

    with open('recipes.txt', 'r', encoding="utf-8") as file:
        cook_book = {}
        new_recip_full = []
        for line in file:
            product_name = line.strip()
            line_quantity = int(file.readline().strip())
            cook_book[product_name] = []
            for item in range(line_quantity):
                new_recip = {}
                values = file.readline().strip()
                new_recip['ingredient_name'] = values.split("|")[0]
                new_recip['quantity'] = values.split("|")[1]
                new_recip['measure'] = values.split("|")[-1]
                cook_book[product_name].append(new_recip)
            file.readline()



    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = recipes()
    for dish in dishes:
        if dish in cook_book:
            for item in cook_book[dish]:
                new_quantity = item['quantity']
                new_quantity_calc = int(new_quantity) * person_count
                item['quantity'] = new_quantity_calc
                print(item)


# print(recipes())
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 5)






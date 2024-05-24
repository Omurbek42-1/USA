# Предположим, что у вас уже есть база данных магазинов и продуктов
# Здесь я просто создам пример базы данных в виде словарей

shops = {
    1: "Asia",
    2: "Globus",
    3: "Spar"
}

products = {
    1: {"name": "Chocolate", "category": "Food products", "price": 10.5, "quantity": 129},
    2: {"name": "Milk", "category": "Dairy", "price": 2.5, "quantity": 80},
    3: {"name": "Bread", "category": "Bakery", "price": 1.2, "quantity": 200},
    # Добавьте больше продуктов по вашему усмотрению
}

# Функция для отображения списка магазинов
def display_shops():
    print("Список магазинов:")
    for id, shop in shops.items():
        print(f"{id}. {shop}")

# Функция для отображения информации о продуктах в выбранном магазине
def display_products(shop_id):
    shop_name = shops.get(shop_id)
    if shop_name:
        print(f"Продукты в магазине {shop_name}:")
        for prod_id, product in products.items():
            if product.get("shop_id") == shop_id:
                print(f"Название продукта: {product['name']}")
                print(f"Категория: {product['category']}")
                print(f"Цена: {product['price']}")
                print(f"Количество на складе: {product['quantity']}")
    else:
        print("Магазин с данным id не найден.")

# Основная программа
def main():
    print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    display_shops()
    while True:
        choice = input("Введите id магазина (или 0 для выхода): ")
        if choice == '0':
            print("Выход из программы...")
            break
        elif choice.isdigit():
            shop_id = int(choice)
            if shop_id in shops:
                display_products(shop_id)
            else:
                print("Магазин с данным id не найден.")
        else:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()
    

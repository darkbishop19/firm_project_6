import tkinter as tk
import sqlite3
from tkinter import messagebox, ttk


def add_client():
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    # Получаем данные из вводных полей
    client_name = str(client_name_entry.get())
    print(client_name)
    if client_name:
        cursor.execute("INSERT INTO clients (client_name) VALUES (?)", (client_name,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Успех", f"Вы добавили клиента под именем: {client_name}")
        # Очищаем вводные поля
        client_name_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Ошибка", f"Вы не ввели имя")


def update_client_name():
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    # Получаем данные из вводных полей
    client_id = int(client_id_entry.get())
    client_new_name = str(client_n_entry.get())

    # Обновляем данные о комплектующем в базе данных
    if client_id:
        cursor.execute("UPDATE clients SET client_name=? WHERE client_id=?", (client_id, client_new_name))
        conn.commit()
        conn.close()
        # Очищаем вводные поля
        client_id_entry.delete(0, tk.END)
        client_n_entry.delete(0, tk.END)
        messagebox.showinfo("Успех", f"Вы обновили имя клиента {client_id}: {client_new_name}")
    else:
        messagebox.showinfo("Ошибка", f"Не удалось обновить имя клиента, видимо вы ошиблись в id")


def view_clients():
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    # Получаем данные о комплектующих из базы данных

    cursor.execute("SELECT * FROM clients")
    components = cursor.fetchall()
    conn.close()

    # Очищаем предыдущий вывод
    output.delete('1.0', tk.END)

    if len(components) == 0:
        output.insert(tk.END, "Нет клиентов")
    # Выводим данные о комплектующих
    for component in components:
        client_id, client_name = component
        output.insert(tk.END, f"ID: {client_id}, Имя клиента: {client_name}\n")


def delete_client():
    output.delete('1.0', tk.END)
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    # Получаем данные из вводных полей
    client_id = int(client_id_entry.get())

    # Удаляем комплектующий из базы данных

    cursor.execute("DELETE FROM clients WHERE client_id=?", (client_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", f"Вы удалили клиента {client_id}")
    # Очищаем вводные поля
    client_id_entry.delete(0, tk.END)
def delete_wholesaler_item():
    output.delete('1.0', tk.END)
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    # Получаем данные из вводных полей
    wholesaler_id = int(wholesaler_id_entry.get())

    # Удаляем комплектующий из базы данных

    cursor.execute("DELETE FROM wholesaler_components WHERE id=?", (wholesaler_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", f"Вы удалили оптовый товар: {wholesaler_id}")
    # Очищаем вводные поля
    client_id_entry.delete(0, tk.END)

def create_order():
    client = client_combobox.get()
    print(client[0])
    client_id = int(client[0])
    computer_id = int(computer_combobox.get())
    print(computer_id)
    date = str(date_entry.get())
    print(date)
    selected_payment = int(payment_var.get())
    print(selected_payment)

    if client_id and computer_id and date and (selected_payment == 1 or selected_payment == 0):
        conn = sqlite3.connect('computer_store.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT total_price FROM computers where id={computer_id}")
        common_price = cursor.fetchone()[0]
        price = float(common_price)
        cursor.execute("INSERT INTO orders (client_id, computer_id, completion_date, price,  paid) VALUES (?,?,?,?,?)",
                       (client_id, computer_id, date, price, selected_payment))
        conn.commit()
        conn.close()
        messagebox.showinfo("Успех", f"Вы успешно разместили заказ")
    else:
        messagebox.showinfo("Ошибка", f"Вы не ввели имя")


def create_computer():
    processor = str(processor_combobox.get())
    processor_id = int(processor[0])
    processor_info, processor_price_info = processor.split("} ")
    processor_price = float(processor_price_info)

    videocard = str(videocard_combobox.get())
    videocard_id = int(videocard[0])
    videocard_info, videocard_price_info = videocard.split("} ")
    videocard_price = float(videocard_price_info)

    ssd = str(ssd_combobox.get())
    ssd_id = int(ssd[0])
    ssd_info, ssd_price_info = ssd.split("} ")
    ssd_price = float(ssd_price_info)

    memory = str(memory_combobox.get())
    memory_id = int(memory[0])
    memory_info, memory_price_info = memory.split("} ")
    memory_price = float(memory_price_info)

    component_ids = [processor_id, videocard_id, ssd_id, memory_id]
    total_price = processor_price + videocard_price + ssd_price + memory_price
    print(component_ids)
    print(f"price:{total_price}")
    if processor and videocard and ssd and memory:
        conn = sqlite3.connect('computer_store.db')
        cursor = conn.cursor()
        component_ids_str = ",".join(str(id) for id in component_ids)
        print(component_ids_str)
        cursor.execute("INSERT INTO computers (component_ids, total_price) VALUES (?, ?)",
                       (component_ids_str, total_price))
        conn.commit()
        conn.close()
        messagebox.showinfo("Успех", f"Вы успешно добавили компьютер")
        # Очищаем вводные поля
        client_name_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Ошибка", f"Вы не ввели имя")


def view_computers():
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT *FROM computers")
    components = cursor.fetchall()
    conn.close()

    output.delete('1.0', tk.END)

    if len(components) == 0:
        output.insert(tk.END, "Нету готовых моделей ПК")
        # Выводим данные о комплектующих
    for component in components:
        computer_id, component_ids, price = component
        output.insert(tk.END, f"ID: {computer_id}, Component ids: {component_ids}, Retail Price: {price}\n")


def view_orders():
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    components = cursor.fetchall()
    conn.close()

    output.delete('1.0', tk.END)

    if len(components) == 0:
        output.insert(tk.END, "Нету готовых моделей ПК")
        # Выводим данные о комплектующих
    for component in components:
        order_id, client_id, computer_id, completion_date, price, paid = component
        output.insert(tk.END,
                      f"ID: {order_id}, ID клиента: {client_id}, ID компьютера: {computer_id}, Стоимость: {price}, Статус оплаты: {paid}\n")


def view_wholesaler_items():
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM wholesaler_components")
    components = cursor.fetchall()
    conn.close()
    output.delete('1.0', tk.END)

    if len(components) == 0:
        output.insert(tk.END, "Нету оптовых цен")
        # Выводим данные о комплектующих
    for component in components:
        order_id, component_name, wholesaler_price, wholesaler_info = component
        output.insert(tk.END,
                      f"ID: {order_id}, название: {wholesaler_price}, цена: {wholesaler_price}, информация о поставщике: {wholesaler_info}")


def view_order():
    output.delete('1.0', tk.END)

    computer = processor_2_combobox.get()
    completion_date = data_2_combobox.get()
    price = price_2_combobox.get()
    processor_2_combobox.set('')
    data_2_combobox.set('')
    price_2_combobox.set('')
    if computer:
        conn = sqlite3.connect('computer_store.db')
        cursor = conn.cursor()
        computer_id = int(computer[0])
        print(computer_id)
        cursor.execute(f"SELECT * FROM orders WHERE computer_id={computer_id}")
        components = cursor.fetchall()
        conn.close()
        print(components)
        for component in components:
            order_id, client_id, computer_id, completion_date, price, paid = component
            output.insert(tk.END,
                          f"ID: {order_id}, ID клиента: {client_id}, ID компьютера: {computer_id}, Стоимость: {price}, Статус оплаты: {paid}\n")

        return
    if completion_date:
        conn = sqlite3.connect('computer_store.db')
        cursor = conn.cursor()
        date = completion_date
        print(date)
        cursor.execute(f"SELECT * FROM orders WHERE completion_date= ?", (date,))
        components = cursor.fetchall()
        conn.close()
        print(components)
        for component in components:
            order_id, client_id, computer_id, completion_date, price, paid = component
            output.insert(tk.END,
                          f"ID: {order_id}, ID клиента: {client_id}, ID компьютера: {computer_id}, Стоимость: {price}, Статус оплаты: {paid}\n")

        return
    if price:
        conn = sqlite3.connect('computer_store.db')
        cursor = conn.cursor()
        pricing = float(price)
        print(pricing)
        cursor.execute(f"SELECT * FROM orders WHERE price={pricing}")
        components = cursor.fetchall()
        conn.close()
        print(components)
        for component in components:
            order_id, client_id, computer_id, completion_date, price, paid = component
            output.insert(tk.END,
                          f"ID: {order_id}, ID клиента: {client_id}, ID компьютера: {computer_id}, Стоимость: {price}, Статус оплаты: {paid}\n")

        return


def add_wholesaler_item():
    item_name = component_id_combobox.get()
    price = float(component_wholesaler_entry.get())
    info = name_wholesaler_entry.get()
    if item_name and price and info:
        conn = sqlite3.connect('computer_store.db')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO wholesaler_components (component_name,wholesaler_price,  wholesaler_info) VALUES (?,?,?)",
            (item_name, price, info))
        conn.commit()
        conn.close()
        messagebox.showinfo("Успех", f"Вы успешно добавили оптовый товар")
        # Очищаем вводные поля
        client_name_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Ошибка", f"Вы  не добавил оптовый товар")


root = tk.Tk()
root.title("Computer Store Manager Backend")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)
# root.rowconfigure(2, weight=1)
# root.rowconfigure(3, weight=1)
# root.rowconfigure(4, weight=1)
# root.rowconfigure(5, weight=1)
# root.rowconfigure(6, weight=1)
# root.rowconfigure(7, weight=1)
# root.rowconfigure(8, weight=1)
# root.rowconfigure(9, weight=1)

client_name_label = tk.Label(root, text="Имя клиента:")
client_name_label.grid(row=0, column=0, padx=5, pady=5)
client_name_entry = tk.Entry(root)
client_name_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

add_client_button = tk.Button(root, text="Добавить нового клиента", command=add_client)
add_client_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

client_id_label = tk.Label(root, text="ID клиента:")
client_id_label.grid(row=2, column=0, padx=5, pady=5)
client_id_entry = tk.Entry(root)
client_id_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="ew")
client_n_label = tk.Label(root, text="Новое имя клиента:")
client_n_label.grid(row=3, column=0, padx=5, pady=5)
client_n_entry = tk.Entry(root)
client_n_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky="ew")
update_client_button = tk.Button(root, text="Обновить имя клиента", command=update_client_name)
update_client_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

delete_clients_button = tk.Button(root, text="Удалить клиента по ID", command=delete_client)
delete_clients_button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

view_clients_button = tk.Button(root, text="Показать всех клиентов", command=view_clients)
view_clients_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

# список пользователей
client_id_label = tk.Label(root, text="Клиент:")
client_id_label.grid(row=6, column=0, padx=5, pady=5)
client_combobox = ttk.Combobox(root, state="readonly")
client_combobox.grid(row=6, column=1, padx=5, pady=5, sticky="ew")
conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM clients")
clients = cursor.fetchall()
client_combobox['values'] = clients
conn.close()

# список компьютеров
computer_id_label = tk.Label(root, text="Компьютер:")
computer_id_label.grid(row=7, column=0, padx=5, pady=5)
computer_combobox = ttk.Combobox(root, state="readonly")
computer_combobox.grid(row=7, column=1, padx=5, pady=5, sticky="ew")
conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()
cursor.execute("SELECT id FROM computers")
computers = cursor.fetchall()
computer_combobox['values'] = computers
conn.close()

date_label = tk.Label(root, text="Дата конца сборки:")
date_label.grid(row=8, column=0, padx=5, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=8, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

processor_id_label = tk.Label(root, text="Процессор:")
processor_id_label.grid(row=11, column=0, padx=5, pady=5)
processor_combobox = ttk.Combobox(root, state="readonly")
processor_combobox.grid(row=11, column=1, padx=5, pady=5, sticky="ew")
conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM client_components WHERE component_name LIKE 'Процессор%' ")
computers = cursor.fetchall()
processor_combobox['values'] = computers
conn.close()

videocard_id_label = tk.Label(root, text="Видеокарта:")
videocard_id_label.grid(row=12, column=0, padx=5, pady=5)
videocard_combobox = ttk.Combobox(root, state="readonly")
videocard_combobox.grid(row=12, column=1, padx=5, pady=5, sticky="ew")
conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM client_components WHERE component_name LIKE 'Видеокарта%' ")
computers = cursor.fetchall()
videocard_combobox['values'] = computers
conn.close()

ssd_id_label = tk.Label(root, text="SSD:")
ssd_id_label.grid(row=13, column=0, padx=5, pady=5)
ssd_combobox = ttk.Combobox(root, state="readonly")
ssd_combobox.grid(row=13, column=1, padx=5, pady=5, sticky="ew")
conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM client_components WHERE component_name LIKE 'SSD%' ")
computers = cursor.fetchall()
ssd_combobox['values'] = computers
conn.close()

memory_id_label = tk.Label(root, text="Видео-память:")
memory_id_label.grid(row=14, column=0, padx=5, pady=5)
memory_combobox = ttk.Combobox(root, state="readonly")
memory_combobox.grid(row=14, column=1, padx=5, pady=5, sticky="ew")
conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM client_components WHERE component_name LIKE 'Видео-память%' ")
computers = cursor.fetchall()
memory_combobox['values'] = computers
conn.close()

processor_label_2 = tk.Label(root, text="Компьютер:")
processor_label_2.grid(row=16, column=0, padx=5, pady=5)
processor_2_combobox = ttk.Combobox(root, state="readonly")
processor_2_combobox.grid(row=16, column=1, padx=5, pady=5, sticky="ew")
conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()
cursor.execute(f"SELECT computer_id FROM orders")
computers = cursor.fetchall()
processor_2_combobox['values'] = computers
conn.close()

data_label_2 = tk.Label(root, text="Дата:")
data_label_2.grid(row=17, column=0, padx=5, pady=5)
data_2_combobox = ttk.Combobox(root, state="readonly")
data_2_combobox.grid(row=17, column=1, padx=5, pady=5, sticky="ew")
conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()
cursor.execute("SELECT completion_date FROM orders")
computers = cursor.fetchall()
data_2_combobox['values'] = computers
conn.close()

price_label_2 = tk.Label(root, text="Цены:")
price_label_2.grid(row=18, column=0, padx=5, pady=5)
price_2_combobox = ttk.Combobox(root, state="readonly")
price_2_combobox.grid(row=18, column=1, padx=5, pady=5, sticky="ew")
conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()
cursor.execute("SELECT price FROM orders")
computers = cursor.fetchall()
price_2_combobox['values'] = computers
conn.close()

component_id_3 = tk.Label(root, text="Компонент:")
component_id_3.grid(row=20, column=0, padx=5, pady=5)
component_id_combobox = ttk.Combobox(root, state="readonly")
component_id_combobox.grid(row=20, column=1, padx=5, pady=5, sticky="ew")
conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()
cursor.execute("SELECT component_name FROM client_components")
computers = cursor.fetchall()
component_id_combobox['values'] = computers
conn.close()

component_wholesaler_label = tk.Label(root, text="Стоимость оптовика:")
component_wholesaler_label.grid(row=21, column=0, padx=5, pady=5)
component_wholesaler_entry = tk.Entry(root)
component_wholesaler_entry.grid(row=21, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

name_wholesaler_label = tk.Label(root, text="Название поставщика:")
name_wholesaler_label.grid(row=22, column=0, padx=5, pady=5)
name_wholesaler_entry = tk.Entry(root)
name_wholesaler_entry.grid(row=22, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

wholesaler_id_label = tk.Label(root, text="ID оптового товара: ")
wholesaler_id_label.grid(row=25, column=0, padx=5, pady=5)
wholesaler_id_entry = tk.Entry(root)
wholesaler_id_entry.grid(row=25, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

def update_database_for_order():
    # клиенты
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    client_combobox['values'] = clients
    conn.close()
    # компьютеры
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM computers")
    computers = cursor.fetchall()
    computer_combobox['values'] = computers
    conn.close()

    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT computer_id FROM orders")
    computers = cursor.fetchall()
    processor_2_combobox['values'] = computers
    conn.close()

    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT completion_date FROM orders")
    computers = cursor.fetchall()
    data_2_combobox['values'] = computers
    conn.close()

    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM orders")
    computers = cursor.fetchall()
    price_2_combobox['values'] = computers
    conn.close()


payment_var = tk.IntVar()

# Создаем радиокнопки для опции "Оплачено" и "Не оплачено"
paid_radiobutton = tk.Radiobutton(root, text="Оплачено", variable=payment_var, value=1)
unpaid_radiobutton = tk.Radiobutton(root, text="Не оплачено", variable=payment_var, value=0)

# Устанавливаем значения по умолчанию
payment_var.set(0)  # Не оплачено

# Размещаем радиокнопки на форме
paid_radiobutton.grid(row=9, column=0, padx=5, pady=5, sticky="w")
unpaid_radiobutton.grid(row=9, column=1, padx=5, pady=5, sticky="w")

create_order_button = tk.Button(root, text="Добавить заказ", command=create_order)
create_order_button.grid(row=10, column=0, padx=5, pady=5, sticky="nsew")

update_order_button = tk.Button(root, text="Обновить информацию из БД", command=update_database_for_order)
update_order_button.grid(row=10, column=1, padx=5, pady=5, sticky="nsew")

view_computer_button = tk.Button(root, text="Посмотреть компьютеры", command=view_computers)
view_computer_button.grid(row=15, column=0, padx=5, pady=5, sticky="nsew")

add_computer_button = tk.Button(root, text="Добавить кастомный компьютер", command=create_computer)
add_computer_button.grid(row=15, column=1, padx=5, pady=5, sticky="nsew")

view_orders_button = tk.Button(root, text="Посмотреть все заказы", command=view_orders)
view_orders_button.grid(row=19, column=1, padx=5, pady=5, sticky="nsew")

view_order_button = tk.Button(root, text="Посмотреть заказ по параметру", command=view_order)
view_order_button.grid(row=19, column=0, padx=5, pady=5, sticky="nsew")

wholesaler_button = tk.Button(root, text="Добавить товар с оптовыми ценами", command=add_wholesaler_item)
wholesaler_button.grid(row=23, column=0, padx=5, columnspan=4, pady=5, sticky="nsew")

wholesaler_view_all_button = tk.Button(root, text="Посмотреть все товары c оптовыми ценами", command=view_wholesaler_items)
wholesaler_view_all_button.grid(row=24, column=0, padx=5, columnspan=4, pady=5, sticky="nsew")

wholesaler_delete_button = tk.Button(root, text="Удалить оптовый товар", command=delete_wholesaler_item)
wholesaler_delete_button.grid(row=26, column=0, padx=5, columnspan=4, pady=5, sticky="nsew")

output = tk.Text(root, height=10, width=40)
output.grid(row=40, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

root.mainloop()

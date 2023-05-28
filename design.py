import tkinter as tk
import sqlite3


def update_component():
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    # Получаем данные из вводных полей
    component_id = int(component_id_entry.get())
    retail_price = float(retail_price_entry.get())

    # Обновляем данные о комплектующем в базе данных

    cursor.execute("UPDATE client_components SET retail_price=? WHERE id=?", (retail_price, component_id))
    conn.commit()
    conn.close()

    # Очищаем вводные поля
    component_id_entry.delete(0, tk.END)
    retail_price_entry.delete(0, tk.END)

    # Обновляем список комплектующих
    view_components()

def add_component():
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    # Получаем данные из вводных полей
    component_name = component_name_entry.get()
    retail_price = float(retail_price_entry.get())
    cursor.execute("INSERT INTO client_components (component_name, retail_price) VALUES (?, ?)", (component_name, retail_price))
    conn.commit()
    conn.close()

    # Очищаем вводные поля
    component_name_entry.delete(0, tk.END)
    retail_price_entry.delete(0, tk.END)

    # Обновляем список комплектующих
    view_components()

def delete_component():
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    # Получаем данные из вводных полей
    component_id = int(component_id_entry.get())

    # Удаляем комплектующий из базы данных

    cursor.execute("DELETE FROM client_components WHERE id=?", (component_id,))
    conn.commit()
    conn.close()

    # Очищаем вводные поля
    component_id_entry.delete(0, tk.END)

    # Обновляем список комплектующих
    view_components()

def view_components():
    conn = sqlite3.connect('computer_store.db')
    cursor = conn.cursor()
    # Получаем данные о комплектующих из базы данных

    cursor.execute("SELECT * FROM client_components")
    components = cursor.fetchall()
    conn.close()

    # Очищаем предыдущий вывод
    output.delete('1.0', tk.END)

    if len(components) == 0:
        output.insert(tk.END, "Нет комплектующих")
    # Выводим данные о комплектующих
    for component in components:
        component_id, component_name, retail_price = component
        output.insert(tk.END, f"ID: {component_id}, Component: {component_name}, Retail Price: {retail_price}\n")

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
# Создаем графический интерфейс
root = tk.Tk()
root.title("Computer Store Manager Frontend")

# Раскладка сетки
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.rowconfigure(8, weight=1)
root.rowconfigure(9, weight=1)

# Метки и поля ввода для обновления комплектующего
component_id_label = tk.Label(root, text="Component ID:")
component_id_label.grid(row=0, column=0, padx=5, pady=5)
component_id_entry = tk.Entry(root)
component_id_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

retail_price_label = tk.Label(root, text="Retail Price:")
retail_price_label.grid(row=1, column=0, padx=5, pady=5)
retail_price_entry = tk.Entry(root)
retail_price_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

update_button = tk.Button(root, text="Update Component", command=update_component)
update_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

# Метки и поля ввода для добавления комплектующего
component_name_label = tk.Label(root, text="Component Name:")
component_name_label.grid(row=3, column=0, padx=5, pady=5)
component_name_entry = tk.Entry(root)
component_name_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

retail_price_label = tk.Label(root, text="Retail Price:")
retail_price_label.grid(row=4, column=0, padx=5, pady=5)
retail_price_entry = tk.Entry(root)
retail_price_entry.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

add_button = tk.Button(root, text="Add Component", command=add_component)
add_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

# Метки и поля ввода для удаления комплектующего
component_id_label = tk.Label(root, text="Component ID:")
component_id_label.grid(row=6, column=0, padx=5, pady=5)
component_id_entry = tk.Entry(root)
component_id_entry.grid(row=6, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

delete_button = tk.Button(root, text="Delete Component", command=delete_component)
delete_button.grid(row=7, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

# Кнопка и поле вывода для просмотра комплектующих
view_components_button = tk.Button(root, text="View Components", command=view_components)
view_components_button.grid(row=8, column=0, padx=5, pady=5, sticky="nsew")


view_computers_button = tk.Button(root, text="View Computers", command=view_computers)
view_computers_button.grid(row=8, column=1, padx=5, pady=5, sticky="nsew")


output = tk.Text(root, height=10, width=40)
output.grid(row=9, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

root.mainloop()


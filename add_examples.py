import sqlite3

conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()


def add_compononets_retail():
    cursor.execute("INSERT INTO client_components (component_name, retail_price) VALUES (?, ?)",
                   ("Процессор AMD A1", 15000))
    cursor.execute("INSERT INTO client_components (component_name, retail_price) VALUES (?, ?)",
                   ("Видео-память HyperX A1", 2000))
    cursor.execute("INSERT INTO client_components (component_name, retail_price) VALUES (?, ?)",
                   ("Видеокарта Nvidia 3060", 25000))
    cursor.execute("INSERT INTO client_components (component_name, retail_price) VALUES (?, ?)",
                   ("SSD WB BLUE 1 TB", 3000))
    cursor.execute("INSERT INTO client_components (component_name, retail_price) VALUES (?, ?)",
                   ("Процессор AMD A2", 20000))
    cursor.execute("INSERT INTO client_components (component_name, retail_price) VALUES (?, ?)",
                   ("Видео-память HyperX A2", 4000))
    cursor.execute("INSERT INTO client_components (component_name, retail_price) VALUES (?, ?)",
                   ("Видеокарта Nvidia 3070", 35000))
    cursor.execute("INSERT INTO client_components (component_name, retail_price) VALUES (?, ?)",
                   ("SSD WB BLUE 2 TB", 5000))


def add_computers():
    component_ids = [5,6,7,8]
    pc_price = cursor.execute("SELECT SUM(retail_price) FROM client_components WHERE id IN (?, ?, ?, ?)",
                              component_ids).fetchone()[0]
    component_ids_str = ",".join(str(id) for id in component_ids)
    cursor.execute("INSERT INTO computers (id, component_ids, total_price) VALUES (?, ?, ?)",
                   (2, component_ids_str, pc_price))


add_computers()
conn.commit()
conn.close()

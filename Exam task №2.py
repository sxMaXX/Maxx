import sqlite3

con = sqlite3.connect('base13.db')
cursor = con.cursor()

#cursor.execute('''create table Телефонный_справочник(nomber integer, name text, surname text);''')

for i in range(3):
    x = int(input("Введите номер телефона: "))
    y = input("Введите имя: ")
    z = input("Введите фамилию: ")
    cursor.execute("""insert into Телефонный_справочник values (?, ?, ?);""", (x, y, z))

con.commit()
con.close()

#Создать таблицу SQL с тремя колонками. Заполнить ее тремя записями.

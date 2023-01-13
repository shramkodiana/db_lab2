import psycopg2
import numpy as np
import matplotlib.pyplot as plt
username = 'shramko'
database = 'lab2'
host = 'localhost'
password = '111'
port = '5432'
query1 = '''
SELECT species.dino_species AS species, COUNT(dinosaur.species_id) FROM dinosaur
JOIN species ON species.species_id = dinosaur.species_id
GROUP BY dino_species
'''
query2 = '''
SELECT diet.dino_diet AS diet, COUNT(dinosaur.diet_id) FROM dinosaur 
JOIN diet ON diet.diet_id = dinosaur.diet_id
GROUP BY dino_diet
'''

query3 = '''
SELECT dino_name, length_in_meters FROM dinosaur
ORDER BY length_in_meters DESC
'''
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))
x = []
y = []
with conn:
    cur = conn.cursor()
    cur.execute(query1)


    figure, (bar_ax) = plt.subplots(1)
    plt.bar(x, y, width=0.6, alpha=0.6, color='blue')
    plt.ylabel('Кількість особин')
    plt.title('Кількість особин кожного виду')


    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.bar(x, y, width=0.6, alpha=0.6, color='blue')
    plt.ylabel('Кількість особин')
    plt.title('Кількість особин кожного виду')
    plt.show()

    x.clear()
    y.clear()
    cur.execute(query2)
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.pie(y, labels=x, shadow=True, autopct='%1.1f%%', startangle=180)
    plt.title('Частка способів харчування')
    plt.show()

    x.clear()
    y.clear()
    cur.execute(query3)
    for row in cur:
        y.append(row[1])
        x.append(row[0])
    plt.plot(x, y, 'go-')
    plt.ylabel('Зріст')
    plt.xlabel('Назви динозаврів')
    plt.title('Показники зросту динозаврів')
    for x, y in zip(x, y):
        plt.annotate(y, xy=(x, y), xytext=(7, 2), textcoords='offset points')
    plt.show()

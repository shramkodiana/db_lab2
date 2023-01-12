import psycopg2

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

with conn:

    print ("\nDatabase opened successfully\n")
    cur = conn.cursor()

    print('1. Кількість особин кожного виду\n')
    cur.execute(query1)
    for row in cur:
        print(row)

    print('\n2. Відношення способів харчування\n')
    cur.execute(query2)
    for row in cur:
        print(row)

    print('\n3. Показник зросту у різних динозаврів\n')
    cur.execute(query3)
    for row in cur:
        print(row)


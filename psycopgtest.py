import psycopg2
import requests

# url = "https://jsonplaceholder.typicode.com/todos"
url = "https://jsonplaceholder.typicode.com/users"
myToken = 'Bearercec6ded42e0b5ca314a44678ff81a1a5'
myUrl = 'https://ows.goszakup.gov.kz/v2/refs/ref_months'
head = {'Authorization': 'access_token cec6ded42e0b5ca314a44678ff81a1a5'}
r = requests.get(myUrl, headers={'Authorization': 'Bearer cec6ded42e0b5ca314a44678ff81a1a5'})
data = r.json()
print(data)

# con = psycopg2.connect(
#     host="localhost",
#     database="testpgsql",
#     user="postgres",
#     password="1")
# cur = con.cursor()
# for i in data:
#     cur.execute("insert into userstest (name, email) values (%s, %s)", (i['name'], i['email']))
# con.commit()
# con.close()




# userID = data["id"]
# title = data["title"]
# con = psycopg2.connect(
#     host = "localhost",
#     database = "testpgsql",
#     user = "postgres",
#     password = "1")
#
# cur = con.cursor()
# cur.execute("insert into mytodos (id, title) values (%s, %s)", ([13, 14, 15], ['asd', 'dsa', 'wsa']))
# con.commit()
# con.close()
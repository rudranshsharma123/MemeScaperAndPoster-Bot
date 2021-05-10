import psycopg2
import numpy
import functools
import operator
#Using Pyscop2 to connect to an existing Cockroach DB node. Removed all the variables due to privacy. Howeevr, you can add yours and it should work well. 
conn = psycopg2.connect(
    database='your db name',
    user='your username',
    password='your passwordd',
    sslmode='require',
    port=26257,
    host='free-tier.gcp-us-central1.cockroachlabs.cloud',
    options="--cluster=your cluster name"
)

class cockroachDB():
    def __init__(self, conn):
        self.conn = conn
    
    def create_table(self):
        '''
        It creates the table we would be storing all our data on 
        '''
        
        print("CREATING TABLE>>>>>>>>")
        with self.conn.cursor() as cur:
             cur.execute(
            """CREATE TABLE IF NOT EXISTS Memes.tested (post_id VARCHAR(255), 
            post_urls VARCHAR(255)
            );"""
        )
        conn.commit()
        print("TABLE IS CREATED>>>>>>")
        return True

    def add_values(self, values:list[list]):
        '''
        It is used to add the values which you pass into the database. Make sure that you have the values as list of lists. i.e [[ALL VALUES OF TYPE 1 TO BE ADDED], [ALL VALUES OF TYPE 2 TO BE ADDED], .......]
        '''
        print(len(values), print(len(values[0])) )
        print(values)
        varlist = [[i[j] for i in values] for j in range(len(values[0]))]
        print(varlist) 
        print("ADDING YOUR VALUES INTO THE TABLE >>>>>>>")
        # print(len(values, len(values[0])))
        # values =functools.reduce(operator.iconcat, values, [])
        # varlist = list(numpy.reshape(values, (5, 10)))
        # varlist = [[i[j] for i in values] for j in range(len(values[0]))]
        # varlist = values
        with self.conn.cursor() as cur:
            # varlist = list(values)
            for ind, value in enumerate(varlist):
                j = "'"
                query_string = "UPSERT INTO Memes.tested VALUES (%s);" %", ".join([ j + i + j for i in value]) #had to do this shenanigan because SQL would'nt take the normal python string?
                cur.execute(query_string)
            conn.commit()
        print("YOU VALUES ARE ADDED INTO THE TABLE>>>>>")
        return True
    
    def get_values(self, printing:bool):
        '''
        it is used to get all the values which is stored in the table
        '''
        
        print("GETTING THE VALUES FROM THE TABLE >>>>>>>")
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM Memes.tested")
            rows = cur.fetchall()
            db = []
            for row in rows:
                db.append([str(cell) for cell in row])
                if printing:
                    print([str(cell) for cell in row])
        print("FOUND THE VALUES IN THE TABLE >>>>>>")
        
        return db
    
            




# conn.connect()
# add_values()
# print_balances()
# with conn.cursor() as cur:
#     cur.execute(
#             """CREATE TABLE IF NOT EXISTS Memes.testing (post_id INT PRIMARY KEY, 
#             post_urls VARCHAR(255), 
#             post_title VARCHAR(255),
#             post_description VARCHAR(255),
#             post_time VARCHAR(255), 
#             post_score INT
#             );"""
#         )
#     cur.execute("""UPSERT INTO Memes.testing VALUES (1, 'sdds', 'ssss', 'ppppp', 'kkkkk', 10);""")
#     

# # conn.commit()
# cock = cockroachDB(conn = conn)
# cock.create_table()
# x = [["1", "2", "3", "4", "5", "6"], ['7', '8', '9', '10', '11', '12'], ['13', '14', '15', '16', '17', '18'],['13', '14', '15', '16', '17', '18'],['13', '14', '15', '16', '17', '18'],['13', '14', '15', '16', '17', '18'],['13', '14', '15', '16', '17', '18'],['13', '14', '15', '16', '17', '18'],['13', '14', '15', '16', '17', '18'],['13', '14', '15', '16', '17', '18']]
# print(len(x), len(x[0]))
# cock.add_values(x)
# print(cock.get_values(printing = True))

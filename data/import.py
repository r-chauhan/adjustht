import csv, sqlite3

DB_FILE = 'data/dataset-sl.db'
DS_FILE = 'data/dataset.csv'

con = sqlite3.connect(DB_FILE)
cur = con.cursor()
cur.execute("DROP TABLE adjdata;")
cur.execute("CREATE TABLE adjdata (date,channel,country,os,impressions,clicks,installs,spend,revenue);") 

with open(DS_FILE,'r') as fin: 
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['date'], i['channel'], i['country'], i['os'], i['impressions'], i['clicks'], i['installs'], i['spend'], i['revenue']) for i in dr]

cur.executemany("INSERT INTO adjdata (date,channel,country,os,impressions,clicks,installs,spend,revenue) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()


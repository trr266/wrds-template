import wrds
db = wrds.Connection()
#db.create_pgpass_file()

libraries = db.list_libraries()
libraries[:4]

tables = db.list_tables('wrdssec')
tables[:4]

col_headers = db.describe_table(library="wrdssec", table="wrds_nlpsa")
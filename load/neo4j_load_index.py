""" Neo4J database loader for the Tycho-2 dataset index. Each region has the following properties:

    1. TYC1      <--- GSC (Guide Star Catalog) Region
    2. RAmin     <--- Smallest RA within Region
    3. RAmax     <--- Largest RA within Region
    4. DEmin     <--- Smallest DEC within Region
    5. DEmax     <--- Largest DEC within Region

Usage: python3 neo4j_load_index.py [uri] [username] [password] [index]
"""
from neo4j.v1 import GraphDatabase
from sys import argv


if __name__ == '__main__':
    # We need to be passed the URI, username, password, and location of the index.
    if len(argv) != 5:
        print('Usage: python3 neo4j_load.py [uri] [username] [password] [index]')
        exit(1)

    # Connect to the database, and start a session.
    driver = GraphDatabase.driver(argv[1], auth=(argv[2], argv[3]))
    session = driver.session()

    # Load our file. We are going to read line by line (ughghghghghghhggh).
    with open(argv[4], 'r') as c_f:
        for i, entry in enumerate(c_f):
            try:
                node = {
                    'RAmin': float(entry[15:21]),
                    'RAmax': float(entry[22:28]),
                    'DEmin': float(entry[29:35]),
                    'DEmax': float(entry[36:42])
                }

                session.run('MATCH (a:Region {' +
                            'TYC1: {}'.format(i + 1) +
                            '}) SET ' +
                            'a.RAmin = {}, '.format(node['RAmin']) +
                            'a.RAmax = {}, '.format(node['RAmax']) +
                            'a.DEmin = {}, '.format(node['DEmin']) +
                            'a.DEmax = {}'.format(node['DEmax']))

            except ValueError as e:
                print(str(e))
                pass

    session.close(), driver.close()

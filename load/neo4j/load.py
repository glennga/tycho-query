""" Neo4J database loader for the Tycho-2 dataset. Each node has the following properties:

    1. TYC2      <--- GSC Running Number
    2. TYC3      <--- GSC Component Identifier
    3. RAmdeg    <--- Mean Right Ascension
    4. DEmdeg    <--- Mean Declination
    5. BTmag    <--- Magnitude

Each region (as of now) has the following property:

    1. TYC1      <--- GSC Region Number

Usage: python3 load.py [uri] [username] [password] [catalog]
"""
from neo4j.v1 import GraphDatabase
from sys import argv


if __name__ == '__main__':
    # We need to be passed the URI, username, password, and location of the catalog.
    if len(argv) != 5:
        print('Usage: python3 load.py [uri] [username] [password] [catalog]')
        exit(1)

    # Connect to the database, and start a session.
    driver = GraphDatabase.driver(argv[1], auth=(argv[2], argv[3]))
    session = driver.session()

    # Load our file. We are going to read line by line (ughghghghghghhggh).
    with open(argv[4], 'r') as c_f:
        for entry in c_f:
            try:
                node = {
                    'TYC1': int(entry[:4]),
                    'TYC2': int(entry[6:10]),
                    'TYC3': int(entry[11]),
                    'RAmdeg': float(entry[15:27]),
                    'DEmdeg': float(entry[28:40]),
                    'BTmag': float(entry[110:116]),
                }

                if node['BTmag'] < 11.0:
                    session.run('CREATE (s:Star {' +
                                'TYC1: {}, '.format(node['TYC1']) +
                                'TYC2: {}, '.format(node['TYC2']) +
                                'TYC3: {}, '.format(node['TYC3']) +
                                'RAmdeg: {}, '.format(node['RAmdeg']) +
                                'DEmdeg: {}, '.format(node['DEmdeg']) +
                                'BTmag: {}'.format(node['BTmag']) +
                                '})')
                    session.run('MERGE (a:Region { ' +
                                'TYC1: {}'.format(node['TYC1']) +
                                '})')
                    session.run('MATCH (s:Star), (a:Region) WHERE ' +
                                's.TYC1 = {} AND '.format(node['TYC1']) +
                                's.TYC2 = {} AND '.format(node['TYC2']) +
                                's.TYC3 = {} AND '.format(node['TYC3']) +
                                'a.TYC1 = {} '.format(node['TYC1']) +
                                'CREATE (a)-[:CONTAINS]->(s)')

            except ValueError as e:
                pass

    session.close(), driver.close()

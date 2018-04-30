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

# Chunk size of each transaction.
CHUNK_SIZE = 10000

if __name__ == '__main__':
    # We need to be passed the URI, username, password, and location of the catalog.
    if len(argv) != 5:
        print('Usage: python3 load.py [uri] [username] [password] [catalog]')
        exit(1)

    # Connect to the database, and start a session.
    driver = GraphDatabase.driver(argv[1], auth=(argv[2], argv[3]))
    session = driver.session()

    # Create our indices.
    session.run('CREATE INDEX ON :Star(TYC1, TYC2, TYC3)')
    session.run('CREATE INDEX ON :Region(TYC1)')

    # Commit counter, and the start of the first transaction.
    tx = session.begin_transaction()
    commit_i = 0

    # Load our file. We are going to read line by line (ughghghghghghhggh).
    with open(argv[4], 'r') as c_f:
        for entry in c_f:
            try:
                if commit_i >= CHUNK_SIZE:
                    tx.commit()
                    tx, commit_i = session.begin_transaction(), 0

                node = {
                    'TYC1': int(entry[:4]),
                    'TYC2': int(entry[6:10]),
                    'TYC3': int(entry[11]),
                    'RAmdeg': float(entry[15:27]),
                    'DEmdeg': float(entry[28:40]),
                    'BTmag': float(entry[110:116]),
                }

                if node['BTmag'] < 12.0:
                    tx.run("""
                        CREATE (s:Star {
                            TYC1: {TYC1}, 
                            TYC2: {TYC2},
                            TYC3: {TYC3},
                            RAmdeg: {RAmdeg},
                            DEmdeg: {DEmdeg},
                            BTmag: {BTmag}
                        })""", node)
                    tx.run("""
                        MERGE (a:Region {
                            TYC1: {TYC1}
                        })""", node)
                    tx.run("""
                        MATCH (s:Star), (a:Region) WHERE
                            s.TYC1 = {TYC1} AND
                            s.TYC2 = {TYC2} AND
                            s.TYC3 = {TYC3} AND
                            a.TYC1 = {TYC1}
                        CREATE (a)-[:CONTAINS]->(s)""", node)
                    commit_i = commit_i + 1

            except ValueError as e:
                pass

    session.close(), driver.close(), tx.commit()

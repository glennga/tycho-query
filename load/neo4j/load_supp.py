""" Neo4J database loader for the Tycho-2 supplement dataset. Each node has the following properties:

    1. TYC2      <--- GSC Running Number
    2. TYC3      <--- GSC Component Identifier
    3. RAmdeg    <--- Mean Right Ascension
    4. DEmdeg    <--- Mean Declination
    5. pmRA      <--- Proper Motion Right Ascension
    6. pmDE      <--- Proper Motion Declination
    7. e_RAmdeg  <--- Mean Right Ascension Standard Error
    8. e_DEmdeg  <--- Mean Declination Standard Error
    9. e_pmRA    <--- Proper Motion Right Ascension Standard Error
    10. e_pmDE   <--- Proper Motion Declination Standard Error
    11. BTmag    <--- Magnitude
    12. e_BTmag  <--- Magnitude Standard Error

Each region (as of now) has the following property:

    1. TYC1      <--- GSC Region Number

Usage: python3 load_supp.py [uri] [username] [password] [catalog]
"""
from neo4j.v1 import GraphDatabase
from sys import argv


if __name__ == '__main__':
    # We need to be passed the URI, username, password, and location of the catalog.
    if len(argv) != 5:
        print('Usage: python3 load_supp.py [uri] [username] [password] [catalog]')
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
                    'pmRA': float(entry[42:48]),
                    'pmDE': float(entry[50:56]),
                    'e_RAmdeg': float(entry[57:62]),
                    'e_DEmdeg': float(entry[63:68]),
                    'e_pmRA': float(entry[69:74]),
                    'e_pmDE': float(entry[75:80]),
                    'BTmag': float(entry[83:89]),
                    'e_BTmag': float(entry[90:95]),
                }

                if node['BTmag'] < 10.0:
                    session.run('CREATE (s:Star {' +
                                'TYC1: {}, '.format(node['TYC1']) +
                                'TYC2: {}, '.format(node['TYC2']) +
                                'TYC3: {}, '.format(node['TYC3']) +
                                'RAmdeg: {}, '.format(node['RAmdeg']) +
                                'DEmdeg: {}, '.format(node['DEmdeg']) +
                                'pmRA: {}, '.format(node['pmRA']) +
                                'pmDE: {}, '.format(node['pmDE']) +
                                'e_RAmdeg: {}, '.format(node['e_RAmdeg']) +
                                'e_DEmdeg: {}, '.format(node['e_DEmdeg']) +
                                'e_pmRA: {}, '.format(node['e_pmRA']) +
                                'e_pmDE: {}, '.format(node['e_pmDE']) +
                                'BTmag: {}, '.format(node['BTmag']) +
                                'e_BTmag: {}'.format(node['e_BTmag']) +
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

""" Neo4J query executor (and timer). CQL files must contain valid syntax, and queries must be separated by a newline.

Usage: python3 query.py [uri] [username] [password] [cql-file] [index-file]
"""

from neo4j.v1 import GraphDatabase
from timeit import timeit
from time import sleep
from sys import argv


def lookup_tyc(ra, dec, index_file):
    """ Given some point in space, search the index file for the matching GSC region.

    :param ra: Right ascension to search for.
    :param dec: Declination to search for.
    :param index_file: Index file to search
    :return: The matching TYC1 number if one exists. Otherwise, -1.
    """
    with open(index_file, 'r') as i_f:
        for i, entry in enumerate(i_f):
            try:
                node = {
                    'RAmin': float(entry[15:21]),
                    'RAmax': float(entry[22:28]),
                    'DEmin': float(entry[29:35]),
                    'DEmax': float(entry[36:42])
                }
                if node['RAmin'] < ra < node['RAmax'] and node['DEmin'] < dec < node['DEmax']:
                    return i

            except ValueError:
                pass

    # If no matching TYC is found, return -1.
    return -1


def print_run(q):
    """ Given a query, run and display the result.

    :param q: Query to execute.
    :return: None.
    """
    if q.find('?') != -1:
        # If desired, search the index file for the TYC1.
        ra, dec = [float(x) for x in q.split('?')[1].split()]
        tyc1 = lookup_tyc(ra, dec, argv[5])
        q = q.split('?')[0] + str(tyc1) + q.split('?')[2]

    # print('Result: ' + ','.join([str(x) for x in session.run(q)]))
    session.run(q)


if __name__ == '__main__':
    # We need to be passed the URI, username, password, and location of the query file.
    if len(argv) != 6:
        print('Usage: python3 query.py [uri] [username] [password] [cql-file] [index-file]')
        exit(1)

    # Connect to the database, and start a session. Enable logging.
    driver = GraphDatabase.driver(argv[1], auth=(argv[2], argv[3]))
    session = driver.session()
    # watch("neo4j.bolt", DEBUG, stdout)

    # Load our file into memory, do not read our comments.
    queries = []
    with open(argv[4], 'r') as cql_f:
        for line in cql_f:
            queries.append(line.strip()) if line.strip() and not line.startswith('//') else None

    # Run our queries 15 times.
    for i in range(15):
        for j, q in enumerate(queries):
            print('Running Time [Query {}, Run {}]: {}'.format(j, i, timeit(stmt=lambda: print_run(q), number=1)))
            sleep(0.25)

    session.close(), driver.close()

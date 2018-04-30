""" Neo4J query executor (and timer). CQL files must contain valid syntax, and queries must be separated by a newline.

Usage: python3 query.py [uri] [username] [password] [cql-file]
"""

from neo4j.v1 import GraphDatabase
from numpy import average, std
from timeit import timeit
from sys import argv


def print_run(q):
    """ Given a query, run and display the result.

    :param q: Query to execute.
    :return: None.
    """
    print('Result: ' + ','.join([str(x) for x in session.run(q)]))
    # session.run(q)


if __name__ == '__main__':
    # We need to be passed the URI, username, password, and location of the query file.
    if len(argv) != 5:
        print('Usage: python3 query.py [uri] [username] [password] [cql-file]')
        exit(1)

    # Connect to the database, and start a session. Enable logging.
    driver = GraphDatabase.driver(argv[1], auth=(argv[2], argv[3]))
    session = driver.session()
    # watch("neo4j.bolt", DEBUG, stdout)

    # Load our file into memory, do not read our comments.
    queries, r_t = [], []
    with open(argv[4], 'r') as cql_f:
        for line in cql_f:
            queries.append(line.strip()) if line.strip() and not line.startswith('//') else None

    # Run our queries 15 times.
    for i in range(15):
        r_t.append(timeit(stmt=lambda: [print_run(q) for q in queries], number=1))
        print('Running Time [{}]: {}s'.format(i, r_t[-1]))

    # Print some statistics of our times.
    print('Running Time [mu]: {}s'.format(average(r_t)))
    print('Running Time [sigma]: {}s'.format(std(r_t)))

    session.close(), driver.close()

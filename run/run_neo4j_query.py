""" Neo4J query executor (and timer). CQL files must contain valid syntax, and queries must be separated by a newline.

Usage: python3 run_neo4j_query.py [uri] [username] [password] [cql-file]
"""

from neo4j.v1 import GraphDatabase
from timeit import timeit
from sys import argv


if __name__ == '__main__':
    # We need to be passed the URI, username, password, and location of the query file.
    if len(argv) != 5:
        print('Usage: python3 run_neo4j_query.py [uri] [username] [password] [cql-file]')
        exit(1)

    # Connect to the database, and start a session.
    driver = GraphDatabase.driver(argv[1], auth=(argv[2], argv[3]))
    session = driver.session()

    # Load our file into memory, do not read our comments.
    queries = []
    with open(argv[4], 'r') as cql_f:
        for line in cql_f:
            queries.append(line) if not line.startswith('//') else None

    # Run our query once.
    print('Running Time (1st): {}s'.format(timeit(stmt=lambda: [session.run(q) for q in queries], number=1)))

    # Run our query set 10 times.
    print('Running Time (10): {}s'.format(timeit(stmt=lambda: [session.run(q) for q in queries], number=10)))

    session.close(), driver.close()

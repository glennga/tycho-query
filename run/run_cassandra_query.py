""" Cassandra query executor (and timer). CQL files must contain valid syntax, queries must be separated by a
 newline, and the number of queries per set must be specified. If n > 1, the result of

Usage: python3 run_cassandra_query.py [uri] [cql-file] [n]
"""

from cassandra.cluster import Cluster
from timeit import timeit
from sys import argv


def hash_c(v):
    """ Round some value v to the closest multiple of 2.49, and return the appropriate multiplier of 2.49 to get this
    number.

    :param v: Celestial value to hash (alpha or delta).
    :return: The new, hashed value.
    """
    from math import ceil
    return ceil((v + (2.49 - v) % v if v != 0 else 0) / 2.49)


def execute_query_sets(q):
    """ Given a sequence of queries, execute them and feed the result of the former into the latter.

    :param q: Query sequence to execute.
    :return: None.
    """
    previous = []

    for q_i in q:
        # Custom function (not CQL), compute the hash for the following values.
        if q_i.split()[0] == 'COMPUTE' and q_i.split()[1] == 'HASH':
            ra, dec = q_i.split()[2], q_i.split()[3]
            previous = [hash_c(ra), hash_c(dec)]

        else:
            # Otherwise, execute the query. Pass the previous result if desired.
            if q_i.find('{') and q_i.find('}'):
                previous = session.execute(q_i.format(p=previous))
            else:
                previous = session.execute(q_i)


if __name__ == '__main__':
    # We need to be passed the URI, the location of the query file, and the number of subqueries.
    if len(argv) != 4:
        print('Usage: python3 run_cassandra_query.py [uri] [cql-file] [n]')
        exit(1)

    # Connect to the database, and start a session.
    cluster = Cluster([argv[1]])
    session = cluster.connect()
    session.set_keyspace('tycho')

    # Load our file into memory, do not read our comments.
    queries, q_t, n_c = [], [], 0
    with open(argv[2], 'r') as cql_f:
        for line in cql_f:

            # Flush our buffer q_t when we have a complete subquery set.
            if n_c < int(argv[3]):
                n_c = (n_c + 1) if not line.startswith(';') else n_c
                q_t.append(line) if not line.startswith(';') else None
            else:
                queries.append(q_t)
                n_c = (n_c + 1) if not line.startswith(';') else n_c
                q_t = [line] if not line.startswith(';') else q_t

    # Run our query once.
    print('Running Time (1st): {}s'.format(timeit(stmt=lambda: [execute_query_sets(q) for q in queries], number=1)))

    # Run our query set 10 times.
    print('Running Time (10): {}s'.format(timeit(stmt=lambda: [execute_query_sets(q) for q in queries], number=10)))

""" Cassandra query executor (and timer). CQL files must contain valid syntax, queries must be separated by a
 newline, and the number of queries per set must be specified.

Usage: python3 query.py [uri] [cql-file] [index-file] [n]
"""

from cassandra.cluster import Cluster
from numpy import average, std
from timeit import timeit
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
            previous = [lookup_tyc(ra, dec, argv[3])]

        else:
            # Otherwise, execute the query. Pass the previous result if desired.
            if q_i.find('{') and q_i.find('}'):
                previous = session.execute(q_i.format(p=previous))
            else:
                previous = session.execute(q_i)
            print('Result: {}'.format(previous))


if __name__ == '__main__':
    # We need to be passed the URI, the location of the query file, and the number of subqueries.
    if len(argv) != 4:
        print('Usage: python3 query.py [uri] [cql-file] [index-file] [n]')
        exit(1)

    # Connect to the database, and start a session.
    cluster = Cluster([argv[1]])
    session = cluster.connect()
    session.set_keyspace('tycho')

    # Load our file into memory, do not read our comments.
    queries, q_t, r_t, n_c = [], [], [], 0
    with open(argv[2], 'r') as cql_f:
        for line in cql_f:

            # Flush our buffer q_t when we have a complete subquery set.
            if n_c < int(argv[4]):
                n_c = (n_c + 1) if not line.startswith(';') else n_c
                q_t.append(line) if not line.startswith(';') else None
            else:
                queries.append(q_t)
                n_c = (n_c + 1) if not line.startswith(';') else n_c
                q_t = [line] if not line.startswith(';') else q_t

    # Run our queries 15 times.
    for i in range(15):
        r_t.append(timeit(stmt=lambda: [execute_query_sets(q) for q in queries], number=1))
        print('Running Time [{}]: {}s'.format(i, r_t[-1]))

    # Print some statistics of our times.
    print('Running Time [mu]: {}s'.format(average(r_t)))
    print('Running Time [sigma]: {}s'.format(std(r_t)))

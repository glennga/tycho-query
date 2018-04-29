""" Cassandra database loader for the Tycho-2 dataset index. Each region has the following columns:

    1. TYC1      <--- GSC (Guide Star Catalog) Region
    2. RAmin     <--- Smallest RA within Region
    3. RAmax     <--- Largest RA within Region
    4. DEmin     <--- Smallest DEC within Region
    5. DEmax     <--- Largest DEC within Region

Usage: python3 load_index.py [uri] [index]
"""
from cassandra.cluster import Cluster
from sys import argv


if __name__ == '__main__':
    # We need to be passed the URI and location of the catalog.
    if len(argv) != 3:
        print('Usage: python3 load_index.py [uri] [catalog]')
        exit(1)

    # Connect to the database, and start a session.
    cluster = Cluster([argv[1]])
    session = cluster.connect()

    # Create our Tycho keyspace.
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 
            'class': 'SimpleStrategy', 
            'replication_factor' : '3' 
        } """ % "tycho")

    # Create the Region table.
    session.set_keyspace('tycho')
    session.execute("""
        CREATE TABLE IF NOT EXISTS tycho.region (
            TYC1 int,
            RAmin float,
            RAmax float,
            DEmin float,
            DEmax float,
            InRegion set<frozen <list<int>>>,
            PRIMARY KEY (TYC1)
        ) """)

    # Our prepared statement. Execute for each region.
    p = session.prepare("""
        INSERT INTO tycho.region (
            TYC1, RAmin, RAmax, DEmin, DEmax
        ) VALUES (?, ?, ?, ?, ?) """)
    # p.consistency_level = ConsistencyLevel.ALL

    # Load our file. We are going to read line by line (ughghghghghghhggh).
    with open(argv[2], 'r') as c_f:
        for i, entry in enumerate(c_f):
            try:
                node = {
                    'RAmin': float(entry[15:21]),
                    'RAmax': float(entry[22:28]),
                    'DEmin': float(entry[29:35]),
                    'DEmax': float(entry[36:42])
                }

                session.execute(p.bind((i + 1, node['RAmin'], node['RAmax'], node['DEmin'], node['DEmax'])))

            except ValueError as e:
                pass

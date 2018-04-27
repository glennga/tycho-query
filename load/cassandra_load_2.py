""" Cassandra database loader for the Tycho-2 dataset. Each table has the following properties:

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
    11. EpRAm    <--- Mean Epoch Right Ascension
    12. EpDEm    <--- Mean Epoch Declination
    13. BTmag    <--- Magnitude
    14. e_BTmag  <--- Magnitude Standard Error

Usage: python3 cassandra_load.py [uri] [catalog]
"""
from cassandra.cluster import Cluster
from sys import argv

def hash_c(v):
    """ Round some value v to the closest multiple of 2.5, and return the appropriate multiplier of 2.5 to get this
    number.

    :param v: Celestial value to hash (alpha or delta).
    :return: The new, hashed value.
    """
    from math import ceil
    return ceil((v + (2.5 - v) % v if v != 0 else 0) / 2.5)


if __name__ == '__main__':
    # We need to be passed the URI and location of the catalog.
    if len(argv) != 3:
        print('Usage: python3 cassandra_load.py [uri] [catalog]')
        exit(1)

    # Connect to the database, and start a session.
    cluster = Cluster([argv[1]])
    session = cluster.connect()

    # Create the Stars table.
    session.set_keyspace('tycho')
    session.execute("""
        CREATE TABLE IF NOT EXISTS tycho.stars (
            TYC1 int,
            TYC2 int,
            TYC3 int,
            RAmdeg float,
            DEmdeg float,
            pmRA float,
            pmDE float,
            e_RAmdeg float,
            e_DEmdeg float, 
            e_pmRA float,
            e_pmDE float,
            EpRAm float,
            EpDEm float,
            BTmag float,
            e_BTmag float, 
            PRIMARY KEY (TYC1, TYC2, TYC3)
    ) """)

    # Our prepared statements. Execute for each star.
    p = session.prepare("""
        INSERT INTO tycho.stars (
            TYC1, TYC2, TYC3, RAmdeg, DEmdeg, pmRA, pmDE, e_RAmdeg, 
            e_DEmdeg, e_pmRA, e_pmDE, EpRAm, EpDEm, BTmag, e_BTmag
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """)

    # Load our file. We are going to read line by line (ughghghghghghhggh).
    with open(argv[2], 'r') as c_f:
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
                    'e_RAmdeg': float(entry[57:60]),
                    'e_DEmdeg': float(entry[61:64]),
                    'e_pmRA': float(entry[65:69]),
                    'e_pmDE': float(entry[70:74]),
                    'EpRAm': float(entry[75:82]),
                    'EpDEm': float(entry[83:90]),
                    'BTmag': float(entry[110:116]),
                    'e_BTmag': float(entry[117:122]),
                }

                if node['BTmag'] < 9.0:
                    session.execute(p.bind((node['TYC1'], node['TYC2'], node['TYC3'], node['RAmdeg'], node['DEmdeg'],
                                            node['pmRA'], node['pmDE'], node['e_RAmdeg'], node['e_DEmdeg'],
                                            node['e_pmRA'], node['e_pmDE'], node['EpRAm'], node['EpDEm'],
                                            node['BTmag'], node['e_BTmag'])))
                    session.execute('UPDATE tycho.region '
                                    'SET InRegion = InRegion + {[' +
                                    '{}, '.format(node['TYC1']) +
                                    '{}, '.format(node['TYC2']) +
                                    '{}'.format(node['TYC3']) +
                                    ']} WHERE ' +
                                    'HRAmin = {} AND '.format(hash_c(node['RAmdeg'])) +
                                    'HDEmin = {}'.format(hash_c(node['DEmdeg'])))

            except ValueError as e:g
                pass

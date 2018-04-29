; Search for all stars near Canopus's location within 2 degrees.
COMPUTE HASH 95.9875 -52.6956
SELECT TYC1 FROM tycho.region WHERE HRAmax = {p[0]} AND HDEmax = {p[1]}
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

// Search for all stars near Alpha Centauri A's location within 2 degrees.
COMPUTE HASH 219.8958 -60.8375
SELECT TYC1 FROM tycho.region WHERE HRAmax = {p[0]} AND HDEmax = {p[1]}
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

// Search for all stars near Arcturus's location within 2 degrees.
COMPUTE HASH 213.9167 19.1822
SELECT TYC1 FROM tycho.region WHERE HRAmax = {p[0]} AND HDEmax = {p[1]}
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

// Search for all stars near Capella's location within 2 degrees.
COMPUTE HASH 79.1708 45.9981
SELECT TYC1 FROM tycho.region WHERE HRAmax = {p[0]} AND HDEmax = {p[1]}
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

// Search for all stars near Rigel's location within 2 degrees.
COMPUTE HASH 78.6333 -8.2017
SELECT TYC1 FROM tycho.region WHERE HRAmax = {p[0]} AND HDEmax = {p[1]}
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

// Search for all stars near Betelgeuse's location within 2 degrees.
COMPUTE HASH 88.7917 7.4069
SELECT TYC1 FROM tycho.region WHERE HRAmax = {p[0]} AND HDEmax = {p[1]}
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

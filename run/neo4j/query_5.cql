// Search for all stars near Canopus within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region),(s0:Star)-[:CONTAINS]-(a:Region) WHERE s0.TYC1 = 8534 AND s0.TYC2 = 2277 AND s0.TYC3 = 1 AND s.BTmag < 6.0 RETURN s

// Search for all stars near Alpha Centauri A within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region), (s0:Star)-[:CONTAINS]-(a:Region) WHERE s0.TYC1 = 9007 AND s0.TYC2 = 5849 AND s0.TYC3 = 1 AND s.BTmag < 6.0 RETURN s

// Search for all stars near Arcturus within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region),(s0:Star)-[:CONTAINS]-(a:Region) WHERE s0.TYC1 = 1472 AND s0.TYC2 = 1436 AND s0.TYC3 = 1 AND s.BTmag < 6.0 RETURN s

// Search for all stars near Capella within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region),(s0:Star)-[:CONTAINS]-(a:Region) WHERE s0.TYC1 = 3358 AND s0.TYC2 = 3141 AND s0.TYC3 = 1 AND s.BTmag < 6.0 RETURN s

// Search for all stars near Rigel within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region),(s0:Star)-[:CONTAINS]-(a:Region) WHERE s0.TYC1 = 5331 AND s0.TYC2 = 1752 AND s0.TYC3 = 1 AND s.BTmag < 6.0 RETURN s

// Search for all stars near Betelgeuse within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region),(s0:Star)-[:CONTAINS]-(a:Region) WHERE s0.TYC1 = 129 AND s0.TYC2 = 1873 AND s0.TYC3 = 1 AND s.BTmag < 6.0 RETURN s

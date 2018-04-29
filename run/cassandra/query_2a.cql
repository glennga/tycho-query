; Search for all stars near Canopus's location within 2 degrees (ALLOW FILTERING).
SELECT TYC1 FROM tycho.region WHERE RAmin < 95.9875 AND RAmax > 95.9875 AND DEmin < -52.6956 AND DEmax > -52.6956 ALLOW FILTERING
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

// Search for all stars near Alpha Centauri A's location within 2 degrees (ALLOW FILTERING).
SELECT TYC1 FROM tycho.region WHERE RAmin < 219.8958 AND RAmax > 219.8958 AND DEmin < -60.8375 AND DEmax > -60.8375 ALLOW FILTERING
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

// Search for all stars near Arcturus's location within 2 degrees (ALLOW FILTERING).
SELECT TYC1 FROM tycho.region WHERE RAmin < 213.9167 AND RAmax > 213.9167 AND DEmin < 19.1822 AND DEmax > 19.1822 ALLOW FILTERING
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

// Search for all stars near Capella's location within 2 degrees (ALLOW FILTERING).
SELECT TYC1 FROM tycho.region WHERE RAmin < 79.1708 AND RAmax > 79.1708 AND DEmin < 45.9981 AND DEmax > 45.9981 ALLOW FILTERING
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

// Search for all stars near Rigel's location within 2 degrees (ALLOW FILTERING).
SELECT TYC1 FROM tycho.region WHERE RAmin < 78.6333 AND RAmax > 78.6333 AND DEmin < -8.2017 AND DEmax > -8.2017 ALLOW FILTERING
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

// Search for all stars near Betelgeuse's location within 2 degrees (ALLOW FILTERING).
SELECT TYC1 FROM tycho.region WHERE RAmin < 88.7917 AND RAmax > 88.7917 AND DEmin < 7.4069 AND DEmax > 7.4069 ALLOW FILTERING
SELECT * FROM tycho.stars WHERE TYC1 = {p[0]}

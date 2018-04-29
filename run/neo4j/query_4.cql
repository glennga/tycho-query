// Search for all stars near Canopus's location within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region) WHERE 95.9875 > a.RAmin AND 95.9875 < a.RAmax AND -52.6956 > a.DEmin AND -52.6956 < a.DEmax AND s.BTmag < 6.0 RETURN s

// Search for all stars near Alpha Centauri A's location within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region) WHERE 219.8958 > a.RAmin AND 219.8958 < a.RAmax AND -60.8375 > a.DEmin AND -60.8375 < a.DEmax AND s.BTmag < 6.0 RETURN s

// Search for all stars near Arcturus's location within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region) WHERE 213.9167 > a.RAmin AND 213.9167 < a.RAmax AND 19.1822 > a.DEmin AND 19.1822 < a.DEmax AND s.BTmag < 6.0 RETURN s

// Search for all stars near Capella's location within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region) WHERE 79.1708 > a.RAmin AND 79.1708 < a.RAmax AND 45.9981 > a.DEmin AND 45.9981 < a.DEmax AND s.BTmag < 6.0 RETURN s

// Search for all stars near Rigel's location within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region) WHERE 78.6333 > a.RAmin AND 78.6333 < a.RAmax AND -8.2017 > a.DEmin AND -8.2017 < a.DEmax AND s.BTmag < 6.0 RETURN s

// Search for all stars near Betelgeuse's location within 2 degrees visible by the human eye.
MATCH (s:Star)-[:CONTAINS]-(a:Region) WHERE 88.7917 > a.RAmin AND 88.7917 < a.RAmax AND 7.4069 > a.DEmin AND 7.4069 < a.DEmax AND s.BTmag < 6.0 RETURN s
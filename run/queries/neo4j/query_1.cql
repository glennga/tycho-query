// Search for all stars near Canopus within 2 degrees.
MATCH (s:Star) WHERE s.TYC1 = 8534 AND s.TYC2 = 2277 AND s.TYC3 = 1 RETURN s

// Search for all stars near Alpha Centauri A within 2 degrees.
MATCH (s:Star) WHERE s.TYC1 = 9007 AND s.TYC2 = 5849 AND s.TYC3 = 1 RETURN s

// Search for all stars near Arcturus within 2 degrees.
MATCH (s:Star) WHERE s.TYC1 = 1472 AND s.TYC2 = 1436 AND s.TYC3 = 1 RETURN s

// Search for all stars near Capella within 2 degrees.
MATCH (s:Star) WHERE s.TYC1 = 3358 AND s.TYC2 = 3141 AND s.TYC3 = 1 RETURN s

// Search for all stars near Rigel within 2 degrees.
MATCH (s:Star) WHERE s.TYC1 = 5331 AND s.TYC2 = 1752 AND s.TYC3 = 1 RETURN s

// Search for all stars near Betelgeuse within 2 degrees.
MATCH (s:Star) WHERE s.TYC1 = 129 AND s.TYC2 = 1873 AND s.TYC3 = 1 RETURN s
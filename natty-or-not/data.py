from numpy import array

ENHANCED = 1
NATTY = 0

sample_biometrics = array([ #height (cm), weight (kg), 1rpm (kg)
    [188, 106.8, 238],
    [167, 100, 225.796],
    [172, 107, 165],
    [175, 109, 204.117],
    [178, 120.2, 288.031],
    [188, 150, 226.796],
    [173, 102, 215.456],
    [191, 118, 227],
    [175, 91, 136.078],
    [185, 109, 225],
    [175, 94, 183.705],
    [175, 100, 164],
    [188, 91, 177],
    [183, 97, 170],
    [183, 97.5, 227],
    [185.5, 107, 180]
])

sample_status = array([
    ENHANCED, ENHANCED, ENHANCED, ENHANCED, ENHANCED,
    ENHANCED, ENHANCED, ENHANCED, ENHANCED, ENHANCED,
    NATTY, NATTY, NATTY, NATTY, NATTY, NATTY
])

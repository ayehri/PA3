#Problem 2

cars.loc[0:4,::2]
cars.loc[(cars['Model'] == 'Mazda RX4')]
cars.loc[(cars['Model'] == 'Camaro Z28', ['cyl'])]
cars.loc[(cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['cyl', 'gear'])]

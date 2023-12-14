#“ Say that we want to find, among a collection of people, 
# one that could drive a car”

class DriverException(Exception):
    pass

people = [
    ('james',16),
    ('Augustine',7),
    ('Akira',14),
    ('Dianna',5)
    ]

driver = None # flag

for person,age in people:
    if age >= 18:
        driver = (person,age)
        break
if driver is None:
    raise DriverException("No eligible drivers found")
class DriverException(Exception):
    pass

people = [
    ('james',16),
    ('Augustine',7),
    ('Akira',14),
    ('Dianna',5)
    ]

for person,age in people:
    if age >= 18:
        driver = (person,age)
        break

else :
    raise DriverException("No eligible drivers found")
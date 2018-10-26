metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   #1 Each tuple holds a record with four fields, the last of which is a coordinate pair.
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  #2 By assigning the last field to a tuple, we unpack the coordinates.
    if longitude <= 0:  #3 if longitude <= 0: limits the output to metropolitan areas in the Western hemisphere.
        print(fmt.format(name, latitude, longitude))
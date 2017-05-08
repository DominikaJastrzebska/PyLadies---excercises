def get_data():
    a = float(input('Type side a: '))
    b = float(input('Type side b: '))
    H = float(input('Type height H: '))
    return a, b, H

def count_volume(a, b, H):
    V = a * b * H
    print('Volume of cuboid is: ',V)


get_data()
count_volume(a, b, H)

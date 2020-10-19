def size():
    Sizes = {
    'XXS' : ['Russia: 42', 'Germany: 36', 'USA: 8', 'France: 38', 'GB: 24'],
    'XS' : ['Russia: 44', 'Germany: 38' , 'USA: 10', 'France: 40', 'GB: 26'],
    'S' : ['Russia: 46', 'Germany: 40', 'USA: 12', 'France: 42', 'GB: 28'],
    'M' : ['Russia: 48', 'Germany: 42', 'USA: 14,' 'France: 44', 'GB: 30'],
    'L' : ['Russia: 50', 'Germany: 44', 'USA: 16', 'France: 46', 'GB: 32'],
    'XL' : ['Russia: 52', 'Germany: 46', 'USA: 18', 'France: 48', 'GB: 34'],
    'XXL' : ['Russia: 54', 'Germany: 48', 'USA: 20', 'France: 50', 'GB: 36]'],
    'XXXL' : ['Russia: 56', 'Germany: 50', 'USA: 22', 'France: 52', 'GB: 38']
    }

    if key in Sizes:
        print('Размеры в разных страннах', Sizes[key])
    else:
        print('Неверный размер')

key = str(input('Международный размер'))
size()
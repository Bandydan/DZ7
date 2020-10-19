d = {'Alex':(4, 3, 4, 4), 'Dani':(4, 3, 3, 5), 'Max':(4, 5, 5, 5)}
e = {}

for key in d:
    e[key] = sum(d[key]) // len(d[key])

    # e.update({'ivanov': (sum(d['ivanov']) // len(d['ivanov']))})
    # e.update({'balanov': (sum(d['balanov']) // len(d['balanov']))})
    # e.update({'sidorov': (sum(d['sidorov']) // len(d['sidorov']))})
print(max(e.items()), min(e.items()))
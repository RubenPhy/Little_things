import itertools, string

def plates():
    n = 1
    while True:
        for plate in itertools.product(string.ascii_lowercase,repeat = n):
            yield ''.join(plate)
        n += 1

num_plates = 100000
p = plates()
results = {i:next(p) for i in range(num_plates)}
print(results[num_plates-1])

import random
from util import save_to_file

def generate_dataset(n, lower_limit, upper_limit):
    arr = []
    for _ in range(n):
        arr.append(random.randint(lower_limit, upper_limit))
    return set(arr)

number = [20,200,2000]
subset = [20,25,30]
ukuran = ['Kecil', 'Sedang', 'Besar']
for i in range(len(number)):
    universe = set(range(1, number[i]+1))
    for j in range(len(subset)):
        dataset = []
        test_set = set()
        while test_set != universe:
            dataset = []
            test_set = set()
            for k in range(subset[j]):
                size = random.randint(number[i]//5, number[i]//2)
                x = generate_dataset(size, 1, number[i])
                dataset.append(x)
                test_set |= x
        costs = [random.randint(1, 100) for _ in range(subset[j])]
        save_to_file(f"dataset/{ukuran[i]}_{subset[j]}.txt", dataset, costs)
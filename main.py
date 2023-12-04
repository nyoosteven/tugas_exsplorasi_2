from branch_and_bound import BB
from greedy import set_cover
from memory_profiler import memory_usage
from util import save_to_file, file_to_data
import sys
import os
import time

def main_cover(cover_function, arr):
    memory_usages = memory_usage((time_main_cover, (cover_function, arr)), max_iterations=1)
    print(f'{max(memory_usages)} MB')

def time_main_cover(cover_function, arr):
    start_time = time.time()
    final = cover_function(arr[0], arr[1], arr[2])
    end_time = time.time()
    print(f'cost = {final[1]}')
    print(f'{(end_time - start_time) * 1000} ms\n')

def main():
    ukuran = ['Kecil', 'Sedang', 'Besar']
    subset = [20, 25, 30]
    dataset = {}
    
    for size in ukuran:
        for n in subset:
            dataset[f'{size}_{n}'] = file_to_data(f'dataset/{size}_{n}.txt')
    
    for size in ukuran:
        for n in subset:
            print(f'Greedy {size}_{n}')
            main_cover(set_cover, dataset[f'{size}_{n}'])
            print()
            print(f'Branch and Bound {size}_{n}')
            main_cover(BB, dataset[f'{size}_{n}'])
            print()

if __name__ == '__main__':
    sys.setrecursionlimit(2**17)
    main()
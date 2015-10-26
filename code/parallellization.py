# Job parallelization over many cores

from joblib import Parallel, delayed

def my_func(x):
    
    return x**2

if __name__ == '__main__':

    count = Parallel(n_jobs=-1)(delayed(my_func)(i) for i in range(10))
    print(count)
import time
import numpy as np
from functools import partial


def test_operators(n, op_type):
    if op_type == '+':
        return n + n
    elif op_type == '-':
        return n - n
    elif op_type == '*':
        return n * n
    elif op_type == '/':
        return n / n
    elif op_type == '%':
        return n % 234
    elif op_type == '**':
        return n ** n


def test_list_ops(lst, op_type, lst_len):
    if op_type == 'append':
        return lst.append(1)
    elif op_type == 'insert':
        return lst.insert(lst_len // 2, 1)
    elif op_type == 'pop':
        return lst.pop()
    elif op_type == 'pop_0':
        return lst.pop(0)
    elif op_type == 'in':
        return lst_len in lst
    elif op_type == '+':
        return lst + lst
    elif op_type == 'get':
        return lst[lst_len // 2]


def test_dict_ops(d, op_type, len_d):
    if op_type == 'insert':
        d['a'] = 1
        return d
    elif op_type == 'get':
        a = {}
        return a[np.random.randint(0, len_d)]
    elif op_type == 'pop':
        a = {}
        return a.pop()
    elif op_type == 'pop_n':
        return lst.pop(np.random.randint(0, len_d))
    elif op_type == 'in':
        return np.random.randint(0, 100000) in lst
    elif op_type == '+':
        return lst + lst


def test_func(func=None, inp_type=None):
    if inp_type == 'numb':
        test_numbers = list(np.arange(100, 1000000000, 10000))
        for n in test_numbers:
            t1 = time.time()
            func(n)
            print(f'n={n}; time elapsed={time.time() - t1}')
    if inp_type == 'list':
        test_lengths = [2 ** i for i in range(30)]
        for l in test_lengths:
            test_list = list(np.arange(0, l))
            list_len = len(test_list)
            t1 = time.time()
            func(test_list, 'get', list_len)
            print(f'N={l}; time elapsed={(time.time() - t1):.10f}')


test_func(func=test_list_ops, inp_type='list')
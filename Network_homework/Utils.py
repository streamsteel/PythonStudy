# -*- coding: utf-8 -*-
# @Author: Huggo
# @Date:   2018-10-19
# @Last Modified by:   Huggo
# @Last Modified time: 2018-10-22

def read_file(filename):
    data = []
    try:
        with open(filename, 'rt') as f:
            for line in f:
                if not line.startswith('#'):
                    fr, to = line.strip().split('\t')
                    data.append((int(fr), int(to)))
        return data
    except:
        print('Data does not exist!'.center(20, '='))

if __name__ == '__main__':
    data = read_file('Wiki-Vote.txt')
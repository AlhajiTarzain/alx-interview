#!/usr/bin/python3
'''module to return pascal triangle'''


def pascal_triangle(n):
    '''
    This is Pascals triangle
    Args:
      n (int): number of rows the triangle should return
    Returns:
      List of lists of integers triangle
    '''
    lists = []
    if n == 0:
        return lists
    for i in range(n):
        lists.append([])
        lists[i].append(1)
        if (i > 0):
            for j in range(1, i):
                lists[i].append(lists[i - 1][j - 1] + lists[i - 1][j])
            lists[i].append(1)
    return lists

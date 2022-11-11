 #...  # TODO реализовать функцию удаления элемента из списка по индексу


def delete(list_, index=None):
    if index is None:
        return list_[0:-1]
    else:
        return list_[0:index] + list_[index + 1:len(list_)]


print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]

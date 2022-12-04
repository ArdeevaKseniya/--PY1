def delete(list_, index=None):

    if index is None:
        index = list_[-1]

    left_side_not_including_index = list_[:index]
    right_side_not_including_index = list_[index+1:]

    return left_side_not_including_index + right_side_not_including_index

print(delete([0, 1, 2], index=-1))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]

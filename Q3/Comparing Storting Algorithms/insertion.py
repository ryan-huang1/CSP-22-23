def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def insertionsort(array):
    counter = 0
    for i in range(0, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j-1, j)
            j -= 1
            counter = counter + 1
            print(counter)

if __name__ == "__main__":
    array = [-8, 15, 25, -2, 0, 3, -4, 27, 13, 15, 10, 8, -8, 15, 25, -2, 0, 3, -4, 27, 13, 15, 10, 8, -8, 15, 25, -2, 0, 3, -4, 27, 13, 15, 10, 8, -8, 15, 25, -2, 0, 3, -4, 27, 13, 15, 10, 8]
    insertionsort(array)
    print(array)
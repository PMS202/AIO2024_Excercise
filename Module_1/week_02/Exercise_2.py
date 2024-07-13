
def max_over_kernel(lst, k):
    result = []
    for i in range(len(lst)):
        start = i
        end = i+k
        if end > len(lst):
            break
        print(lst[start: end])
        result.append(max(lst[start: end]))
    return result


def count_chars(str):
    result = {}
    for i in str.lower():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


def words_counting(file_path):

    with open(file_path, "r") as file:
        content = file.read()
    # print(content.split())
    result = {}

    for i in content.split():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result


def levenshtein_distance(source, target):
   # step 1: create array m x n
    n = len(source) + 1
    m = len(target) + 1
    arr = [[0]*m for _ in range(n)]

    # step 2: fill in first row and column
    for i in range(m):
        arr[0][i] = i

    for i in range(1, n):
        arr[i][0] = i

    # step 3: fill in arr
    del_cost = 0
    ins_cost = 0
    sub_cost = 0
    for i in range(1, n):
        for j in range(1, m):
            if source[i-1] == target[j-1]:
                cost = 0
            else:
                cost = 1

            del_cost = arr[i-1][j] + 1
            ins_cost = arr[i][j-1] + 1
            sub_cost = arr[i-1][j-1] + cost
            arr[i][j] = min(del_cost, ins_cost, sub_cost)
    return arr[n-1][m-1]


if __name__ == "__main__":
    # 1 Answer
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(max_over_kernel(num_list, k))

# 2 Answer
    string = 'smiles'
    print(count_chars(string))

# 3 Answer
    file_path = "D:\Hoc\AIO2024\AIO2024_Excercise\Module_1\week_02\P1_data.txt"
    result = words_counting(file_path)
    print(result['man'])


# 4 Answer
    source = "hola"
    target = "hello"
    print(levenshtein_distance(source, target))

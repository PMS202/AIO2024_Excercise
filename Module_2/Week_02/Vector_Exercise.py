import numpy as np

# 1. Các phép toán trên vector và ma trận.
# (a) Độ dài của vector:


def compute_vector_length(vector):

    len_of_vector = np.linalg.norm(vector)

    return len_of_vector

# (b) Phép tích vô hướng:


def compute_dot_product(vector1, vector2):

    result = vector1.dot(vector2)

    return result

# (c) Nhân vector với ma trận:


def matrix_multi_vector(matrix, vector):

    result = matrix.dot(vector)

    return result

# (d) Nhân ma trận với ma trận:


def matrix_multi_matrix(matrix1, matrix2):

    result = matrix1.dot(matrix2)

    return result

# (e) Ma trận nghịch đảo:


def inverse_matrix(matrix):

    result = np.linalg.inv(matrix)

    return result


# 2. Eigenvector và eigenvalues:

def compute_eigenvalues_eigenvectors(matrix):

    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    return eigenvalues, eigenvectors

# 3. Cosine Similarity:


def compute_cosine(v1, v2):

    cos_sin = np.dot(v1, v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))

    return cos_sin

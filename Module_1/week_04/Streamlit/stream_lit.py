import streamlit as st


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        words = sorted(set([words.strip() for words in lines]))
        return words


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


st.markdown(
    """
    <style>
    @keyframes gradient {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }

    .stApp {
        background: linear-gradient(-45deg, #ff7e5f, #feb47b, #86e3ce, #d4a5a5);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def streamlist():
    st.title("Word Correction")
    input_text = st.text_input("Nhập vào đây")
    if st.button("Find Words"):
        distance = [levenshtein_distance(input_text, words)
                    for words in vocabs]
        st.subheader("This is correct words:")
        st.header(vocabs[distance.index(min(distance))], divider=True)
        sorted_distance = dict(
            sorted(zip(vocabs, distance), key=lambda item: item[1]))
        col1, col2 = st.columns(2)
        col1.write("Vocabs:")
        col1.write(vocabs)
        col2.write("Distance:")
        col2.write(sorted_distance)


if __name__ == "__main__":
    vocabs = load_vocab(
        r"C:\Users\MISA\Downloads\Compressed\source\source\data\vocab.txt")
    streamlist()

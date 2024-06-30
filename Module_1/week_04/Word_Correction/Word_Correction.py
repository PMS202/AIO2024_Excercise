import streamlit as st


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        words = sorted(set([words.strip() for words in lines]))
        return words


def leven_distance(token1, token2):
    m = len(token1)
    n = len(token2)

    distances = [[0] * (n + 1) for _ in range(m + 1)]

    for t1 in range(m + 1):
        distances[t1][0] = t1

    for t2 in range(n + 1):
        distances[0][t2] = t2

    a, b, c = 0, 0, 0

    for t1 in range(1, m + 1):
        for t2 in range(1, n + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]     # Thêm
                b = distances[t1 - 1][t2]     # Xóa
                c = distances[t1 - 1][t2 - 1]  # Thay thế

                if a <= b and a <= c:
                    distances[t1][t2] = a + 1
                elif b <= a and b <= c:
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1
    return distances[m][n]


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

    st.markdown("# Word Correction\nMade by Phúc")
    input_text = st.text_input("Nhập vào đây")
    if st.button("Find Words"):
        distance = [leven_distance(input_text, words)
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
        r"D:\Hoc\AIO2024\AIO2024_Excercise\Module_1\week_04\Word_Correction\vocab.txt")
    streamlist()

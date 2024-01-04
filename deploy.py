import streamlit as st


def main():
    st.title("Ứng dụng đếm từ")
    

    user_input = st.text_input("Nhập văn bản:")
    

    words = user_input.split()
    word_count = len(words)
    

    st.write(f"Số từ trong văn bản: {word_count}")

if __name__ == '__main__':
    main()

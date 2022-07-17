
import math

import seaborn as sns
import streamlit as st


@st.cache
def load_dataset():
    """Titanic データセットを読み込む関数"""
    return sns.load_dataset('titanic')


def main():
    # データセットを読み込んで必要なページ数を計算する
    df = load_dataset()
    rows_per_page = 10
    total_pages = math.ceil(len(df) / rows_per_page)

    if 'page' not in st.session_state:
        st.session_state['page'] = 1

    left_col, center_col, right_col = st.beta_columns(3)

    # ページ数の増減ボタン
    with left_col:
        def minus_one_page():
            st.session_state['page'] -= 1
        if st.session_state['page'] > 1:
            st.button(label='<< Prev',
                      on_click=minus_one_page)

    with right_col:
        def plus_one_page():
            st.session_state['page'] += 1
        if st.session_state['page'] < total_pages:
            st.button(label='Next >>',
                      on_click=plus_one_page)

    # 現在のページ番号
    with center_col:
        st.write(f"Page: {st.session_state['page']} / {total_pages}")

    # ページ番号に応じた範囲のデータフレームを表示する
    start_iloc = (st.session_state['page'] - 1) * rows_per_page
    end_iloc = start_iloc + rows_per_page + 1
    st.write(df.iloc[start_iloc:end_iloc])


if __name__ == '__main__':
    main()
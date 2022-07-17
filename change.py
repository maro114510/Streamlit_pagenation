import streamlit as st

def main():
    # １ページ目表示
    st.sidebar.title("test_streamlit")
    st.session_state["file"]=st.sidebar.file_uploader("upload")
    if st.session_state["file"] != None:
        st.session_state["page_control"] = 1
        raise st.experimental_rerun()

def next_page():
    # ２ページ目表示
    st.sidebar.title("ページが切り替わりました")
    st.markdown("## 次のページです")
    st.markdown("ファイルの中身")
    st.markdown(st.session_state["file"])

# 状態保持する変数を作成して確認
if ("page_control" in st.session_state and
   st.session_state["page_control"] == 1):
    next_page()
else:
    st.session_state["page_control"] = 0
    main()
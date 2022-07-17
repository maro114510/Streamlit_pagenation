
import streamlit as st


st.write("Hello,world")
st.title('Counter ')
if "count" not in st.session_state:
  st.session_state.count =0

def incremet_counter():
  st.session_state.count += 1

st.button('Increment',on_click=incremet_counter)

st.write('Count =',st.session_state.count)

st.text_input("message",key="text_input")

def change_value():
  st.session_state['text_input'] == "hello,world"

st.button('Click',on_click=change_value)

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

def page1():
    st.title("What's your name?")

    def change_page():
        st.session_state["page-select"] = "page2"

    with st.form(key="name-form"):
        st.text_input("Name", key="name")
        st.form_submit_button(label="Submit", on_click=change_page)


def page2():
    name = st.session_state["name"]
    st.title(f"Hello, {name}")


pages = dict(
    page1="ページ1",
    page2="ページ2",
)

page_id = st.sidebar.selectbox( # st.sidebar.*でサイドバーに表示する
    "ページ名",
    ["page1", "page2"],
    format_func=lambda page_id: pages[page_id], # 描画する項目を日本語に変換
)

if page_id == "page1":
    page1()

if page_id == "page2":
    page2()

from dataclasses import dataclass


@dataclass
class Mutable:
    is_broken: bool = False


@dataclass(frozen=True)
class Immutable:
    is_broken: bool = False


taro_house = Mutable()
jiro_house = Mutable()
maburo_house = Immutable()

taro_house.is_broken = True
jiro_house.is_broken = True
maburo_house.is_broken = True  

from pathlib import Path
from typing import Protocol

class IRepository(Protocol):
    def get(self) -> list[str]:
        pass

class FileRepository(IRepository):
    def get(self) -> list[str]:
        return Path("members.txt").read_text().split(",")

class MemoryRepository(IRepository):
    def get(self) -> list[str]:
        return ["Taro", "Jiro", "Saburo"]
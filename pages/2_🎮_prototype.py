import streamlit as st
from streamlit import session_state as stss

from modules.utils import read_data  # type: ignore
from views.prototype.add_data import add_data  # type: ignore
from views.prototype.check_metrics import check_metrics  # type: ignore
from views.prototype.edit_and_calc import edit_and_calc  # type: ignore
from views.prototype.search import search  # type: ignore

data = read_data()

if "id_add_row" not in stss:
    stss.id_add_row = 0
if "id_add_csv" not in stss:
    stss.id_add_csv = 0
if "id_add_files" not in stss:
    stss.id_add_files = 0


# ページ全般の設定
st.set_page_config(
    layout="wide",
    page_title="prototype - pages for hands-on",
    page_icon="🎮",
)

# ヘッダー
st.header("Prototype Sample", divider="gray")

# サイドバー: 検索条件入力欄
filtered_data = search(area=st.sidebar, data=data)

# タブ
tabs = st.tabs(["Add Data", "Edit & Calculate", "Check Metrics"])
with tabs[0]:
    add_data(area=st, data=data, filtered_data=filtered_data)

with tabs[1]:
    edit_and_calc(area=st, data=data, filtered_data=filtered_data)

with tabs[2]:
    check_metrics(area=st, data=data, filtered_data=filtered_data)

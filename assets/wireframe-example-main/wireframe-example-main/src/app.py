import pandas as pd
import streamlit as st

from views.add_data import add_data  # type: ignore
from views.check_metrics import check_metrics  # type: ignore
from views.disp_data import disp_data  # type: ignore
from views.edit_and_calc import edit_and_calc  # type: ignore
from views.search import search  # type: ignore

# データの取得
df = pd.read_csv("./assets/data.csv", encoding="utf-8")

# ページ全般の設定
st.set_page_config(layout="wide")

# ヘッダー
st.header("Wireframe Sample", divider="gray")

# サイドバー: 検索条件入力欄
search(area=st.sidebar)

# タブ
tabs = st.tabs(["Add Data", "Edit & Calculate", "Check Metrics"])
with tabs[0]:
    disp_data(area=st, data=df, height=230)
    add_data(area=st)

with tabs[1]:
    disp_data(area=st, data=df, height=570)
    edit_and_calc(area=st)

with tabs[2]:
    disp_data(area=st, data=df, height=230)
    check_metrics(area=st, data=df)

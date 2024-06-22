import streamlit as st


def edit_and_calc(area):
    col_l, col_r = area.columns([1, 7])
    if col_l.checkbox("Edit Mode"):
        # 変更反映ボタンを押さなければ何もしない
        if not col_r.button("Save Changes"):
            return None

        # 以下は変更反映ボタンが押された場合
        inform_modified()
    else:
        # 計算実行ボタンを押さなければ何もしない
        if not col_r.button("Request Calculation"):
            return None

        # 以下は計算実行ボタンが押された場合
        calc()


@st.experimental_dialog("Modification saved")
def inform_modified():
    pass


@st.experimental_dialog("Calculate")
def calc():
    st.write("Are you sure you want to request calculation?")
    st.text_input("Any Comments:")
    if st.button("Request"):
        st.success("Requested calculation succesfully")

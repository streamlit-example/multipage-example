# 検索
def search(area):
    area.title("Search Commands")
    area.multiselect("Status", options=["just_uploaded", "calculating", "calculated"])
    area.text_input("Name")
    area.text_input("Type")
    area.number_input("Max Size", value=None)
    area.number_input("Min Size", value=None)

    area.title("Reload")
    area.button("Reload Data")

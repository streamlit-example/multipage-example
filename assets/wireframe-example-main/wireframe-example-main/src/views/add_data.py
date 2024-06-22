def add_data(area):
    columns_ = area.columns([2, 3])
    columns_[0].subheader("Upload")
    add_files(area=columns_[0])
    add_csv(area=columns_[0])
    add_row(area=columns_[1])


def add_row(area):
    area.subheader("Add Data")

    cols1 = area.columns(3)
    cols1[0].text_input("ID", key="id")
    cols1[1].text_input("Name", key="name")
    cols1[2].text_input("Type", key="type")

    cols2 = area.columns(3)
    cols2[0].number_input("Size 1", value=None)
    cols2[1].number_input("Size 2", value=None)
    cols2[2].number_input("Size 3", value=None)

    area.text_input("Remarks (optional)", "")

    area.button("Add data")


def add_files(area):
    area.file_uploader("Files", accept_multiple_files=True)
    area.button("Upload Files")


def add_csv(area):
    area.file_uploader("CSV", type="csv")
    area.button("Upload CSV")

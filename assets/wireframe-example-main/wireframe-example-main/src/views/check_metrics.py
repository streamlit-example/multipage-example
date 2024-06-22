import matplotlib.pyplot as plt


def check_metrics(area, data):
    cols = area.columns(3)
    cols[0].scatter_chart(
        data=data.rename(columns={"Size X [cm]": "x"}), x="x", y="Rate"
    )  # こうしなければ、スペースあるいは角カッコが災いしてグラフが表示されない
    cols[1].bar_chart(data.sort_values("Rate", ascending=False), x="Name", y="Rate")
    data_count = data["Status"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(list(data_count.values), labels=list(data_count.index))
    cols[2].pyplot(fig)

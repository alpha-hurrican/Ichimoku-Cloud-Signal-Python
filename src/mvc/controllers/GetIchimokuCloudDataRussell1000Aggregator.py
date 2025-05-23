from src.mvc.core.DataCloudSignalAggregatorMVC import Control, Model, View


def main(
    fetch1HData=False,
    fetchDailyData=True,
    fetchWeeklyData=False,
    fetchMonthlyData=False,
):
    if fetch1HData:
        _model = Model(
            "data/russell1000/1h/",
            "asset_list/Russell1000.csv",
            "output/cloud/",
            "Russell1000-cloud-1H",
            "1H",
            True,
        )
        _control = Control(_model, View())
        _control.main()
    if fetchDailyData:
        _model = Model(
            "data/russell1000/d/",
            "asset_list/Russell1000.csv",
            "output/cloud/",
            "Russell1000-cloud-D",
            "1D",
        )
        _control = Control(_model, View())
        _control.main()
    if fetchWeeklyData:
        _model = Model(
            "data/russell1000/w/",
            "asset_list/Russell1000.csv",
            "output/cloud/",
            "Russell1000-cloud-W",
            "1W",
        )
        _control = Control(_model, View())
        _control.main()
    if fetchMonthlyData:
        _model = Model(
            "data/russell1000/m/",
            "asset_list/Russell1000.csv",
            "output/cloud/",
            "Russell1000-cloud-M",
            "1M",
        )
        _control = Control(_model, View())
        _control.main()


if __name__ == "__main__":
    main()

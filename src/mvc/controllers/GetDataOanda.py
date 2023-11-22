from src.mvc.core.DataPandasForexOandaMVC import Control, Model, View


def main(
    fetch1HData=False,
    fetch4HData=False,
    fetchDailyData=False,
    fetchWeeklyData=False,
    fetchMonthlyData=False,
):
    # period: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    # interval: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

    if fetch1HData:
        _model = Model(
            "data/forexoanda/1h/",
            "asset_list/ForexOanda.csv",
            "H1",
            "300",
            True,
        )
        _control = Control(_model, View())
        _control.main()
    if fetch4HData:
        # print("fetch 4h")
        _model = Model(
            "data/forexoanda/4h/",
            "asset_list/ForexOanda.csv",
            "H4",
            "300",
            True,
        )
        _control = Control(_model, View())
        _control.main()
    if fetchDailyData:
        _model = Model(
            "data/forexoanda/d/",
            "asset_list/ForexOanda.csv",
            "D",
            "300",
            True,
        )
        _control = Control(_model, View())
        _control.main()
    if fetchWeeklyData:
        _model = Model(
            "data/forexoanda/w/",
            "asset_list/ForexOanda.csv",
            "W",
            "300",
            True,
        )
        _control = Control(_model, View())
        _control.main()
        _control.showAssetList()
    if fetchMonthlyData:
        _model = Model(
            "data/forexoanda/m/",
            "asset_list/ForexOanda.csv",
            "M",
            "300",
            True,
        )
        _control = Control(_model, View())
        _control.main()
        _control.showAssetList()


if __name__ == "__main__":
    main()

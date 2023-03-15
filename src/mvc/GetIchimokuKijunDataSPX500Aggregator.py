from src.mvc.DataKijunSignalAggregatorMVC import Control, Model, View


def main(fetchDailyData=True, fetchWeeklyData=False):
    if fetchDailyData:
        _model = Model(
            "data/spx500/d/", "asset_list/SPX500.csv", "output/", "SPX 500-D"
        )
        _control = Control(_model, View())
        _control.main()
    if fetchWeeklyData:
        _model = Model(
            "data/spx500/w/", "asset_list/SPX500.csv", "output/", "SPX 500-W"
        )
        _control = Control(_model, View())
        _control.main()


if __name__ == "__main__":
    main()
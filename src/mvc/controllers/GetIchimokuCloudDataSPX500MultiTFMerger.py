from src.mvc.core.DataCloudSignalMultiTimeframeMerger import (
    Control,
    Model,
    View,
)


def main(run_merger=True):
    if run_merger:
        _model = Model(
            [
                "output/SPX500-cloud-D.csv",
                "output/SPX500-cloud-W.csv",
                "output/SPX500-cloud-M.csv",
            ],
            "output/SPX500-cloud-merged.csv",
        )
        _control = Control(_model, View())
        _control.main()


if __name__ == "__main__":
    main()
# from DataKickerSignalMVC import Control, Model, View
from src.mvc.DataKickerSignalMVC import Control, Model, View

def main():
    _model = Model('data/ftse100/d/', 'asset_list/FTSE100.csv')
    _control = Control(_model, View())
    _control.main()    

    _model = Model('data/ftse100/w/', 'asset_list/FTSE100.csv')
    _control = Control(_model, View())
    _control.main()

if __name__ == "__main__":
    main()
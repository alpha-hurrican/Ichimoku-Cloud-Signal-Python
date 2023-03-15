import pandas as pd
from abc import abstractclassmethod, ABC


class DataOHLC(ABC):
    @abstractclassmethod
    def readLocalCsvData(self, symbols, __csvPath):
        pass


class DataCloudSignal(DataOHLC):
    def __init__(self, __symbol, __csvPath, __isIntraday=False):
        self.symbol = __symbol
        self.csvPath = __csvPath
        self.isIntraday = __isIntraday

    def setupPd_intraday(self, csvSuffix="_cloud.csv", folderPath="data/"):
        pd.set_option("display.max_rows", None)  # print every row for debug
        pd.set_option("display.max_columns", None)  # print every column for debug

        try:
            __path = self.csvPath + self.symbol + csvSuffix
            __data = pd.read_csv(__path)
            # print(__path)
            # print(__data.Datetime)
            __data.index = __data.Datetime
            __data["Returns"] = self.getReturn(
                __data["Close"], __data["Close"].shift(1)
            )
            __data["Cloud Signal"] = self.getCloudDirection(
                __data["Close"], __data["senkou_span_a"], __data["senkou_span_b"]
            )
            __data["Cloud Signal Count"] = self.getCloudSignalCount(
                __data["Cloud Signal"]
            )
            self.setColumnsSaveCsv_intraday(__data)
            # print(__data)
        except FileNotFoundError:
            print(f"Error: {__path} not found")

    def setupPd(self, csvSuffix="_cloud.csv", folderPath="data/"):
        pd.set_option("display.max_rows", None)  # print every row for debug
        pd.set_option("display.max_columns", None)  # print every column for debug
        try:
            __path = self.csvPath + self.symbol + csvSuffix
            __data = pd.read_csv(__path)
            # print(__data.Date)
            __data.index = __data.Date
            __data["Returns"] = self.getReturn(
                __data["Close"], __data["Close"].shift(1)
            )
            __data["Cloud Signal"] = self.getCloudDirection(
                __data["Close"], __data["senkou_span_a"], __data["senkou_span_b"]
            )
            __data["Cloud Signal Count"] = self.getCloudSignalCount(
                __data["Cloud Signal"]
            )
            print(__data)
            self.setColumnsSaveCsv(__data)
        except FileNotFoundError:
            print(f"Error: {__path} not found")

    def getCloudSignalCount(self, __cloudDirectionList):
        __newList = []
        __cloudDirectionCount = None
        __curCloudDirection = None
        for __i in range(len(__cloudDirectionList)):
            if pd.isna(__cloudDirectionList[__i]):
                __cloudDirectionCount = __cloudDirectionList[__i]
            elif __curCloudDirection == None:
                __curCloudDirection = __cloudDirectionList[__i]
                __cloudDirectionCount = 1
            elif not __cloudDirectionList[__i] == __curCloudDirection:
                __curCloudDirection = __cloudDirectionList[__i]
                __cloudDirectionCount = 1
            else:
                __cloudDirectionCount += 1

            __newList.append(__cloudDirectionCount)
        return __newList

    def getCloudDirection(self, __close, __senkou_span_a, __senkou_span_b):
        __data = []
        __curDirection = None
        # print(__senkou_span_a)
        for __i in range(len(__senkou_span_b)):
            if pd.isna(__senkou_span_b[__i]):
                # pass alone senkou span b NaN back to column
                __data.append(__senkou_span_b[__i])
            elif pd.isna(__senkou_span_a[__i]):
                __data.append(__senkou_span_b[__i])
            elif (
                # Close is above the cloud
                __close[__i] > __senkou_span_a[__i]
                and __close[__i] > __senkou_span_b[__i]
            ):
                __curDirection = 1
                __data.append(__curDirection)
            elif (
                # Close is below the cloud
                __close[__i] < __senkou_span_a[__i]
                and __close[__i] < __senkou_span_b[__i]
            ):
                __curDirection = -1
                __data.append(__curDirection)
            # elif (
            #     __close[__i] < __senkou_span_a[__i]
            #     and __close[__i] > __senkou_span_b[__i]
            # ):
            #     # Close is within cloud
            #     __curDirection = 0
            #     __data.append(__curDirection)
            # elif (
            #     # Close is within cloud
            #     __close[__i] > __senkou_span_a[__i]
            #     and __close[__i] < __senkou_span_b[__i]
            # ):
            #     __curDirection = 0
            #     __data.append(__curDirection)
            else:
                # Close is within cloud
                __curDirection = 0
                __data.append(__curDirection)
        # print(__data)
        return __data

    def getReturn(self, __curClose, __preClose):
        return __curClose / __preClose - 1

    def setColumnsSaveCsv(self, __data, csvSuffix="_cloudCount.csv"):
        header = ["Date", "Cloud Signal", "Cloud Signal Count"]
        __data.to_csv(
            self.csvPath + self.symbol + csvSuffix, columns=header, index=False
        )

    def setColumnsSaveCsv_intraday(self, __data, csvSuffix="_cloudCount.csv"):
        header = ["Datetime", "Cloud Signal", "Cloud Signal Count"]
        __data.to_csv(
            self.csvPath + self.symbol + csvSuffix, columns=header, index=False
        )

    def readLocalCsvData(self, symbols, __csvPath):
        pass

    def main(self):
        if self.isIntraday == False:
            self.setupPd(
                "_ichimokuTapy.csv"
            )  # _ichimokuPlotly _ichimokuTapy _ichimokuFinta
        else:
            self.setupPd_intraday(
                "_ichimokuTapy.csv"
            )  # _ichimokuPlotly _ichimokuTapy _ichimokuFinta


class Model(object):
    def __init__(self, __csvPath, __assetListPath, __isIntraday=False):
        self.csvPath = __csvPath
        self.assetListPath = __assetListPath
        self.isIntraday = __isIntraday
        self.symbols = None
        self.dataOHLC = None

    @property
    def isIntraday(self):
        return self.__isIntraday

    @isIntraday.setter
    def isIntraday(self, __isIntraday):
        self.__isIntraday = __isIntraday

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, __symbol):
        self.__symbol = __symbol

    @property
    def csvPath(self):
        return self.__csvPath

    @csvPath.setter
    def csvPath(self, __csvPath):
        self.__csvPath = __csvPath

    @property
    def assetListPath(self):
        return self.__assetListPath

    @assetListPath.setter
    def assetListPath(self, __assetListPath):
        self.__assetListPath = __assetListPath

    def readAssetList(self, __csvPath, __colName="symbol"):
        df = pd.read_csv(__csvPath)
        # print(df.to_string())
        l_symbol = df[__colName].tolist()
        self.symbols = l_symbol
        return l_symbol

    def readLocalCsvData(self, symbols, __csvPath):
        __dict_df = {}
        for __symbol in symbols:
            try:
                __filePath = __csvPath + __symbol + ".csv"
                __df = pd.read_csv(__filePath)
                __dict_df[__symbol] = __df
            except FileNotFoundError:
                print(f"Error: {__filePath} not found")
                continue
        return __dict_df

    def getBatchLocalData(self):
        self.dataOHLC = self.readLocalCsvData(self.symbols, self.csvPath)

    def getIndividualSymbolData(self):
        for __symbol, __value in self.dataOHLC.items():
            # print(__symbol, self.csvPath)
            dataP = DataCloudSignal(__symbol, self.csvPath, self.isIntraday)
            dataP.main()
        print("Cloud signal count csv files are created")


class Control(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def getAssetList(self):
        self.model.readAssetList(self.model.assetListPath)

    def showAssetList(self):
        __dict_symbols = self.model.readAssetList(self.model.assetListPath)
        self.view.showAssetList(__dict_symbols)

    def getDataOHLC(self):
        self.model.getDataOHLC()

    def getBatchLocalData(self):
        self.model.getBatchLocalData()

    def getIndividualSymbolData(self):
        self.model.getIndividualSymbolData()

    def main(self):
        print("-------------------- Generating Cloud Signals --------------------")
        self.getAssetList()
        self.getBatchLocalData()
        self.getIndividualSymbolData()


class View(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    _model = Model("data/futurescurrency/w/", "asset_list/FuturesCurrency.csv")
    _control = Control(_model, View())
    _control.main()
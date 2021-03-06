import pandas as pd
from matplotlib import pyplot as plt

class Visitors():
    topVisitorCnt = 0
    topCountry = ""
    secondTopVisitorCnt = 0
    secondCountry = ""
    thirdTopVisitorCnt = 0
    thirdCountry = ""

    def __init__(self):
        xls = pd.ExcelFile("Project_File.xlsx")
        # print(xls)
        self.myCols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.myColNames = ["MonthYear", "Brunei Darussalam", "Indonesia", "Malaysia", "Philippines", "Thailand", "Viet Nam", "Myanmar", "Japan", "Hong Kong", "China", "Taiwan", "Korea, Republic Of"]
        self.mydata = xls.parse(0, usecols= self.myCols, names = self.myColNames)
        # print(self.mydata["MonthYear"])

        splitYear = self.mydata["MonthYear"].str.split(" ", n=1, expand= True)
        #print(splitYear)

        self.mydata = self.mydata.assign(Year=splitYear[0])
        # print("\nAdded back Year Column")
        #print(self.mydata)

        self.mydata = self.mydata.assign(Month=splitYear[1])
        # print("\nAdded back Month Column")
        # print(self.mydata)

        self.mydata = self.mydata[self.mydata["Year"].astype(int) >= 2000]
        # print("\nRemove Years less than 2000")
        #print(self.mydata)

        self.mydata = self.mydata[self.mydata["Year"].astype(int) <= 2001]
        # print("\nRemove Years more than 2001")
        print(self.mydata)

    def generate2000MalaysiaAvg(self):
        # print("generating MY avg")
        # print(self.mydata)

        # print("\nGet the MY columns")
        # print(self.mydata.iloc[:, [3,13,14]] )
        malaysia = self.mydata.iloc[:, [3,13,14]]
        malaysia2000 = malaysia[malaysia["Year"] == "2000"]
        # print("\nOnly MY 2000")
        # print(malaysia2000)
        myMean = malaysia2000["Malaysia"].mean()
        print("\nThe average visitors from Malaysia in 2000: " + str(myMean))

    def makeMalaysia2000LineChart(self):
        malaysia = self.mydata.iloc[:, [3,13,14]]
        malaysia2000 = malaysia[malaysia["Year"] == "2000"]

        print("\nOnly MY 2000")
        print(malaysia2000)

        plt.plot(malaysia2000["Month"], malaysia2000["Malaysia"])
        plt.title("Malaysian Visitors in Year 2000")
        plt.show()
#dgfbfdbfgbf
    def getMalaysia2000VisitorCount(self):
        malaysia = self.mydata.iloc[:, [3,13,14]]
        malaysia2000 = malaysia[malaysia["Year"]== "2000" ]
        return malaysia2000["Malaysia"].sum()

    def getTop3Countries(self):
        for country in self.myColNames:

            if country != "MonthYear":
                # print(country)
                # print(self.mydata[country].sum())

                if self.mydata[country].sum() > self.topVisitorCnt:
                    self.topVisitorCnt = self.mydata[country].sum()
                    self.topCountry = country
                elif self.mydata[country].sum() > self.secondTopVisitorCnt:
                    self.secondTopVisitorCnt = self.mydata[country].sum()
                    self.secondCountry = country
                elif self.mydata[country].sum() > self.thirdTopVisitorCnt:
                    self.thirdTopVisitorCnt = self.mydata[country].sum()
                    self.thirdCountry = country

        print("\n" + self.topCountry)
        print(self.topVisitorCnt)
        print("\n" + self.secondCountry)
        print(self.secondTopVisitorCnt)
        print("\n" + self.thirdCountry)
        print(self.thirdTopVisitorCnt)

# test = Visitors()
# test.generate2000MalaysiaAvg()
# test.makeMalaysia2000LineChart()
# test.getTop3Countries()
# print(test.getMalaysia2000VisitorCount())
from FormattedData import FormatData

NewData = FormatData.ReadData("TestFile.csv")

for Entry in NewData:
    print(Entry)

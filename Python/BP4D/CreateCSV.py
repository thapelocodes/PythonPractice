from FormattedData import FormatData

NewData = [FormatData("George", 65, True),
           FormatData("Sally", 47, False),
           FormatData("Doug", 52, True)]

FormatData.SaveData("TestFile.csv", NewData)

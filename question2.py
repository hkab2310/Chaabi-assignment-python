# Q2. Dictionary, what?
# Write a program that returns the file type from a file name. The type of the file is determined
# from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
# png,image) will be input.
# The program takes input in the following form:
# 1. Input extension and type values in the form of a string having the following format:
# a. "extension1,type1;extension2,type2;extension3,type3"
# b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
# our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
# 2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
# "xyz.xls", "text.csv", "123"]
# The program should return a dict of filename: type pairs
# E.g.
# f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
# "xyz.xls", "text.csv", "123"]) should return
# {
# "abc.jpg": "image",
# "xyz.xls": "spreadsheet",
# "Text.csv": "unknown",
# "123": "unknown"
# }

extensionTypeString = input()
fileNamesList = input().split(" ")   #input the list values in space separated manner
# print(extensionTypeString,fileNamesList)
extensions =extensionTypeString.split(";")
extensionList = []
for i in range(0,len(extensions)):
    extensionList.append({
        "extension" : extensions[i].split(",")[0],
        "filetype" : extensions[i].split(",")[1]
    })

# print(extensionList)
filesDictionary = {}
for i in range(0,len(fileNamesList)):
    if fileNamesList[i].find(".") == -1:
        filesDictionary[fileNamesList[i]] = "unknown"
    else:
        fileName = fileNamesList[i].split(".")[0]
        fileExtension = fileNamesList[i].split(".")[1]
        derivedFileType = "unknown"
        for j in range(0,len(extensionList)):
            if extensionList[j]["extension"] == fileExtension:
                derivedFileType = extensionList[j]["filetype"]
        filesDictionary[fileNamesList[i]] = derivedFileType


print(filesDictionary)
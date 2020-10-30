def romanToDecimal(roman_number):
    roman_list = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for index,current_number in enumerate(roman_number):
        if (index+1) == len(roman_number) or roman_list[current_number] >= roman_list[roman_number[index+1]]:
            result+=roman_list[current_number]
        else:
            result-=roman_list[current_number]
    return result

'''
arabes=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII','XXIII','XXIV','XXV','XXVI','XXVII','XXVIII','XXIX','XXX','XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL','XLI','XLII','XLIII','XLIV','XLV','XLVI','XLVII','XLVIII','XLIX','L']

for i in arabes:
    roman_to_decimal(i)
'''

def sortRoman(names):
    listOrdererByName = []
    listOrdererByNumber = []
    middleList = []
    tempList = []
    # To generate the equivalent decimal number in a list of tuples
    for currentName in names:
        listOrdererByName.append((currentName.split(' ')[0],currentName.split(' ')[1],romanToDecimal(currentName.split(' ')[1])))
    # To order by name
    listOrdererByName=sorted(listOrdererByName)
    # To split equal list of names 
    for index,currentName in enumerate(listOrdererByName):
        if index == 0:
            tempList.append(currentName)
        else:
            # If the current name is equal to the previous, then append it in the same sublist
            if currentName[0] == listOrdererByName[index-1][0]:
                tempList.append(currentName)
                # Ultimo nombre
                if index == (len(listOrdererByName)-1):
                    middleList.append(tempList)
            # In other case, append it in a new sublist
            else:
                middleList.append(tempList)
                tempList=[]
                tempList.append(currentName)
                # Last iteration
                if index == (len(listOrdererByName)-1):
                    middleList.append(tempList)                

    # To order sublist
    for subList in middleList:
        tempList=[]
        tempList.append(sorted(subList,key=lambda x:x[2]))
        # Finally, generate the resulting list
        for index,currentName in enumerate(tempList[0]):
            listOrdererByNumber.append(currentName[0]+' '+currentName[1])
    return print(listOrdererByNumber)

def main():
    names=['Steven XL','Steven XVI','David IX','Mary XV','Mary XIII','Mary XX']
    sortRoman(names)
    names=['Louis IX','Philippe II']
    sortRoman(names)

if __name__ == '__main__':
    main()

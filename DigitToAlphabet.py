# A system that can convert digits into alphabetical string. For example: 12019 -> Twelve thousand and nineteen
upperLimit = 10**6
notAustistic = False
while not notAustistic:
    userInput = int(input('Enter a number between 0 to 10 million: '))
    if userInput > 10**6 or userInput < 0:
        print("ENTER A NUMBER WITHIN THE SPECIFIED RANGE!")
    else:
        notAustistic = True
userInput = str(userInput)
tens = {
    1: "Ten",
    2: "Twenty",
    3: "Thirty",
    4: "Fourty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety"
}
teens = {
    1: "Eleven",
    2: "Twelve",
    3: "Thirteen",
    4: "Fourteen",
    5: "Fifteen",
    6: "Sixteen",
    7: "Seventeen",
    8: "Eighteen",
    9: "Nineteen"
}
ones = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}
length = 0
for num in userInput:
    length += 1
# i = length
output = ""
i = length  # Start from the last index

while i > 0:  # Use a while loop to control iteration manually
    digit = int(userInput[-i])

    if digit == 0:
        i -= 1
        continue
    else:
        if i % 3 == 0:
            output += ones[digit] + " hundred "
        elif i % 4 == 0:
            output += ones[digit] + " thousand "
        elif i % 5 == 0:
            if digit == 1 and int(userInput[-i+1]) > 0:
                output += teens[int(userInput[-i+1])] + " thousand "
                i -= 2
                continue
            output += tens[digit]
        elif i % 7 == 0:
            output += ones[digit] + " million "
        else:
            if i % 2 == 1:
                if int(userInput[-i-1]) == 0:
                    output += "and "
                output += f"{ones[digit]} "
            else:
                if digit == 1 and int(userInput[-i+1]) > 0:
                    output += f"and {teens[int(userInput[-i+1])]} "
                    i -= 2
                    continue
                else:
                    output += f"and {tens[digit]} "
    
    i -= 1 
print(output.capitalize())

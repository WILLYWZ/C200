#Get inputs for windchill

Ta = float(input("Enter Farenhait Temperature: "))

V = float(input("Enter wind speed mph: "))

#Complete the rest of program

Twc = 34.74 + 0.6215 * Ta- 35.75 * V**0.16 + 0.4275 * Ta * V**0.16

print("The windchill for ",Ta, " deg and ", V, "mph is ", Twc, "deg")

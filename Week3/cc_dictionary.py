

inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}
def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
    print(total_inches)



snow_Thursday = input("How many snow fell on Thursday: ")
snow_Thursday = int(snow_Thursday)
inches_snow["Thursday"] = snow_Thursday
print_total_snowfall(inches_snow)



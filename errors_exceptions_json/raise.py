def calc_bmi():
    hegiht=float(input("your height please"))
    weight=int(input("your weight please? "))

    if(hegiht>3):
        raise ValueError("Human height should not be so big")
    if(weight>250):
        raise ValueError("Weight is unreasonable")


try:
    calc_bmi()
except ValueError as err_msg:
    print(err_msg)
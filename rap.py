
def speed_of_drivers(speed):
    if speed < 70:
        print("ok")
    elif speed > 70:
        speed = input("speed: ")
        k = (int(speed)-70)/5
        print(k)
        if k > 12:
            print("licence suspended")


speed_of_drivers(1000)

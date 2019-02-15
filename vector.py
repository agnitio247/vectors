from math import *
import sys

class Vector:
    def __init__(self, norm, angle):
        self.norm = norm
        self.angle = angle

    def GetVx(self):
        return self.norm * cos(radians(self.angle))

    def GetVy(self):
        return self.norm * sin(radians(self.angle))

    def GetCad(self):
        if self.angle <= 90:
            return 1
        elif self.angle > 90 and self.angle <= 180:
            return 2
        elif self.angle > 180 and self.angle <= 270:
            return 3
        else:
            return 4

    def GetAlpha(self):
        return degrees(atan(abs(self.GetVy()/self.GetVx())))

    def __add__(self, vector):
        Vx = self.GetVx() + vector.GetVx()
        Vy = self.GetVy() + vector.GetVy()
        R = sqrt(Vx**2 + Vy**2).real
        alpha = degrees(atan(abs(Vy/Vx)))
        angle = 0
        if self.norm >= vector.norm:
            if self.GetCad() == 1:
                angle = alpha
            elif self.GetCad() == 2:
                angle = 180 - alpha
            elif self.GetCad() == 3:
                angle = 180 + alpha
            else:
                angle = 360 - alpha
        elif self.norm < vector.norm:
            if vector.GetCad() == 1:
                angle = alpha
            elif vector.GetCad() == 2:
                angle = 180 - alpha
            elif vector.GetCad() == 3:
                angle = 180 + alpha
            else:
                angle = 360 - alpha
        return Vector(R, angle)

    def Info(self):
        return str(self) + ":\nx: " + str(round(self.GetVx(), 2)) + "\ny: " + str(round(self.GetVy(), 2)) + "\nCad: " + str(self.GetCad()) + "\nAlpha: " + str(round(self.GetAlpha(), 2)) + "\n"

    def __str__(self):
        return(str(round(self.norm, 2)) + " at " + str(round(self.angle, 2)) + " degrees")

def add():
    if len(sys.argv) > 1:
        R = Vector(0, 0)
        arg = 2
        while arg < len(sys.argv):
            R = R + Vector(int(sys.argv[arg].split(";")[0]), int(sys.argv[arg].split(";")[1]))
            arg += 1
        print(str(R))
    else:
        R = Vector(0, 0)
        while True:
            vector = input("Add > ")
            if vector == "=":
                print("\n" + R.Info())
                break
            else:
                R = R + Vector(int(vector.split(";")[0]), int(vector.split(";")[1]))

def NO(x, y):
    v = sqrt(x**2 + y**2).real
    alpha = degrees(atan(abs(y/x)))
    if x > 0 and y > 0:
        angle = alpha
    elif x < 0 and y > 0:
        angle = 180 - alpha
    elif x < 0 and y < 0:
        angle = 180 + alpha
    else:
        angle = 360 - alpha
    return Vector(v, angle)

def mainInput():
    print(
    """
****************************************
Vector Calculator
****************************************
What do you want to do?""")
    while True:
        print(
        """---------------------------------------
1- Add vectors                         |
2- Get info                            |
3- Convert to magnitude and direction  |
4- Exit                                |
---------------------------------------
        """
        )
        cmd = input("1/2/3/4 > ")
        if cmd == "1":
            print("\nAdd vectors (magnitude;direction \"=\" when done)\n")
            add()
            continue
        elif cmd == "2":
            print("\nenter vector info:\n(magnitude;direction)\n")
            info = input("> ")
            print("\n" + Vector(float(info.split(";")[0]), float(info.split(";")[1])).Info())
            continue
        elif cmd == "3":
            print("\n" + NO(float(input("x > ")), float(input("y > "))).Info())
        elif cmd == "4":
            break
        else:
            print("Invalid input")
            continue

def mainArgs():
    if sys.argv[1] == "-a":
        add()
    elif sys.argv[1] == "-i":
        print("\n" + Vector(float(sys.argv[2].split(";")[0]), float(sys.argv[2].split(";")[1])).Info())
    elif sys.argv[1] == "-c":
        print("\n" + NO(float(sys.argv[2]), float(sys.argv[3])).Info())
    else:
        print("Invalid input")

def main():
    if len(sys.argv) > 1:
        try:
            mainArgs()
        except Exception as e:
            print("Error: " + str(e))
            main()
    else:
        try:
            mainInput()
        except Exception as e:
            print("Error: " + str(e))
            main()

if __name__ == '__main__':
    main()

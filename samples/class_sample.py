# Function
def function_name(arguments):
    # do something
    return


class Day:

    def __init__(self):
        self.status = 0

    def start_work(self):
        self.status = 1

    def end_day(self):
        self.status = 0

# Class
class Point3d:

    def __init__(self, X=0, Y=0, Z=0):
        self.X = X
        self.Y = Y
        self.Z = Z

    def get_string(self):
        return f"({self.X}, {self.Y}, {self.Z})"

print()    
today = Day()
print()
print(today.status)
print()
today.start_work()
print()
print(today.status)
print()
today.end_day()
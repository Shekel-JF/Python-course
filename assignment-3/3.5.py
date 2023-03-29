class Bug:
    count = 0

    def __init__(self):
        Bug.count += 1
        self.id = Bug.count

    def __del__(self):
        print("Koniec: " + str(Bug.count) + " ID: " + str(self.id))
        Bug.count -= 1
        del self

    def __str__(self):
        return "Licznik: " + str(Bug.count) + " ID: " + str(self.id)


bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])

print()
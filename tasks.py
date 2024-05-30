class Task():
    def __init__(self, name, descr, date, state = 'New'):
        self.name = name
        self.descr = descr
        self.date = date
        self.state = 'New'

    def Done(self):
        self.state = "Done"

    def Show(self):
        print (self.name)
        print(self.descr)
        print(self.date)
        print(self.state)

tasks = []

tasks.append(Task("1. Today", "Walk into the park", "01-05-2024"))
tasks.append(Task("2. Today Tonight", "Watch TV", "02-05-2024"))

for tt in tasks:
    tt.Show()
print("")
print("Done 0")
tasks[0].Done()

print("")
print("New tasks:")
for tt in tasks:
    if tt.state == "New":
        tt.Show()



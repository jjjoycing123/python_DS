class HashClass:
    def __init__(self, size):
        self.data = [None] * size

    def getData(self):
        return self.data

    def setValue(self, key, value):
        index = self.hash(key)
        self.data[index] = value

    def getValue(self, key):
        index = self.hash(key)
        return self.data[index]

    def hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.getData())
        return hash


temp = HashClass(50)
temp.setValue("grapes", 10000)
temp.setValue("grapess", 7)
print(temp.getValue("grapes"))
print(temp.getValue("grapes"))
print(temp.getValue("grapess"))

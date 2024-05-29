class Store():

    def __init__(self, name = 'Alfa', address = 'Big Ben 1', items = {}):
        self.name = name
        self.address = address
        self.items = items

    def new_item(self,item):
        self.items |= item

    def sub_item(self, item_key):
        if item_key in self.items:
            self.items.pop(item_key)

    def get_price(self,item_key):
        if item_key in self.items:
            return (self.items[item_key])
        else:
            return None


    def set_price(self,item_key, val ):
        self.items[item_key] = val
        return (self.items[item_key])

    def show(self):
        print(f"Name:    {self.name}")
        print(f"Address:    {self.address}")
        print("Товары:")
        print(self.items)


items = {
    'apple': 0.5,
    'meat': 2.75,
    'milk': 1.33,
    'onion': 0.25
}
items2 = {
    'coffee': 1.5,
    'tea': 0.75
}

store1 = Store('Ramstor', 'City 10', items)
store2 = Store('Metro', 'Moscow, Sadovaya 15', items | {'potato' :3} | {'vater':2.01})
store3 = Store('Perekrestok', 'SPb, Liteynaya 8', items2)

store3.show()
print("")
store2.show()
print("")
store1.show()
print("")
print("Add new item")
store1.new_item({'bananas': 1.2})
print (store1.items)
print("")
print("Remove apple")
store1.sub_item('apple')
print (store1.items)
print("")
print(store1.get_price('ggg'))
print("")
print('onion (old price)= ' + f'{store1.get_price("onion")}')
store1.set_price('onion', 50)
print('onion (new price)= ' + f'{store1.get_price("onion")}')



# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

#automate the boring stuff
#chapter 5 - dictionaries and structuring data
#fantasy game inventory


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


#defines the displayInventory function
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(str(count) + " " + item)
        item_total += count
    print("Total number of items: " + str(item_total))


#calls displayInventory function on stuff
displayInventory(stuff)
        

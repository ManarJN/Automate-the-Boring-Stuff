#automate the boring stuff
#chapter 5 - dictionaries and structuring data
#fantasy game inventory - program that prints and edits a given inventory list


#defines function that lists items in an inventory and their amounts
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(str(count) + " " + item)
        item_total += count
    print("Total number of items: " + str(item_total))


#calls displayInventory function on stuff
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)


#separates projects' outputs with an empty line
print()


#defines function that adds a list of items to an inventory
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return(inventory)

#calls addtoInventory function on inv and dragonLoot
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
    

#automate the boring stuff
#chapter 4 - lists
#comma code - program that adds commas between a given list of items


#prompts user to enter individual items
userItemList = []
print('Please add more than 2 items.')
while True:
    print('Enter item ' + str(len(userItemList) + 1) + ' (Or enter nothing to stop.):')
    userItem = input()
    if userItem == '':
        break
    userItemList += [userItem]
    

#defines sentence function
def sentence(itemList):
    sentence = ""
    for item in itemList[:-1]:  #combines all items except last
        sentence += item + ', '
    sentence += 'and ' + itemList[-1]  #appends last item
    print(sentence)


#calls sentence function on userItemList
sentence(userItemList)




####################################################
# NOTE: did not account for lists with <= 2 items. #
####################################################

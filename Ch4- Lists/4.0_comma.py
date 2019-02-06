#automate the boring stuff
#chapter 4 - lists
#comma code


#prompts user to enter individual items
user_item_list = []
print('Please add more than 2 items.')
while True:
    print('Enter item ' + str(len(user_item_list) + 1) + ' (Or enter nothing to stop.):')
    user_item = input()
    if user_item == '':
        break
    user_item_list += [user_item]
    

#defines sentence function
def sentence(item_list):
    sentence = ""
    for item in item_list[:-1]:  #combines all items except last
        sentence += item + ', '
    sentence += 'and ' + item_list[-1]  #appends last item
    print(sentence)


#calls sentence function on entry
sentence(user_item_list)




####################################################
# NOTE: did not account for lists with <= 2 items. #
####################################################

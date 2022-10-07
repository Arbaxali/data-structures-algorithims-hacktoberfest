game_list=[0,1,2]

def display(game_list):
    print("Here is the current list: ")
    print(game_list)


def pos():

    choice="wrong"

    while choice not in ['0','1','2']:
        choie=input("Pick a pos (0,1,2): ")

        if choie not in ['0','1','2']:
            print("sorry!")
    return int(choie)
def game_on():

    choice="wrong"

    while choice not in ['Y','N']:
        choie=input("Keep playing ( Y or N) ")

        if choie not in ['Y','N']:
            print("sorry!")

    if choie=="Y":
        return True
    else:
        return False




def replace(game_list,pos):
    user_replacement=input("Type a string to place at pos: ")
    game_list[pos]=user_replacement
    return game_list



game_on()

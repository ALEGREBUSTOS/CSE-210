


def main():
    position=[0,1,2,3,4,5,6,7,8,9]
    choose = int(input("In the bellow table choose one number between 0 at 8: "))
    X_or_O = input("Enter X or O: ")
    while not (has_winner(position) or table(position,choose,X_or_O)):
        choose = int(input("choose one number between 0 at 8, in the bellow table: "))
        X_or_O = input("Enter X or O: ")
        table(position,choose,X_or_O)
    


def table(position, choose, string):


        print(f'{position[0]} | {position[1]} | {position[2]}') 
        print(f'{position[3]} | {position[4]} | {position[5]}')
        print(f'{position[6]} | {position[7]} | {position[8]}')

        for element in position:
            if choose == element:
                position.insert(choose, string)
        
                
def has_winner(position):
    return (position[0] == position[1] == position[2] or
            position[3] == position[4] == position[5] or
            position[6] == position[7] == position[8] or
            position[0] == position[3] == position[6] or
            position[1] == position[4] == position[7] or
            position[2] == position[5] == position[8] or
            position[0] == position[4] == position[8] or
            position[2] == position[4] == position[6])

               
if __name__ == "__main__":
    main()
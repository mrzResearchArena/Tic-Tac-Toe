import random

g = [1, 2, 3, 4, 5, 6, 7, 8, 9]

winHuman = 0
winComputer = 0

drawHuman = 0
drawComputer = 0


def show():
    print('-------------------')
    print('|  {}  |  {}  |  {}  |'.format(g[0], g[1], g[2]))
    print('-------------------')

    print('|  {}  |  {}  |  {}  |'.format(g[3], g[4], g[5]))
    print('-------------------')

    print('|  {}  |  {}  |  {}  |'.format(g[6], g[7], g[8]))
    print('-------------------')


def verdict(pin):
    if g[0] == pin and g[1] == pin and g[2] == pin:
        return True
    elif g[3] == pin and g[4] == pin and g[5] == pin:
        return True
    elif g[6] == pin and g[7] == pin and g[8] == pin:
        return True
    elif g[0] == pin and g[3] == pin and g[6] == pin:
        return True
    elif g[1] == pin and g[4] == pin and g[7] == pin:
        return True
    elif g[2] == pin and g[5] == pin and g[8] == pin:
        return True
    elif g[0] == pin and g[4] == pin and g[8] == pin:
        return True
    elif g[2] == pin and g[4] == pin and g[6] == pin:
        return True
    else:
        False


def draw():
    C = 0
    i = 0
    while i < 9:
        if g[i] == 'x' or g[i] == 'o': C += 1
        i = i + 1
    # print(C)
    if C == 9:
        return 'Draw'
    else:
        return 'NOT Draw'


def intelligentNumberGenerate():
    # return int(random.uniform(0, 9)) :) Randomly Generation

    # ------------------------ Attack ------------------- #

    # for row-1:
    if g[1] == 'o' and g[2] == 'o' and g[0] != 'x':
        return 0
    elif g[0] == 'o' and g[2] == 'o' and g[1] != 'x':
        return 1
    elif g[0] == 'o' and g[1] == 'o' and g[2] != 'x':
        return 2

    # for row-2:
    elif g[4] == 'o' and g[5] == 'o' and g[3] != 'x':
        return 3
    elif g[3] == 'o' and g[5] == 'o' and g[4] != 'x':
        return 4
    elif g[3] == 'o' and g[4] == 'o' and g[5] != 'x':
        return 5

    # for row-3:
    elif g[7] == 'o' and g[8] == 'o' and g[6] != 'x':
        return 6
    elif g[6] == 'o' and g[8] == 'o' and g[7] != 'x':
        return 7
    elif g[6] == 'o' and g[7] == 'o' and g[8] != 'x':
        return 8

    # for column-1:
    elif g[3] == 'o' and g[6] == 'o' and g[0] != 'x':
        return 0
    elif g[0] == 'o' and g[6] == 'o' and g[3] != 'x':
        return 3
    elif g[0] == 'o' and g[3] == 'o' and g[6] != 'x':
        return 6

    # for column-2:
    elif g[4] == 'o' and g[7] == 'o' and g[1] != 'x':
        return 1
    elif g[1] == 'o' and g[7] == 'o' and g[4] != 'x':
        return 4
    elif g[1] == 'o' and g[4] == 'o' and g[7] != 'x':
        return 7

    # for column-3:
    elif g[5] == 'o' and g[8] == 'o' and g[2] != 'x':
        return 2
    elif g[2] == 'o' and g[8] == 'o' and g[5] != 'x':
        return 5
    elif g[2] == 'o' and g[5] == 'o' and g[8] != 'x':
        return 8

    # for diagonal-1:
    elif g[4] == 'o' and g[8] == 'o' and g[0] != 'x':
        return 0
    elif g[0] == 'o' and g[8] == 'o' and g[4] != 'x':
        return 4
    elif g[0] == 'o' and g[4] == 'o' and g[8] != 'x':
        return 8

    # for diagonal-2:
    elif g[4] == 'o' and g[6] == 'o' and g[2] != 'x':
        return 2
    elif g[2] == 'o' and g[6] == 'o' and g[4] != 'x':
        return 4
    elif g[2] == 'o' and g[4] == 'o' and g[6] != 'x':
        return 6

    # Defence
    # for row-1:
    elif g[1] == 'x' and g[2] == 'x' and g[0] != 'o': return 0
    elif g[0] == 'x' and g[2] == 'x' and g[1] != 'o': return 1
    elif g[0] == 'x' and g[1] == 'x' and g[2] != 'o': return 2

    # for row-2:
    elif g[4] == 'x' and g[5] == 'x' and g[3] != 'o': return 3
    elif g[3] == 'x' and g[5] == 'x' and g[4] != 'o': return 4
    elif g[3] == 'x' and g[4] == 'x' and g[5] != 'o': return 5

    # for row-3:
    elif g[7] == 'x' and g[8] == 'x' and g[6] != 'o': return 6
    elif g[6] == 'x' and g[8] == 'x' and g[7] != 'o': return 7
    elif g[6] == 'x' and g[7] == 'x' and g[8] != 'o': return 8

    # for column-1:
    elif g[3] == 'x' and g[6] == 'x' and g[0] != 'o': return 0
    elif g[0] == 'x' and g[6] == 'x' and g[3] != 'o': return 3
    elif g[0] == 'x' and g[3] == 'x' and g[6] != 'o': return 6

    # for column-2:
    elif g[4] == 'x' and g[7] == 'x' and g[1] != 'o': return 1
    elif g[1] == 'x' and g[7] == 'x' and g[4] != 'o': return 4
    elif g[1] == 'x' and g[4] == 'x' and g[7] != 'o': return 7


    # for column-3:
    elif g[5] == 'x' and g[8] == 'x' and g[2] != 'o': return 2
    elif g[2] == 'x' and g[8] == 'x' and g[5] != 'o': return 5
    elif g[2] == 'x' and g[5] == 'x' and g[8] != 'o': return 8


    # for diagonal-1:
    elif g[4] == 'x' and g[8] == 'x' and g[0] != 'o': return 0
    elif g[0] == 'x' and g[8] == 'x' and g[4] != 'o': return 4
    elif g[0] == 'x' and g[4] == 'x' and g[8] != 'o': return 8


    # for diagonal-2:
    elif g[4] == 'x' and g[6] == 'x' and g[2] != 'o': return 2
    elif g[2] == 'x' and g[6] == 'x' and g[4] != 'o': return 4
    elif g[2] == 'x' and g[4] == 'x' and g[6] != 'o': return 6


    else: return -1

def humanTurn():

    print('Turn for human x:')
    while True:

        num = int(input()) - 1
        if 0 <= num <= 8:
            if g[num] == 'x' or g[num] == 'o':
                print('Please, human input again')
            else:
                g[num] = 'x'
                break
        else:
            print('You press wrong key, please, human input again.')

    if verdict('x'):
        global winHuman; winHuman += 1
        print('--- Human WIN ---')
        return False

    else:
        if draw() == 'Draw':
            global drawHuman; drawHuman += 1
            global drawComputer; drawComputer += 1
            print('--- Match Drawn ---')
            return False

    show()
    return True

def computerTurn():
    print('Turn for computer o:')
    import time
    time.sleep(5)
    while True:
        random.seed()
        numberGenerate = intelligentNumberGenerate()
        # print(numberGenerate)

        if numberGenerate != -1:
            # if g[numberGenerate] == 'x' or g[numberGenerate] == 'o': None
            # else:
            g[numberGenerate] = 'o'
            break

        else:
            # while True:
            #     numberGenerate = int(random.uniform(0, 9))
            #     if g[numberGenerate] == 'x' or g[numberGenerate] == 'o':
            #         None
            #     else:
            #         g[numberGenerate] = 'o'
            #         break
            # break
            successAssigned = False

            from random import shuffle
            items = [0, 2, 6, 8]
            shuffle(items)

            for i in items:
                if g[i] == 'x' or g[i] == 'o': None
                else:
                    g[i] = 'o'
                    successAssigned = True
                    break

            while not successAssigned:
                numberGenerate = int(random.uniform(0, 9))
                if g[numberGenerate] == 'x' or g[numberGenerate] == 'o':
                    None
                else:
                    g[numberGenerate] = 'o'
                    break
            break

    if verdict('o'):
        global winComputer; winComputer += 1
        print('--- Computer WIN ---')
        return False

    else:
        if draw() == 'Draw':

            global drawComputer; drawComputer += 1
            global drawHuman; drawHuman += 1
            print('--- Match Drawn ---')
            return False
    show()
    return True

def summary(n):

    pointsComputer = winComputer*4 + drawComputer*2
    pointsHuman =  winHuman*4 + drawHuman*2

    if pointsComputer>pointsHuman:
        print('Finally Computer WIN.')
    else:
        if pointsComputer < pointsHuman:
            print('Finally Human WIN.')
        else:
            print('Scores are label.')

    print()
    print('______________ Summary ______________')
    print()
    print('Total games is {}.'.format(n))
    print('-------------------------------------')
    print('Players  | Win | Lost | Draw | Points')
    print('-------------------------------------')
    print('Human    |  {}  |  {}   |  {}   |  {}'.format(winHuman, (n-winHuman-drawHuman), drawHuman, pointsHuman))
    print('-------------------------------------')
    print('Computer |  {}  |  {}   |  {}   |  {}'.format(winComputer, (n-winComputer-drawComputer), drawComputer, pointsComputer))
    print('-------------------------------------')


def main():
    show()

    print('How many times you wanna play?')
    totalGames = int(input())
    for _ in range(totalGames):
        print('Games #{}:'.format(_+1))
        show()

        ensure = True

        if _ % 2 == 0:
            while ensure:
                if ensure:
                    ensure = humanTurn()
                if ensure:
                    ensure = computerTurn()
        else:
            while ensure:
                if ensure:
                    ensure = computerTurn()
                if ensure:
                    ensure = humanTurn()

        print()
        print("--- Current Senerio ---")
        print()
        show()
        for i in range(1, 10):
            g[i-1] = i

    summary(totalGames)


if __name__ == '__main__':
    main()
    # show()
    # # g[0] = 'o'
    # show()
    # if g[0] == 'x' or g[0] == 'o': None
    # else: g[0] = 'o'
    #
    # show()
    # for i in (0, 2, 4, 8):
    #     print(i)
    # import this

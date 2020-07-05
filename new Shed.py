from __future__ import division
from __future__ import print_function
import pygame, sys, os
from pygame.locals import *
import random
import threading



class MouseThread(threading.Thread):

    def __init__(self, ID):
        threading.Thread.__init__(self)
        self.ID = ID
        self.state = 0

    def run(self):
        global direction
        global threadnumber
        global deck
        global playanother
        global firstplayedcard
        global gameon
        global turnnumber
        global players
        global pickup
        global gamestart
        global playedcards
        global nextplayerturn
        while gameon:
            clock.tick(20)
            if self.ID == 1:
                mousepos = pygame.mouse.get_pos()
                self.ID = 0
                if nextplayerturn:
                    if len(players[turnnumber].handcards) == len(players[turnnumber].hiddencards) == 0:
                        print(players[turnnumber].name + ' won')
                        del players[turnnumber]
                        if not direction:
                            turnnumber -= 1
                            if turnnumber == -1:
                                turnnumber = len(players) - 1
                        elif turnnumber >= len(players):
                            turnnumber = 0
                        if len(players) == 1:
                            gamestart = 4
                    else:
                        nextplayerturn = False
                        firstplayedcard = False
                        playanother = False
                        if gamestart == 3:
                            players[turnnumber].handcards += players[turnnumber].frontrowcards
                            players[turnnumber].frontrowcards = []
                            players[turnnumber].handcards.sort()
                elif gamestart == 2:
                    if pickup and not firstplayedcard:
                        print(players[turnnumber].name + ' picked up')
                        pickup = False
                        players[turnnumber].handcards += playedcards
                        players[turnnumber].handcards.sort()
                        playedcards = []
                        nextplayerturn = True
                        if direction:
                            turnnumber += 1
                            if turnnumber == len(players):
                                turnnumber = 0
                        else:
                            turnnumber -= 1
                            if turnnumber == -1:
                                turnnumber = len(players) - 1
                    elif len(players[turnnumber].handcards):
                        if 400 < mousepos[1] < 456:
                            xpos = mousepos[0] - 130
                            if 0 < xpos < 20 * len(players[turnnumber].handcards):
                                if Is_Playable(players[turnnumber].handcards[int(xpos / 20)]):
                                    print(players[turnnumber].name + ' played ' + players[turnnumber].handcards[int(xpos / 20)])
                                    playedcards.append(players[turnnumber].handcards[int(xpos / 20)])
                                    firstplayedcard = True
                                    playanother = False
                                    if playedcards[-1][0:2] == '10':
                                        playedcards = []
                                        if len(players[turnnumber].handcards) != 0 or len(players[turnnumber].hiddencards) != 0:
                                            firstplayedcard = False
                                    elif playedcards[-1][0:2] == '15':
                                        if direction:
                                            direction = False
                                        else:
                                            direction = True
                                    del players[turnnumber].handcards[int(xpos / 20)]
                                    try:
                                        if playedcards[-1][0] == '1':
                                            if playedcards[-1][1] == '5' and playedcards[-2][1] == '5':
                                                playedcards = []
                                                if len(players[turnnumber].handcards) != 0 or len(players[turnnumber].hiddencards) != 0:
                                                    firstplayedcard = False
                                            elif playedcards[-1][1] == playedcards[-2][1] == playedcards[-3][1] == playedcards[-4][1]:
                                                playedcards = []
                                                if len(players[turnnumber].handcards) != 0 or len(players[turnnumber].hiddencards) != 0:
                                                    firstplayedcard = False
                                        elif playedcards[-1][0] == playedcards[-2][0] == playedcards[-3][0] == playedcards[-4][0]:
                                            playedcards = []
                                            if len(players[turnnumber].handcards) != 0 or len(players[turnnumber].hiddencards) != 0:
                                                firstplayedcard = False
                                    except Exception:
                                        pass

                                    if not playanother and firstplayedcard:
                                        if len(players[turnnumber].handcards):
                                            for x in players[turnnumber].handcards:
                                                if Is_Playable(x):
                                                    playanother = True

                                        elif len(players[turnnumber].frontrowcards):
                                            for x in players[turnnumber].frontrowcards:
                                                if Is_Playable(x):
                                                    playanother = True

                                    if not playanother and firstplayedcard:
                                        if len(deck):
                                            cardsperplayer = int(54 / len(order))
                                            while cardsperplayer / 3 != int(cardsperplayer / 3):
                                                cardsperplayer -= 1

                                            while len(players[turnnumber].handcards) < cardsperplayer / 3 and len(deck):
                                                players[turnnumber].handcards.append(deck[0])
                                                del deck[0]

                                        nextplayerturn = True
                                        if direction:
                                            turnnumber += 1
                                            if turnnumber == len(players):
                                                turnnumber = 0
                                        else:
                                            turnnumber -= 1
                                            if turnnumber == -1:
                                                turnnumber = len(players) - 1
                            elif playanother:
                                playanother = False
                                if len(deck):
                                    players[turnnumber].handcards.append(deck[0])
                                    del deck[0]
                                nextplayerturn = True
                                if direction:
                                    turnnumber += 1
                                    if turnnumber == len(players):
                                        turnnumber = 0
                                else:
                                    turnnumber -= 1
                                    if turnnumber == -1:
                                        turnnumber = len(players) - 1
                        elif playanother:
                            playanother = False
                            if len(deck):
                                players[turnnumber].handcards.append(deck[0])
                                del deck[0]
                            nextplayerturn = True
                            if direction:
                                turnnumber += 1
                                if turnnumber == len(players):
                                    turnnumber = 0
                            else:
                                turnnumber -= 1
                                if turnnumber == -1:
                                    turnnumber = len(players) - 1
                    elif len(players[turnnumber].frontrowcards):
                        if 400 < mousepos[1] < 456:
                            xpos = mousepos[0] - 130
                            if 0 < xpos < 20 * len(players[turnnumber].frontrowcards):
                                if Is_Playable(players[turnnumber].frontrowcards[int(xpos / 20)]):
                                    print(players[turnnumber].name + ' played ' + players[turnnumber].frontrowcards[int(xpos / 20)])
                                    playedcards.append(players[turnnumber].frontrowcards[int(xpos / 20)])
                                    firstplayedcard = True
                                    playanother = False
                                    if playedcards[-1][0:2] == '10':
                                        playedcards = []
                                        firstplayedcard = False
                                    elif playedcards[-1][0:2] == '15':
                                        if direction:
                                            direction = False
                                        else:
                                            direction = True
                                    del players[turnnumber].frontrowcards[int(xpos / 20)]
                                    try:
                                        if playedcards[-1][0] == '1':
                                            if playedcards[-1][1] == '5' and playedcards[-2][1] == '5':
                                                playedcards = []
                                                if len(players[turnnumber].handcards) != 0 or len(players[turnnumber].hiddencards) != 0:
                                                    firstplayedcard = False
                                            elif playedcards[-1][1] == playedcards[-2][1] == playedcards[-3][1] == playedcards[-4][1]:
                                                playedcards = []
                                                if len(players[turnnumber].handcards) != 0 or len(players[turnnumber].hiddencards) != 0:
                                                    firstplayedcard = False
                                        elif playedcards[-1][0] == playedcards[-2][0] == playedcards[-3][0] == playedcards[-4][0]:
                                            playedcards = []
                                            if len(players[turnnumber].handcards) != 0 or len(players[turnnumber].hiddencards) != 0:
                                                firstplayedcard = False
                                    except Exception:
                                        pass

                                    if not playanother and firstplayedcard:
                                        if len(players[turnnumber].frontrowcards):
                                            for x in players[turnnumber].frontrowcards:
                                                if Is_Playable(x):
                                                    playanother = True

                                    if not playanother and firstplayedcard:
                                        nextplayerturn = True
                                        if direction:
                                            turnnumber += 1
                                            if turnnumber == len(players):
                                                turnnumber = 0
                                        else:
                                            turnnumber -= 1
                                            if turnnumber == -1:
                                                turnnumber = len(players) - 1
                                elif not firstplayedcard:
                                    pickup = True
                                    for x in players[turnnumber].frontrowcards:
                                        if Is_Playable(x):
                                            pickup = False

                                    if pickup:
                                        playedcards.append(players[turnnumber].frontrowcards[int(xpos / 20)])
                                        del players[turnnumber].frontrowcards[int(xpos / 20)]
                            elif playanother:
                                playanother = False
                                nextplayerturn = True
                                if direction:
                                    turnnumber += 1
                                    if turnnumber == len(players):
                                        turnnumber = 0
                                else:
                                    turnnumber -= 1
                                    if turnnumber == -1:
                                        turnnumber = len(players) - 1
                        elif playanother:
                            playanother = False
                            nextplayerturn = True
                            if direction:
                                turnnumber += 1
                                if turnnumber == len(players):
                                    turnnumber = 0
                            else:
                                turnnumber -= 1
                                if turnnumber == -1:
                                    turnnumber = len(players) - 1
                    elif 400 < mousepos[1] < 456:
                        xpos = mousepos[0] - 130
                        if 0 < xpos < 20 * len(players[turnnumber].hiddencards):
                            if Is_Playable(players[turnnumber].hiddencards[int(xpos / 20)]):
                                print(players[turnnumber].name + ' played ' + players[turnnumber].hiddencards[int(xpos / 20)])
                                playedcards.append(players[turnnumber].hiddencards[int(xpos / 20)])
                                firstplayedcard = True
                                if playedcards[-1][0:2] == '10':
                                    playedcards = []
                                    if len(players[turnnumber].handcards) != 0 or len(players[turnnumber].hiddencards) != 0:
                                        firstplayedcard = False
                                elif playedcards[-1][0:2] == '15':
                                    if direction:
                                        direction = False
                                    else:
                                        direction = True
                                del players[turnnumber].hiddencards[int(xpos / 20)]
                                try:
                                    if playedcards[-1][0] == '1':
                                        if playedcards[-1][1] == '5' and playedcards[-2][1] == '5':
                                            playedcards = []
                                            if len(players[turnnumber].handcards) != 0 or len(players[turnnumber].hiddencards) != 0:
                                                firstplayedcard = False
                                        elif playedcards[-1][1] == playedcards[-2][1] == playedcards[-3][1] == playedcards[-4][1]:
                                            playedcards = []
                                            if len(players[turnnumber].handcards) != 0 or len(players[turnnumber].hiddencards) != 0:
                                                firstplayedcard = False
                                    elif playedcards[-1][0] == playedcards[-2][0] == playedcards[-3][0] == playedcards[-4][0]:
                                        playedcards = []
                                        if len(players[turnnumber].handcards) != 0 or len(players[turnnumber].hiddencards) != 0:
                                            firstplayedcard = False
                                except Exception:
                                    pass

                                if firstplayedcard:
                                    nextplayerturn = True
                                    if direction:
                                        turnnumber += 1
                                        if turnnumber == len(players):
                                            turnnumber = 0
                                    else:
                                        turnnumber -= 1
                                        if turnnumber == -1:
                                            turnnumber = len(players) - 1
                            else:
                                print(players[turnnumber].name + ' played ' + players[turnnumber].hiddencards[int(xpos / 20)])
                                playedcards.append(players[turnnumber].hiddencards[int(xpos / 20)])
                                del players[turnnumber].hiddencards[int(xpos / 20)]
                                pickup = True
                                firstplayedcard = False
                elif gamestart == 3:
                    if 400 < mousepos[1] < 456:
                        xpos = mousepos[0] - 130
                        if 0 < xpos < 20 * len(players[turnnumber].handcards):
                            players[turnnumber].frontrowcards.append(players[turnnumber].handcards[int(xpos / 20)])
                            del players[turnnumber].handcards[int(xpos / 20)]

        threadnumber -= 1


class Player():

    def __init__(self, cards, name):
        self.name = name
        self.AI = False
        self.hiddencards = []
        self.frontrowcards = []
        self.handcards = []
        for x in range(0, int(len(cards) / 3)):
            self.hiddencards.append(cards[x])

        for x in range(int(len(cards) / 3), int(len(cards) * 2 / 3)):
            self.frontrowcards.append(cards[x])

        for x in range(int(len(cards) * 2 / 3), int(len(cards))):
            self.handcards.append(cards[x])


class AIPlayer():

    def __init__(self, cards, name):
        self.AI = True
        self.name = name
        self.hiddencards = []
        self.frontrowcards = []
        self.handcards = []
        for x in range(0, int(len(cards) / 3)):
            self.hiddencards.append(cards[x])

        for x in range(int(len(cards) / 3), int(len(cards) * 2 / 3)):
            self.frontrowcards.append(cards[x])

        for x in range(int(len(cards) * 2 / 3), int(len(cards))):
            self.handcards.append(cards[x])

    def findhighesthand(self, playable):
        flag1 = False
        flag4 = False
        samecards = []
        for x in playable:
            if self.handcards[x][0] == '1' and not self.handcards[x][1] == '5' and not self.handcards[x][1] == '0':
                flag1 = True
            if 3 < int(self.handcards[x][0]):
                flag4 = True

        if flag1:
            highest = 11
            for x in playable:
                if self.handcards[x][0] == '1' and not self.handcards[x][1] == '5' and not self.handcards[x][1] == '0':
                    if highest < int(self.handcards[x][0:2]):
                        highest = int(self.handcards[x][0:2])

        elif flag4:
            highest = 4
            for x in playable:
                if highest < int(self.handcards[x][0]):
                    highest = int(self.handcards[x][0])

        else:
            return [playable[-1]]
        for x in range(0, len(playable)):
            if flag1:
                try:
                    if int(self.handcards[playable[x]][0:2]) == highest:
                        samecards.append(playable[x])
                except Exception:
                    pass

            elif int(self.handcards[playable[x]][0]) == highest:
                samecards.append(playable[x])

        return samecards

    def findlowesthand(self, playable):
        flag1 = False
        flag4 = False
        samecards = []
        for x in playable:
            if self.handcards[x][0] == '1' and not self.handcards[x][1] == '5' and not self.handcards[x][1] == '0':
                flag1 = True
            if 3 < int(self.handcards[x][0]):
                flag4 = True

        if flag4:
            lowest = 9
            for x in playable:
                if self.handcards[x][0] != '1' and self.handcards[x][0] != '2' and self.handcards[x][0] != '3':
                    if lowest > int(self.handcards[x][0]):
                        lowest = int(self.handcards[x][0])

        elif flag1:
            lowest = 14
            for x in playable:
                if self.handcards[x][0] == '1' and not self.handcards[x][1] == '5' and not self.handcards[x][1] == '0':
                    if lowest > int(self.handcards[x][0:2]):
                        lowest = int(self.handcards[x][0:2])

        else:
            return [playable[0]]
        for x in range(0, len(playable)):
            if flag4:
                if int(self.handcards[playable[x]][0]) == lowest:
                    samecards.append(playable[x])
            else:
                try:
                    if int(self.handcards[playable[x]][0:2]) == lowest:
                        samecards.append(playable[x])
                except Exception:
                    pass

        return samecards

    def findhighestfrontrow(self, playable):
        flag1 = False
        flag4 = False
        samecards = []
        for x in playable:
            if self.frontrowcards[x][0] == '1' and not self.frontrowcards[x][1] == '5' and not self.frontrowcards[x][1] == '0':
                flag1 = True
            if 3 < int(self.frontrowcards[x][0]):
                flag4 = True

        if flag1:
            highest = 11
            for x in playable:
                if self.frontrowcards[x][0] == '1' and not self.frontrowcards[x][1] == '5' and not self.frontrowcards[x][1] == '0':
                    if highest < int(self.frontrowcards[x][0:2]):
                        highest = int(self.frontrowcards[x][0:2])

        elif flag4:
            highest = 4
            for x in playable:
                if highest < int(self.frontrowcards[x][0]):
                    highest = int(self.frontrowcards[x][0])

        else:
            return [playable[-1]]
        for x in range(0, len(playable)):
            if flag1:
                try:
                    if int(self.frontrowcards[playable[x]][0:2]) == highest:
                        samecards.append(playable[x])
                except Exception:
                    pass

            elif int(self.frontrowcards[playable[x]][0]) == highest:
                samecards.append(playable[x])

        return samecards

    def findlowestfrontrow(self, playable):
        flag1 = False
        flag4 = False
        samecards = []
        for x in playable:
            if self.frontrowcards[x][0] == '1' and not self.frontrowcards[x][1] == '5' and not self.frontrowcards[x][1] == '0':
                flag1 = True
            if 3 < int(self.frontrowcards[x][0]):
                flag4 = True

        if flag4:
            lowest = 9
            for x in playable:
                if self.frontrowcards[x][0] != '1' and self.frontrowcards[x][0] != '2' and self.frontrowcards[x][0] != '3':
                    if lowest > int(self.frontrowcards[x][0]):
                        lowest = int(self.frontrowcards[x][0])

        elif flag1:
            lowest = 14
            for x in playable:
                if self.frontrowcards[x][0] == '1' and not self.frontrowcards[x][1] == '5' and not self.frontrowcards[x][1] == '0':
                    if lowest > int(self.frontrowcards[x][0:2]):
                        lowest = int(self.frontrowcards[x][0:2])

        else:
            return [playable[0]]
        for x in range(0, len(playable)):
            if flag4:
                if int(self.frontrowcards[playable[x]][0]) == lowest:
                    samecards.append(playable[x])
            else:
                try:
                    if int(self.frontrowcards[playable[x]][0:2]) == lowest:
                        samecards.append(playable[x])
                except Exception:
                    pass

        return samecards

    def playcard(self):
        global direction
        global playedcards
        global firstplayedcard
        handpositions = []
        frontrowpositions = []
        firstplayedcard = False
        playedmorethanone = False
        if len(self.handcards):
            for x in range(0, len(self.handcards)):
                if Is_Playable(self.handcards[x]):
                    firstplayedcard = True
                    handpositions.append(x)

            if not len(handpositions):
                self.handcards += playedcards
                playedcards = []
                print(self.name + ' picked up')
                return True
            if len(handpositions) > 1:
                playedmorethanone = True
            if len(players[(turnnumber + 1) % len(players)].handcards) < 4:
                handpositions2 = self.findhighesthand(handpositions)
            else:
                handpositions2 = self.findlowesthand(handpositions)
            handpositions2.reverse()
            for y in handpositions2:
                playedcards.append(self.handcards[y])
                print(self.name + ' played ' + playedcards[-1])
                del self.handcards[y]

            if len(deck):
                cardsperplayer = int(54 / len(order))
                while cardsperplayer / 3 != int(cardsperplayer / 3):
                    cardsperplayer -= 1

                while len(self.handcards) < cardsperplayer / 3 and len(deck):
                    self.handcards.append(deck[0])
                    del deck[0]

            if not len(self.handcards):
                for x in range(0, len(self.frontrowcards)):
                    if Is_Playable(self.frontrowcards[x]):
                        frontrowpositions.append[x]

                if not len(frontrowpositions):
                    return True
                playedmorethanone = True
                frontrowpositions.reverse()
                for y in frontrowpositions:
                    playedcards.append(self.frontrowcards[y])
                    print('AI played ' + playedcards[-1])
                    del self.frontrowcards[y]

            if playedcards[-1][0:2] == '10':
                playedcards = []
                if len(self.handcards) or len(self.hiddencards):
                    self.playcard()
                return True
            if playedcards[-1][0:2] == '15' and not playedmorethanone:
                if direction:
                    direction = False
                else:
                    direction = True
            try:
                if playedcards[-1][0] == '1':
                    if playedcards[-1][1] == '5' and playedcards[-2][1] == '5':
                        playedcards = []
                        if len(self.handcards) or len(self.hiddencards):
                            self.playcard()
                        return True
                    elif playedcards[-1][1] == playedcards[-2][1] == playedcards[-3][1] == playedcards[-4][1]:
                        playedcards = []
                        if len(self.handcards) or len(self.hiddencards):
                            self.playcard()
                        return True
                elif playedcards[-1][0] == playedcards[-2][0] == playedcards[-3][0] == playedcards[-4][0]:
                    playedcards = []
                    if len(self.handcards) or len(self.hiddencards):
                        self.playcard()
                    return True
            except Exception:
                pass

        elif len(self.frontrowcards):
            for x in range(0, len(self.frontrowcards)):
                if Is_Playable(self.frontrowcards[x]):
                    firstplayedcard = True
                    frontrowpositions.append(x)

            if not len(frontrowpositions):
                self.handcards += playedcards
                playedcards = []
                print(self.name + ' picked up along with ' + self.frontrowcards[-1])
                self.handcards.append(self.frontrowcards[-1])
                del self.frontrowcards[-1]
                return True
            if len(frontrowpositions) > 1:
                playedmorethanone = True
            if len(players[(turnnumber + 1) % len(players)].frontrowcards) < 4:
                frontrowpositions2 = self.findhighestfrontrow(frontrowpositions)
            else:
                frontrowpositions2 = self.findlowestfrontrow(frontrowpositions)
            frontrowpositions2.reverse()
            for y in frontrowpositions2:
                playedcards.append(self.frontrowcards[y])
                print(self.name + ' played ' + playedcards[-1])
                del self.frontrowcards[y]

            if playedcards[-1][0:2] == '10':
                playedcards = []
                if len(self.handcards) or len(self.hiddencards):
                    self.playcard()
                return True
            if playedcards[-1][0:2] == '15' and not playedmorethanone:
                if direction:
                    direction = False
                else:
                    direction = True
            try:
                if playedcards[-1][0] == '1':
                    if playedcards[-1][1] == '5' and playedcards[-2][1] == '5':
                        playedcards = []
                        if len(self.handcards) or len(self.hiddencards):
                            self.playcard()
                        return True
                    elif playedcards[-1][1] == playedcards[-2][1] == playedcards[-3][1] == playedcards[-4][1]:
                        playedcards = []
                        if len(self.handcards) or len(self.hiddencards):
                            self.playcard()
                        return True
                elif playedcards[-1][0] == playedcards[-2][0] == playedcards[-3][0] == playedcards[-4][0]:
                    playedcards = []
                    if len(self.handcards) or len(self.hiddencards):
                        self.playcard()
                    return True
            except Exception:
                pass

        elif Is_Playable(self.hiddencards[0]):
            playedcards.append(self.hiddencards[0])
            del self.hiddencards[0]
            print(self.name + ' played ' + playedcards[-1])
            if playedcards[-1][0:2] == '10':
                playedcards = []
                if len(self.handcards) or len(self.hiddencards):
                    self.playcard()
                return True
            if playedcards[-1][0:2] == '15' and not playedmorethanone:
                if direction:
                    direction = False
                else:
                    direction = True
            try:
                if playedcards[-1][0] == '1':
                    if playedcards[-1][1] == '5' and playedcards[-2][1] == '5':
                        playedcards = []
                        if len(self.handcards) or len(self.hiddencards):
                            self.playcard()
                        return True
                    if playedcards[-1][1] == playedcards[-2][1] == playedcards[-3][1] == playedcards[-4][1]:
                        playedcards = []
                        if len(self.handcards) or len(self.hiddencards):
                            self.playcard()
                        return True
                elif playedcards[-1][0] == playedcards[-2][0] == playedcards[-3][0] == playedcards[-4][0]:
                    playedcards = []
                    if len(self.handcards) or len(self.hiddencards):
                        self.playcard()
                    return True
            except Exception:
                pass

        else:
            playedcards.append(self.hiddencards[0])
            del self.hiddencards[0]
            print(self.name + ' played ' + playedcards[-1] + ' and had to pick up')
            self.handcards += playedcards
            playedcards = []

    def frontrowsort(self):
        self.handcards += self.frontrowcards
        self.frontrowcards = []
        flag3 = True
        flag2 = False
        flag10 = False
        flag15 = False
        flag1 = False
        flag0 = False
        while len(self.frontrowcards) < len(self.handcards):
            flag = True
            for x in range(0, len(self.handcards)):
                if flag and flag3:
                    if self.handcards[x][0] == '3':
                        flag = False
                        self.frontrowcards.append(self.handcards[x])
                        del self.handcards[x]
                if flag and flag2:
                    if self.handcards[x][0] == '2':
                        flag = False
                        self.frontrowcards.append(self.handcards[x])
                        del self.handcards[x]
                if flag and flag10:
                    if self.handcards[x][0:2] == '10':
                        flag = False
                        self.frontrowcards.append(self.handcards[x])
                        del self.handcards[x]
                if flag and flag15:
                    if self.handcards[x][0:2] == '15':
                        flag = False
                        self.frontrowcards.append(self.handcards[x])
                        del self.handcards[x]
                if flag and flag1:
                    if self.handcards[x][0] == '1':
                        flag = False
                        self.frontrowcards.append(self.handcards[x])
                        del self.handcards[x]
                if flag and flag0:
                    flag = False
                    self.frontrowcards.append(self.handcards[-1])
                    del self.handcards[-1]

            if flag and flag3:
                flag3 = False
                flag2 = True
            elif flag and flag2:
                flag2 = False
                flag10 = True
            elif flag and flag10:
                flag10 = False
                flag15 = True
            elif flag and flag15:
                flag15 = False
                flag1 = True
            elif flag and flag1:
                flag1 = False
                flag0 = True


def Is_Playable(card):
    if len(playedcards) == 0:
        return True
    if firstplayedcard:
        if card[0] == '1':
            if playedcards[-1][1] == card[1]:
                return True
        elif card[0] == playedcards[-1][0]:
            return True
        return False
    if card[0] == '2' or card[0] == '3':
        return True
    if card[0:2] == '10':
        return True
    if card[0:2] == '15':
        return True
    topcard = 0
    flag = False
    if playedcards[-1][0] == '3' or playedcards[-1][1] == '5':
        flag = True
        for x in playedcards:
            if x[0] != '3' and x[1] != '5':
                topcard = x

    if flag:
        if topcard == 0:
            return True
        playedcards.append(topcard)
    if playedcards[-1][0] != '1':
        if playedcards[-1][0] == '7':
            if flag:
                del playedcards[-1]
            if card[0] == '1':
                return False
            elif int(card[0]) < 8:
                return True
            else:
                return False
        if card[0] == '1':
            if flag:
                del playedcards[-1]
            return True
        elif int(card[0]) >= int(playedcards[-1][0]):
            if flag:
                del playedcards[-1]
            return True
        else:
            if flag:
                del playedcards[-1]
            return False
    else:
        if card[0] != '1':
            if flag:
                del playedcards[-1]
            return False
        if int(card[1]) >= int(playedcards[-1][1]):
            if flag:
                del playedcards[-1]
            return True
        if flag:
            del playedcards[-1]
        return False
    if flag:
        del playedcards[-1]
    return False


def New_Card_Deck():
    cardnames = []
    for i in range(2, 15):
        cardnames.append(str(i) + 'c')
        cardnames.append(str(i) + 'd')
        cardnames.append(str(i) + 'h')
        cardnames.append(str(i) + 's')

    cardnames.append('15r')
    cardnames.append('15b')
    return cardnames


def Get_Player_Parameters():
    maxplayers = 18
    humanplayers = int(raw_input('How many players?\n> '))
    while humanplayers < 2 or humanplayers > maxplayers:
        humanplayers = int(raw_input('Too many or less than zero. How many players?\n> '))

    playerorder = []
    for x in range(0, humanplayers):
        playerorder.append(raw_input('Who goes in position ' + str(x+1) + "? Type 'AI' for AI player\n> "))

    return playerorder


def Initiate_Players(order, deck, cardsperplayer):
    players = []
    aino = 0
    for x in order:
        if x.upper() == 'AI':
            aino += 1
            players.append(AIPlayer(deck[0:cardsperplayer], 'AI #' + str(aino)))
        else:
            players.append(Player(deck[0:cardsperplayer], x))
        for y in range(0, cardsperplayer):
            del deck[0]

    return players


    
gameon = True
gamestart = 0
rate = 20
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Best shed ever')
turn = 0
clockwise = True
playedcards = []
allcards = New_Card_Deck()
cards = {}
for x in allcards:
    cards[x] = pygame.image.load(os.path.join('graphics', x + '.png')).convert()

background = pygame.image.load(os.path.join('graphics', 'background.png')).convert()
cardback = pygame.image.load(os.path.join('graphics', 'cardback.png')).convert()
threadnumber = 1
mousethread = MouseThread(0)

mousethread.start()
while gameon:
    clock.tick(rate)
    screen.blit(background, (0, 0))
    if gamestart == 1:
        deck = list(allcards)
        random.shuffle(deck)
        cardsperplayer = int(54 / len(order))
        while cardsperplayer / 3 != int(cardsperplayer / 3):
            cardsperplayer -= 1

        players = Initiate_Players(order, deck, cardsperplayer)
        gamestart = 3
        nextplayerturn = True
        turnnumber = 0
        direction = True
        playanother = False
        pickup = False
        playedcards = []
    elif gamestart == 2:
        try:
            for x in range(0, len(players)):
                screen.blit(pygame.font.Font('freesansbold.ttf', 20).render(players[x].name, 0, (255, 255, 255)), (30 + (30 + 20 * int(cardsperplayer / 3)) * x, 5))
                for y in range(0, len(players[x].hiddencards)):
                    screen.blit(cardback, (30 + 20 * y + (30 + 20 * int(cardsperplayer / 3)) * x, 30))

                for y in range(0, len(players[x].frontrowcards)):
                    screen.blit(cards[players[x].frontrowcards[y]], (30 + 20 * y + (30 + 20 * int(cardsperplayer / 3)) * x, 40))

                if len(players[x].handcards):
                    screen.blit(cardback, (30 + (30 + 20 * int(cardsperplayer / 3)) * x, 105))
                    screen.blit(pygame.font.Font('freesansbold.ttf', 20).render(str(len(players[x].handcards)), 0, (255, 255, 255)), (45 + (30 + 20 * int(cardsperplayer / 3)) * x, 125))

            if len(deck):
                screen.blit(pygame.font.Font('freesansbold.ttf', 20).render('Deck: ' + str(len(deck)), 0, (255, 255, 255)), (20, 515))
                screen.blit(cardback, (20, 540))
            if nextplayerturn:
                screen.blit(pygame.font.Font('freesansbold.ttf', 20).render(players[turnnumber].name + "'s turn. Press left mouse button to continue.", 0, (255, 255, 255)), (20, 250))
            elif players[turnnumber].AI:
                players[turnnumber].playcard()
                nextplayerturn = True
                if direction:
                    turnnumber += 1
                    if turnnumber == len(players):
                        turnnumber = 0
                else:
                    turnnumber -= 1
                    if turnnumber == -1:
                        turnnumber = len(players) - 1
            elif len(players[turnnumber].handcards):
                pickup = True
                for x in range(0, len(players[turnnumber].handcards)):
                    screen.blit(cards[players[turnnumber].handcards[x]], (130 + 20 * x, 400))
                    if Is_Playable(players[turnnumber].handcards[x]):
                        pickup = False

                if pickup and not firstplayedcard:
                    screen.blit(pygame.font.Font('freesansbold.ttf', 20).render(players[turnnumber].name + ' cannot play, need to pick up. Press left mouse button to continue.', 0, (255, 255, 255)), (20, 250))
            elif len(players[turnnumber].frontrowcards):
                for x in range(0, len(players[turnnumber].frontrowcards)):
                    screen.blit(cards[players[turnnumber].frontrowcards[x]], (130 + 20 * x, 400))

                if pickup and not firstplayedcard:
                    screen.blit(pygame.font.Font('freesansbold.ttf', 20).render(players[turnnumber].name + ' cannot play, need to pick up. Press left mouse button to continue.', 0, (255, 255, 255)), (20, 250))
            else:
                for x in range(0, len(players[turnnumber].hiddencards)):
                    screen.blit(cardback, (130 + 20 * x, 400))

                if pickup:
                    screen.blit(pygame.font.Font('freesansbold.ttf', 20).render(players[turnnumber].name + ' cannot play, need to pick up. Press left mouse button to continue.', 0, (255, 255, 255)), (20, 250))
            if playanother:
                screen.blit(pygame.font.Font('freesansbold.ttf', 20).render('You can playanother card or click anywhere else to pass.', 0, (255, 255, 255)), (20, 250))
            for x in range(0, len(playedcards)):
                screen.blit(cards[playedcards[x]], (130 + 20 * x, 300))

        except Exception:
            pass

    elif gamestart == 3:
        for x in range(0, len(players)):
            screen.blit(pygame.font.Font('freesansbold.ttf', 20).render(players[x].name, 0, (255, 255, 255)), (30 + (30 + 20 * int(cardsperplayer / 3)) * x, 5))
            for y in range(0, len(players[x].hiddencards)):
                screen.blit(cardback, (30 + 20 * y + (30 + 20 * int(cardsperplayer / 3)) * x, 30))

            for y in range(0, len(players[x].frontrowcards)):
                screen.blit(cards[players[x].frontrowcards[y]], (30 + 20 * y + (30 + 20 * int(cardsperplayer / 3)) * x, 40))

            if len(players[x].handcards):
                screen.blit(cardback, (30 + (30 + 20 * int(cardsperplayer / 3)) * x, 105))
                screen.blit(pygame.font.Font('freesansbold.ttf', 20).render(str(len(players[x].handcards)), 0, (255, 255, 255)), (45 + (30 + 20 * int(cardsperplayer / 3)) * x, 125))

        if len(deck):
            screen.blit(pygame.font.Font('freesansbold.ttf', 20).render('Deck: ' + str(len(deck)), 0, (255, 255, 255)), (20, 515))
            screen.blit(cardback, (20, 540))
        if nextplayerturn:
            screen.blit(pygame.font.Font('freesansbold.ttf', 20).render(players[turnnumber].name + "'s turn. Press left mouse button to continue.", 0, (255, 255, 255)), (20, 250))
        elif players[turnnumber].AI:
            players[turnnumber].frontrowsort()
            nextplayerturn = True
            turnnumber += 1
            if turnnumber == len(players):
                turnnumber = 0
                gamestart = 2
        else:
            for x in range(0, len(players[turnnumber].handcards)):
                screen.blit(cards[players[turnnumber].handcards[x]], (130 + 20 * x, 400))

            if len(players[turnnumber].frontrowcards) < len(players[turnnumber].handcards):
                screen.blit(pygame.font.Font('freesansbold.ttf', 20).render('Choose cards to go in the front row.', 0, (255, 255, 255)), (20, 250))
            else:
                nextplayerturn = True
                turnnumber += 1
                if turnnumber == len(players):
                    turnnumber = 0
                    gamestart = 2
    elif gamestart == 4:
        screen.blit(pygame.font.Font('freesansbold.ttf', 20).render(players[0].name + 'Lost. Click to start another match or close the window to exit.', 0, (255, 255, 255)), (20, 250))
    else:
        order = Get_Player_Parameters()
        gamestart = 1
    pygame.display.flip()
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        gameon = False
        while threadnumber:
            pass

        pygame.quit()
        sys.exit()
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            if gamestart != 4:
                mousethread.ID = 1
            else:
                gamestart = 0

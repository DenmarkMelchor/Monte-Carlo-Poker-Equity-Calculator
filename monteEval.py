import random
from time import time
import concurrent.futures

""" rangedDeck = {"AA":.005,"AKs":.035,"AQs":.040,"AJs":.055,"ATs":.060,"A9s":.085,"A8s":.105,"A7s":.120,"A6s":.155,"A5s":.155,"A4s":.170,"A3s":.205,"A2s":.215,
    "AKo":.050,"KK":.010,"KQs":.070,"KJs":.085,"KTs":.100,"K9s":.145,"K8s":.180,"K7s":.210,"K6s":.240,"K5s":.265,"K4s":.300,"K3s":.350,"K2s":.355,
    "AQo":.070,"KQo":.115,"QQ":.015,"QJs":.120,"QTs":.150,"Q9s":.185,"Q8s":.265,"Q7s":.320,"Q6s":.350,"Q5s":.375,"Q4s":.405,"Q3s":.415,"Q2s":.470,
    "AJo":.080,"KJo":.140,"QJo":.195,"JJ":.020,"JTs":.210,"J9s":.295,"J8s":.335,"J7s":.400,"J6s":.445,"J5s":.480,"J4s":.520,"J3s":.530,"J2s":.545,
    "ATo":.105,"KTo":.175,"QTo":.235,"JTo":.315,"TT":.025,"T9s":.335,"T8s":.400,"T7s":.445,"T6s":.525,"T5s":.545,"T4s":.590,"T3s":.615,"T2s":.635,
    "A9o":.145,"K9o":.225,"Q9o":.295,"J9o":.385,"T9o":.430,"99":.030,"98s":.425,"97s":.525,"96s":.560,"95s":.615,"94s":.665,"93s":.700,"92s":.710,
    "A8o":.165,"K8o":.285,"Q8o":.375,"J8o":.455,"T8o":.510,"98o":.560,"88":.035,"87s":.540,"86s":.610,"85s":.655,"84s":.715,"83s":.760,"82s":.785,
    "A7o":.200,"K7s":.345,"Q7o":.440,"J7o":.515,"T7o":.585,"97o":.620,"87o":.675,"77":.055,"76s":.650,"75s":.675,"74s":.745,"73s":.790,"72s":.895,
    "A6o":.255,"K6s":.365,"Q6o":.480,"J6o":.605,"T6o":.635,"96o":.720,"86o":.735,"76o":.770,"66":.090,"65s":.715,"64s":.760,"63s":.840,"62s":.895,
    "A5o":.250,"K5s":.395,"Q5o":.500,"J5o":.630,"T5o":.695,"95o":.705,"85o":.800,"75o":.820,"65o":.850,"55":.145,"54s":.780,"53s":.840,"52s":.900,
    "A4o":.275,"K4s":.415,"Q4o":.550,"J4o":.645,"T4o":.740,"94o":.810,"84o":.850,"74o":.895,"64o":.905,"54o":.900,"44":.230,"43s":.855,"42s":.900,
    "A3o":.305,"K3s":.465,"Q3o":.575,"J3o":.660,"T3o":.745,"93o":.830,"83o":.900,"73o":.930,"63o":.950,"53o":.940,"43o":.960,"33":.320,"32s":.910,
    "A2o":.345,"K2s":.490,"Q2o":.600,"J2o":.685,"T2o":.800,"92o":.900,"82o":.915,"72o":.970,"62o":.990,"52o":.980,"42o":.995,"32o":.995,"22":.420
    } """

rangedDeck = [['AA', 0.005], ['KK', 0.01], ['QQ', 0.015], ['JJ', 0.02], ['TT', 0.025], ['99', 0.03], ['AKs', 0.035], ['88', 0.035], ['AQs', 0.04], ['AKo', 0.05], ['AJs', 0.055], ['77', 0.055], ['ATs', 0.06], ['KQs', 0.07], ['AQo', 0.07], ['AJo', 0.08], ['A9s', 0.085], ['KJs', 0.085], ['66', 0.09], ['KTs', 0.1], ['A8s', 0.105], ['ATo', 0.105], ['KQo', 0.115], ['A7s', 0.12], ['QJs', 0.12], ['KJo', 0.14], ['K9s', 0.145], ['A9o', 0.145], ['55', 0.145], ['QTs', 0.15], ['A6s', 0.155], ['A5s', 0.155], ['A8o', 0.165], ['A4s', 0.17], ['KTo', 0.175], ['K8s', 0.18], ['Q9s', 0.185], ['QJo', 0.195], ['A7o', 0.2], ['A3s', 0.205], ['JTs', 0.21], ['A2s', 0.215], ['K9o', 0.225], ['44', 0.23], ['QTo', 0.235], ['A5o', 0.25], ['A6o', 0.255], ['Q8s', 0.265], ['A4o', 0.275], ['K8o', 0.285], ['J9s', 0.295], ['Q9o', 0.295], ['A3o', 0.305], ['JTo', 0.315], ['Q7s', 0.32], ['33', 0.32], ['J8s', 0.335], ['T9s', 0.335], ['K7s', 0.345], ['A2o', 0.345], ['Q6s', 0.35], ['K6s', 0.365], ['Q5s', 0.375], ['Q8o', 0.375], ['J9o', 0.385], ['K5s', 0.395], ['J7s', 0.4], ['T8s', 0.4], ['Q4s', 0.405], ['K4s', 0.415], ['Q3s', 0.415], ['22', 0.42], ['98s', 0.425], ['T9o', 0.43], ['Q7o', 0.44], ['J6s', 0.445], ['T7s', 0.445], ['J8o', 0.455], ['K3s', 0.465], ['Q2s', 0.47], ['J5s', 0.48], ['Q6o', 0.48], ['K2s', 0.49], ['Q5o', 0.5], ['T8o', 0.51], ['J7o', 0.515], ['J4s', 0.52], ['T6s', 0.525], ['97s', 0.525], ['J3s', 0.53], ['87s', 0.54], ['J2s', 0.545], ['T5s', 0.545], ['Q4o', 0.55], ['96s', 0.56], ['98o', 0.56], ['Q3o', 0.575], ['T7o', 0.585], ['T4s', 0.59], ['Q2o', 0.6], 
['J6o', 0.605], ['86s', 0.61], ['T3s', 0.615], ['95s', 0.615], ['97o', 0.62], ['J5o', 0.63], ['T2s', 0.635], ['T6o', 0.635], ['J4o', 0.645], ['76s', 0.65], ['85s', 0.655], ['J3o', 0.66], ['94s', 0.665], ['87o', 0.675], ['75s', 0.675], ['J2o', 0.685], ['T5o', 0.695], ['93s', 0.7], ['95o', 0.705], ['92s', 0.71], ['84s', 0.715], ['65s', 0.715], ['96o', 0.72], ['86o', 0.735], ['T4o', 0.74], ['74s', 0.745], ['T3o', 0.745], ['83s', 0.76], ['64s', 0.76], ['76o', 0.77], ['54s', 0.78], ['82s', 0.785], ['73s', 0.79], 
['85o', 0.8], ['T2o', 0.8], ['94o', 0.81], ['75o', 0.82], ['93o', 0.83], ['63s', 0.84], ['53s', 0.84], ['65o', 0.85], ['84o', 0.85], ['43s', 0.855], ['72s', 0.895], ['62s', 0.895], ['74o', 0.895], ['52s', 0.9], ['54o', 0.9], ['42s', 0.9], ['83o', 0.9], ['92o', 0.9], ['64o', 0.905], ['32s', 0.91], ['82o', 0.915], ['73o', 0.93], ['53o', 0.94], ['63o', 0.95], ['43o', 0.96], ['72o', 0.97], ['52o', 0.98], ['62o', 0.99], ['42o', 0.995], ['32o', 0.995]]

def build_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['h','s','c','d']
    deck = []
    for rank in ranks:
        for suit in suits:
            card = rank+suit
            deck.append(card)
    return deck

def pickCard(takenCards, deck):
    taken = True
    while taken == True:
        choice = random.choice(deck)
        i = 0
        for card in takenCards:
            if choice != card:
                i += 1
        if i == len(takenCards):
            taken = False
    takenCards.append(choice)
    return choice, takenCards

def pickCards_inRange(numVillains, villains, deck, takenCards, probableRange):
    for i in range(numVillains):
        inRange = False
        while inRange == False:
            villains.append(["card1", "card2", probableRange])
            cardChoice, takenCards = pickCard(takenCards, deck)
            villains[i][0] = cardChoice
            cardChoice, takenCards = pickCard(takenCards, deck)
            villains[i][1] = cardChoice
            if villains[i][0][0] == villains[i][1][0]:
                rangedCards = villains[i][0][0] + villains[i][1][0]
            elif villains[i][0][1] == villains[i][1][1]:
                rangedCards = villains[i][0][0] + villains[i][1][0] + 's'
            else:
                rangedCards = villains[i][0][0] + villains[i][1][0] + 'o'
            for i in range(len(rangedDeck)):
                if rangedDeck[i][0] == rangedCards:
                    if rangedDeck[i][1] <= probableRange:
                        inRange = True
                    else:
                        del villains[i]

def flushEval(hand):
    sMatch = cMatch = dMatch = hMatch = 0
    sCards = cCards = dCards = hCards = []
    flushCards = []
    isFlush = False
    flush_val = 0
    for i in range(7):
        match = hand[i][1]
        if match == "0": # accounts for card with rank 10
            match = hand[i][2]
        if match == "s":
            sMatch += 1
            sCards.append(hand[i])
        if match == "c":
            cMatch += 1
            cCards.append(hand[i])
        if match == "d":
            dMatch += 1
            dCards.append(hand[i])
        if match == "h":
            hMatch += 1
            hCards.append(hand[i])
    if sMatch >= 5:
        isFlush = True
        flushCards = sCards
    elif cMatch >= 5:
        isFlush = True
        flushCards = cCards
    elif dMatch >= 5:
        isFlush = True
        flushCards = dCards
    elif hMatch >= 5:
        isFlush = True
        flushCards = hCards
    if isFlush:
        cardRankorder = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        highestNum = 0
        for i in range(5):
            for x in range(13):
                if flushCards[i][0] == cardRankorder[x][0]:
                    if x >= highestNum:
                        highestNum = x
        flush_val = 6000000 + highestNum
    return isFlush, flushCards, flush_val

def straightEval(hand):
    rankOrder = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    handOrder = [] + rankOrder
    highRank = ""
    straight_val = 0
    isStraight = False
    for i in range(len(hand)):
        for x in range(14):
            if hand[i][0] == handOrder[x][0]:
                handOrder[x] = hand[i]
    for i in range(14):
        if len(handOrder[i]) == 1:
            handOrder[i] = 0
    while 0 in handOrder:
        handOrder.remove(0)
    for i in range(10):
        for x in range(len(handOrder)-4):
            if handOrder[x][0] == rankOrder[i][0]:
                if handOrder[x+1][0] == rankOrder[i+1][0]:
                    if handOrder[x+2][0] == rankOrder[i+2][0]:
                        if handOrder[x+3][0] == rankOrder[i+3][0]:
                            if handOrder[x+4][0] == rankOrder[i+4][0]:
                                highRank = i+4
                                isStraight = True
    if isStraight:
        straight_val = 5000000 + highRank
    return isStraight, highRank, straight_val

def straightflushEval(hand):
    is_straightFlush = False
    isStraight = False
    straight_calculated = False
    straight_val = 0
    straightFlush_val = 0
    isFlush, flushCards, flush_val = flushEval(hand)
    if isFlush == True:
        isStraight, highRank, straight_val = straightEval(flushCards)
        if isStraight == True:
            straightFlush_val = 9000000 + highRank
            is_straightFlush = True
    else:
        straight_calculated = False
    return is_straightFlush, straightFlush_val, isFlush, flush_val, isStraight, straight_val, straight_calculated

def fourkindEval(hand):
    is_fourKind = False
    fourKind_val = 0
    found = False
    for i in range(7):
        if found:
            break
        rankCount = 0
        for x in range(7):
            if hand[i][0] == hand[x][0]:
                rankCount += 1
                if rankCount == 4:
                    is_fourKind = True
                    fourKind_rank = hand[i][0]
                    found = True
                    break
    if is_fourKind:
        lastCard = [] + hand
        for i in range(7):
            if lastCard[i][0] == fourKind_rank:
                lastCard[i] = 0
        while 0 in lastCard:
            lastCard.remove(0)
        highestNum = 0
        for i in range(len(lastCard)):
            if lastCard[i][0] == 'T':
                lastCard[i] = 10
            elif lastCard[i][0] == 'J':
                lastCard[i] = 11
            elif lastCard[i][0] == 'Q':
                lastCard[i] = 12
            elif lastCard[i][0] == 'K':
                lastCard[i] = 13
            elif lastCard[i][0] == 'A':
                lastCard[i] = 14
            else:
                lastCard[i] = int(lastCard[i][0])
            if lastCard[i] >= highestNum:
                highestNum = lastCard[i]
        fourKind_val = 8000000 + highestNum
    return is_fourKind, fourKind_val

def threekindEval(hand):
    is_threeKind = False
    threeKind_rankVal = 0
    threeKind_rank = ""
    threeKinds = []
    for i in range(7):
        rankCount = 0
        for x in range(7):
            if hand[i][0] == hand[x][0]:
                rankCount += 1
                if rankCount == 3:
                    is_threeKind = True
                    threeKinds.append(hand[i][0])
    if is_threeKind == True:
        cardRankorder = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        highestNum = 0
        for i in range(len(threeKinds)):
            for x in range(13):
                if threeKinds[i][0] == cardRankorder[x][0]:
                    threeKinds[i] = str(x)
            if int(threeKinds[i]) >= highestNum:
                highestNum = int(threeKinds[i])
        threeKind_rank = cardRankorder[highestNum]
        threeKind_rankVal = highestNum
    return is_threeKind, threeKind_rank, threeKind_rankVal

def fullhouseEval(hand):
    is_fullHouse = False
    fullHouse_val = 0
    threeKind_val = 0
    is_threeKind, threeKind_rank, threeKind_rankVal = threekindEval(hand)
    if is_threeKind:
        has_pair = False
        pairs = []
        lastFour = [] + hand
        for i in range(7):
            if lastFour[i][0] == threeKind_rank:
                lastFour[i] = 0
        while 0 in lastFour:
            lastFour.remove(0)
        for i in range(4):
            rankCount = 0
            for x in range(4):
                if lastFour[i][0] == lastFour[x][0]:
                    rankCount += 1
                    if rankCount == 2:
                        has_pair = True
                        pairs.append(lastFour[i][0])
        if has_pair == False:
            cardRankorder = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
            highestNum = 0
            secondHighest = 0
            for i in range(4):
                for x in range(13):
                    if lastFour[i][0] == cardRankorder[x][0]:
                        if x >= highestNum:
                            highestNum = x
                            firstKicker_rank = cardRankorder[x][0]
            for i in range(4):
                if lastFour[i][0] == firstKicker_rank:
                    lastFour[i] = 0
            firstKicker_val = highestNum
            while 0 in lastFour:
                lastFour.remove(0)
            for i in range(3):
                for x in range(13):
                    if lastFour[i][0] == cardRankorder[x][0]:
                        if x >= secondHighest:
                            secondHighest = x               
            secondKicker_val = secondHighest
            threeKind_val = 4000000 + (threeKind_rankVal*250) + (firstKicker_val * 15) + (secondKicker_val)
        if has_pair:
            is_fullHouse = True
            cardRankorder = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
            highestNum = 0
            for i in range(len(pairs)):
                for x in range(13):
                    if pairs[i][0] == cardRankorder[x][0]:
                        pairs[i] = str(x)
                if int(pairs[i]) >= highestNum:
                    highestNum = int(pairs[i])
            pair_rankVal = highestNum
            fullHouse_val = 7000000 + (threeKind_rankVal*15) + (pair_rankVal)
    return is_fullHouse, fullHouse_val, is_threeKind, threeKind_val

def twopairEval(hand):
    is_twoPair = False
    is_onePair = False
    twoPair_val = 0
    onePair_val = 0
    pairs = []
    for i in range(7):
        rankCount = 0
        for x in range(7):
            if hand[i][0] == hand[x][0]:
                rankCount += 1
                if rankCount == 2:
                    pairs.append(hand[i][0])
    if len(pairs) == 4 or len(pairs) == 6:
        is_twoPair = True
        cardRankorder = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        highestNum = 0
        for i in range(len(pairs)):
            for x in range(13):
                if pairs[i][0] == cardRankorder[x][0]:
                    if x >= highestNum:
                        highestNum = x
                        higherPair_rank = cardRankorder[x][0]
        for i in range(len(pairs)):
            if pairs[i][0] == higherPair_rank:
                pairs[i] = 0
        higherPair_val = highestNum
        while 0 in pairs:
            pairs.remove(0)
        sec_highestNum = 0
        for i in range(len(pairs)):
            for x in range(13):
                if pairs[i][0] == cardRankorder[x][0]:
                    if x >= sec_highestNum:
                        sec_highestNum = x
                        lowerPair_rank = cardRankorder[x][0]
        for i in range(len(pairs)):
            if pairs[i][0] == lowerPair_rank:
                pairs[i] = 0
        lowerPair_val = sec_highestNum
        while 0 in pairs:
            pairs.remove(0)
        kickers = [] + hand
        for i in range(7):
            if kickers[i][0] == higherPair_rank or kickers[i] == lowerPair_rank:
                kickers[i] = 0
        while 0 in kickers:
            kickers.remove(0)
        highestKicker = 0
        for i in range(len(kickers)):
            for x in range(13):
                if kickers[i][0] == cardRankorder[x][0]:
                    if x >= highestKicker:
                        highestKicker = x
        kicker_val = highestKicker
        twoPair_val = 3000000 + (higherPair_val * 250 ) + (lowerPair_val * 15 ) + (kicker_val)
    elif len(pairs) == 2:
        is_onePair = True
        cardRankorder = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        for i in range(13):
            if pairs[0][0] == cardRankorder[i][0]:
                pair_val = i
                break
        kickers = [] + hand
        pairRank = pairs[0][0]
        for i in range (7):
            if kickers[i][0] == pairRank:
                kickers[i] = 0
        while 0 in kickers:
            kickers.remove(0)
        highestKicker = 0
        for i in range(5):
            for x in range(13):
                if kickers[i][0] == cardRankorder[x][0]:
                    if x >= highestKicker:
                        highestKicker = x
                        highestKicker_rank = cardRankorder[x][0]
        for i in range(5):
            if kickers[i][0] == highestKicker_rank:
                kickers[i] = 0
        firstKick_val = highestKicker
        while 0 in kickers:
            kickers.remove(0)
        sec_highestKicker = 0
        for i in range(4):
            for x in range(13):
                if kickers[i][0] == cardRankorder[x][0]:
                    if x >= sec_highestKicker:
                        sec_highestKicker = x
                        sechighestKicker_rank = cardRankorder[x][0]
        for i in range(4):
            if kickers[i][0] == sechighestKicker_rank:
                kickers[i] = 0
        secKick_val = sec_highestKicker
        while 0 in kickers:
            kickers.remove(0)
        third_highestKicker = 0
        for i in range(3):
            for x in range(13):
                if kickers[i][0] == cardRankorder[x][0]:
                    if x >= third_highestKicker:
                        third_highestKicker = x
        thirdKick_val = third_highestKicker
        onePair_val = 2000000 + (pair_val * 4000) + (firstKick_val * 250) + (secKick_val * 15) + thirdKick_val
    return is_twoPair, twoPair_val, is_onePair, onePair_val

def highcardEval(hand):
    cardRankorder = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    highestNum = 0
    for i in range(7):
        for x in range(13):
            if hand[i][0] == cardRankorder[x][0]:
                if x >= highestNum:
                    highestNum = x
                    highestRank = cardRankorder[x][0]
    for i in range(7):
        if hand[i][0] == highestRank:
            hand[i] = 0
    while 0 in hand:
        hand.remove(0)
    sec_highestNum = 0
    for i in range(6):
        for x in range(13):
            if hand[i][0] == cardRankorder[x][0]:
                if x >= sec_highestNum:
                    sec_highestNum = x
                    sec_highestRank = cardRankorder[x][0]
    for i in range(6):
        if hand[i][0] == sec_highestRank:
            hand[i] = 0
    while 0 in hand:
        hand.remove(0)
    third_highestNum = 0
    for i in range(5):
        for x in range(13):
            if hand[i][0] == cardRankorder[x][0]:
                if x >= third_highestNum:
                    third_highestNum = x
                    third_highestRank = cardRankorder[x][0]
    for i in range(5):
        if hand[i][0] == third_highestRank:
            hand[i] = 0
    while 0 in hand:
        hand.remove(0)
    fourth_highestNum = 0
    for i in range(4):
        for x in range(13):
            if hand[i][0] == cardRankorder[x][0]:
                if x >= fourth_highestNum:
                    fourth_highestNum = x
                    fourth_highestRank = cardRankorder[x][0]
    for i in range(4):
        if hand[i][0] == fourth_highestRank:
            hand[i] = 0
    while 0 in hand:
        hand.remove(0)
    fifth_highestNum = 0
    for i in range(3):
        for x in range(13):
            if hand[i][0] == cardRankorder[x][0]:
                if x >= fifth_highestNum:
                    fifth_highestNum = x
    highCard_val = 1000000 + (highestNum * 60010) + (sec_highestNum * 4000) + (third_highestNum * 250) + (fourth_highestNum * 15) + fifth_highestNum
    return highCard_val

def evalHand(hand):
    # hand = commCards + player[0] + player[1]
    # player[0] = 1st card, player[1] = 2nd card
    is_straightFlush, straightFlush_val, isFlush, flush_val, isStraight, straight_val, straight_calculated = straightflushEval(hand) 
    if is_straightFlush:
        return straightFlush_val
    is_fourKind, fourKind_val = fourkindEval(hand)
    if is_fourKind:
        return fourKind_val
    is_fullHouse, fullHouse_val, is_threeKind, threeKind_val = fullhouseEval(hand)
    if is_fullHouse:
        return fullHouse_val
    if isFlush:
        return flush_val
    if straight_calculated == False:
        isStraight, highRank, straight_val = straightEval(hand)
    if isStraight:
        return straight_val
    if is_threeKind:
        return threeKind_val
    is_twoPair, twoPair_val, is_onePair, onePair_val = twopairEval(hand)
    if is_twoPair:
        return twoPair_val
    if is_onePair:
        return onePair_val
    return highcardEval(hand)

# hole1 and hole2 must be in "2-A + h/s/c/d" format | probableRange is from 0 to 1
# never set probableRange to less than 0.05
def monteEval(numSimulations, hole1, hole2, numVillains, probableRange, commCard1, commCard2, commCard3, commCard4, commCard5):
    heroWins = 0
    ties = 0
    for i in range(numSimulations):
        deck = build_deck()
        hero = [hole1, hole2]
        takenCards = [hole1, hole2, commCard1, commCard2, commCard3, commCard4, commCard5]
        villains = []
        # assigns villain cards in range
        for i in range(numVillains): 
            inRange = False
            while inRange == False:
                villains.append(["card1", "card2", probableRange])
                cardChoice, takenCards = pickCard(takenCards, deck)
                villains[i][0] = cardChoice
                cardChoice, takenCards = pickCard(takenCards, deck)
                villains[i][1] = cardChoice
                if villains[i][0][0] == villains[i][1][0]:
                    rangedCards = villains[i][0][0] + villains[i][1][0]
                elif villains[i][0][1] == villains[i][1][1]:
                    rangedCards = villains[i][0][0] + villains[i][1][0] + 's'
                else:
                    rangedCards = villains[i][0][0] + villains[i][1][0] + 'o'
                for x in range(len(rangedDeck)):
                    if rangedDeck[x][0] == rangedCards:
                        if rangedDeck[x][1] <= probableRange:
                            inRange = True
                if inRange == False:
                    del villains[-1]
                    del takenCards[-1]
                    del takenCards[-2]
        # assign community cards
        commCards = [commCard1, commCard2, commCard3, commCard4, commCard5]
        for i in range(5):
            if commCards[i] == "":
                cardChoice, takenCards = pickCard(takenCards, deck)
                commCards[i] = cardChoice
        # evaluate hands of each player and find winner
        heroHand = hero + commCards
        heroScore = evalHand(heroHand)
        villainHands = []
        villainScores = []
        heroWin = True
        tie = False
        for i in range(numVillains):
            villainHands.append([villains[i][0], villains[i][1], commCards[0], commCards[1], commCards[2], commCards[3], commCards[4]])
            villainScores.append(evalHand(villainHands[i]))
            if villainScores[i] > heroScore:
                heroWin = False
        if heroWin:
            for i in range(numVillains):
                if villainScores[i] == heroScore:
                    tie = True
        # count win, tie, or loss
        if tie:
            ties += 1
        elif heroWin:
            heroWins += 1
    # calculate and return equity based on simulations
    if heroWins == 0:
        if ties == 0:
            return 0
        if ties > 0:
            return ((ties/numSimulations)/2)
    else:
        if ties > 0:
            return ((heroWins/numSimulations) + ((ties/numSimulations)/2))
        else:
            return (heroWins/numSimulations)

# Amount of simulations = procs * sims | 10 procs * 1000 sims per proc = 10,000 simulations.
def multi_monteEval(procs, sims, hole1, hole2, numVillains, probableRange, commCard1, commCard2, commCard3, commCard4, commCard5):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(monteEval, sims, hole1, hole2, numVillains, probableRange, commCard1, commCard2, commCard3, commCard4, commCard5) for _ in range(procs)]

        probableEquity = 0
        for result in concurrent.futures.as_completed(results):
            probableEquity = probableEquity + result.result()   
        probableEquity = round(probableEquity/procs, 4)
    return probableEquity

def main():
    # Asks for hero's hole cards, number of villains, and probable range of said villains.
    hole1 = input("What is your first hole card? (i.e. Ad for Ace of Diamonds) ")
    hole2 = input("What is your second hole card? (i.e. Ad for Ace of Diamonds) ")
    villNum = int(input("How many villains are there? "))
    probRange = float(input("What is the probable range for each of the villains? "))

    # Creates function that asks for street and community cards if necessary.
    def askStreetCards():
        street = input("What street is it? (1 or preflop, 2 or flop, 3 or turn, 4 or river)")
        comm1 = ""
        comm2 = ""
        comm3 = ""
        comm4 = ""
        comm5 = ""
        if street == "4" or street == "river":
            comm1 = input("What is the first community card? (i.e. Ad for Ace of Diamonds)")
            comm2 = input("What is the second community card? (i.e. Ad for Ace of Diamonds)")
            comm3 = input("What is the third community card? (i.e. Ad for Ace of Diamonds)")
            comm4 = input("What is the fourth community card? (i.e. Ad for Ace of Diamonds)")
            comm5 = input("What is the fifth community card? (i.e. Ad for Ace of Diamonds)")
        elif street == "3" or street == "turn":
            comm1 = input("What is the first community card? (i.e. Ad for Ace of Diamonds)")
            comm2 = input("What is the second community card? (i.e. Ad for Ace of Diamonds)")
            comm3 = input("What is the third community card? (i.e. Ad for Ace of Diamonds)")
            comm4 = input("What is the fourth community card? (i.e. Ad for Ace of Diamonds)")
            comm5 = ""
        elif street == "2" or street == "flop":
            comm1 = input("What is the first community card? (i.e. Ad for Ace of Diamonds)")
            comm2 = input("What is the second community card? (i.e. Ad for Ace of Diamonds)")
            comm3 = input("What is the third community card? (i.e. Ad for Ace of Diamonds)")
        elif street == "1" or street == "preflop":
            pass
        else:
            print("Please supply a proper input.")
            comm1, comm2, comm3, comm4, comm5 = askStreetCards()
        return comm1, comm2, comm3, comm4, comm5

    # Calls created function.
    comm1, comm2, comm3, comm4, comm5 = askStreetCards()

    # Calculates and prints probable equity for hero | Change first 2 arguments to change number of simulations
    probableEquity = multi_monteEval(10, 1000, hole1, hole2, villNum, probRange,  comm1, comm2, comm3, comm4, comm5)
    print(f"Probable Equity: {probableEquity}")

# Necessary to use multiprocessing.
if __name__ == '__main__':
    main()

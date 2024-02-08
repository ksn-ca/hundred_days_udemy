import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
dealer_cards = []

def deal_card(num_cards):
    cards_to_add = []
    for i in range(num_cards):
        cards_to_add.append(random.choice(cards))
    return cards_to_add

def check_winner():
    dealer_sum = sum(dealer_cards)
    user_sum = sum(user_cards)
    winner = ''

    if dealer_sum > 21 and user_sum > 21:
        winner = 'DRAW'
    elif dealer_sum > 21:
        winner = 'You win'
    elif user_sum > 21:
        winner = 'Dealer wins'
    elif user_sum > dealer_sum:
        winner = 'You win'
    else: 
        winner = 'Dealer wins'

    return winner

def print_score():
    print(f'Your cards are : {user_cards}, current score: {sum(user_cards)}')
    print(f'Computer cards are {dealer_cards}, computer score: {sum(dealer_cards)}')
    print(check_winner())

def blackjack():
    #first interation 
    user_cards.extend(deal_card(2))
    # dealer_cards.extend(deal_card(2))
    
    while sum(dealer_cards) < 17:
        dealer_cards.extend(deal_card(1))

    cont = True
    while cont:
        print(f'Your cards are : {user_cards}, current score: {sum(user_cards)}')
        print(f'Computer first card is {dealer_cards[0]}')

        user_choice = input('Type y to get another card, type n to pass.   ')

        if user_choice == 'y':
            user_cards.extend(deal_card(1))
            if sum(user_cards) > 21:
                if 11 in user_cards:
                    eleven_index = user_cards.index(11)
                    user_cards.pop(eleven_index)
                    user_cards.insert(eleven_index, 1)
                    print('You changed ace 11 to 1.')
                else:
                    print_score()
                    cont = False
        else:   
            print_score()
            cont = False


blackjack()

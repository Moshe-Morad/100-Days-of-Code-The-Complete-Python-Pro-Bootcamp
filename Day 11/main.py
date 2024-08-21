import random
from art import logo


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


user_sum_of_card = 0
dealer_sum_of_card = 0
print(logo)
while input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").lower() == "y":
    user = [deal_card(), deal_card()]
    for card_u in user:
        user_sum_of_card += card_u
    print(f"Your cards: {user}, current score: {user_sum_of_card}")

    dealer = [deal_card()]
    print(f"Computer's first card: {dealer}")

    user_answer = input("Type 'Y' to get another card, type 'N' to pass:  ")
    if user_answer == "y":
        user.append(deal_card())
        user_sum_of_card += user[2]
        print(f"Your cards: {user}, current score: {user_sum_of_card}")
        print(f"Computer's first card: {dealer}")
    print(f"Your final hand: {user}, final score: {user_sum_of_card}")

    if user_sum_of_card < 21:
        dealer.append(deal_card())
        for card_d in dealer:
            dealer_sum_of_card += card_d
        print(f"Computer's cards: {dealer}, current score: {dealer_sum_of_card}")
        if dealer_sum_of_card < 17:
            dealer.append(deal_card())
            dealer_sum_of_card += dealer[2]
        print(f"Computer's final hand: {dealer}, final score: {dealer_sum_of_card}")
    else:
        dealer_sum_of_card += dealer[0]
        print(f"Computer's final hand: {dealer}, final score: {dealer_sum_of_card}")

    if user_sum_of_card > 21 and dealer_sum_of_card > 21:
        print("You went over. You lose 😤")
    if user_sum_of_card == dealer_sum_of_card:
        print("Draw 🙃")
    elif dealer_sum_of_card == 21:
        print("Lose, opponent has Blackjack 😱")
    elif user_sum_of_card == 21:
        print("Win with a Blackjack 😎")
    elif user_sum_of_card > 21:
        print("You went over. You lose 😭")
    elif dealer_sum_of_card > 21:
        print("Opponent went over. You win 😁")
    elif user_sum_of_card < dealer_sum_of_card <= 21:
        print("your hand is lower then the dealer, You lose 😤")
    elif dealer_sum_of_card < user_sum_of_card <= 21:
        print("dealer hand is lower then your hand, You win 😃")
else:
    print("Thank you for participant!")

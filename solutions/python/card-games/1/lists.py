"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
        
    return [number ,number+1,number+2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    # if rounds or number == []:
    #     return []
    # else:
    return (rounds_1+ rounds_2)


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    for i in rounds:
        if i ==number:
            return True 
    else:
        return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    # avg=sum(hand)/len(hand)
    # for i in hand:
    #     if i == avg:
    #         return True 
    # else:
    #     return False
    middle_index = len(hand) // 2
    middle_num = hand[middle_index]
    avg=(hand[0] + hand[-1] )/2

    return card_average(hand) in (avg , middle_num)


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_list=[]
    odd_list=[]
    
    for i in range(len(hand)):
        if i%2==0:
            even_list.append(hand[i])
        else:
            odd_list.append(hand[i])
            
    avg_eve=sum(even_list)/len(even_list)
    avg_odd=sum(odd_list)/len(odd_list)
    
    if avg_eve==avg_odd:
        return True 
    else:
        return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1]==11:
        last_El=hand[-1]*2
        hand.pop()
        hand.append(last_El)
        return hand
    else :
        return hand 
    

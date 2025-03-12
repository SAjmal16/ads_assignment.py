def trick_score(trick, trump_suit):
    """
    Computes the score of a trick in a card game using a standard deck of 32 cards.
    
    Parameters:
    trick (set of tuples): A set containing exactly four distinct cards represented as (rank, suit).
    trump_suit (str): The trump suit for the trick, must be one of 'Spades', 'Diamonds', 'Hearts', or 'Clubs'.
    
    Returns:
    int: The total score of the trick based on card values.
    
    Raises:
    TypeError: If trump_suit is not a valid suit.
    ValueError: If trick does not contain exactly four valid cards.
    """
    valid_suits = {'Spades', 'Diamonds', 'Hearts', 'Clubs'}
    valid_ranks = {'7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'}
    
    if trump_suit not in valid_suits:
        raise TypeError("Invalid trump suit. Must be one of: 'Spades', 'Diamonds', 'Hearts', or 'Clubs'.")
    
    if not isinstance(trick, set) or len(trick) != 4:
        raise ValueError("Trick must be a set of exactly four distinct cards.")
    
    for card in trick:
        if not isinstance(card, tuple) or len(card) != 2:
            raise ValueError("Each card must be a tuple (rank, suit).")
        rank, suit = card
        if rank not in valid_ranks or suit not in valid_suits:
            raise ValueError(f"Invalid card detected: {card}.")
    
    # Define trump and non-trump scoring values
    trump_values = {"Jack": 20, "9": 14, "Ace": 11, "10": 10, "King": 4, "Queen": 3, "8": 0, "7": 0}
    non_trump_values = {"Ace": 11, "10": 10, "King": 4, "Queen": 3, "Jack": 2, "9": 0, "8": 0, "7": 0}
    
    score = 0
    for rank, suit in trick:
        if suit == trump_suit:
            score += trump_values[rank]
        else:
            score += non_trump_values[rank]
    
    return score

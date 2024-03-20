import random

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

HAND_SIZE = 7

#
# Problem #1: Scoring a word
#
def get_word_score(word: str, n: int) -> int:
    """
    Returns the score for a word. Assumes the word is a valid word.
 
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.
 
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
 
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    assert isinstance(word,str), "word must be a string"
    
    if len(word) > 0:
        word = word.lower()
        assert word.islower(), "lower() conversion failed"
    assert isinstance(n, int), "n must be an int"
    assert n >= 0, "hand length n must not be 0"
 
    # Pseudocode
    """
    for each letter in word
        get letter score from dict SCRABBLE_LETTER_VALUES
        add up all the letter scores
    
    multiply by length of word
    followed by bonus calculation
    example if n=7 and you make the word "waybill" on the first try.
    it would be worth 155 points (the base score for "waybill" is (4++))
    """
    word_score = 0
 
    for letter in word:
        letter_score = SCRABBLE_LETTER_VALUES[letter]
        word_score += letter_score
    
    word_score *= len(word)
    if len(word) == n:
        word_score += 50

    # checking post-conditions
    assert word_score >= 0, "score calculation failed"
    assert isinstance(word_score, int), "score must be int"
 
    return word_score
 
#testcases for logic
print("Waybill earned", get_word_score("waybill", 7), "points" ) #155
 
#testcases for assertion
#Legal
# get_word_score("haPPy", 7)
# #Illegal
# get_word_score(1000, 7)
# get_word_score("", 7)
# get_word_score("blabla", 0)
 
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.
 
    For example:
    >>> display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.
 
    hand: dictionary (string -> int)
    """
#     for letter in hand.keys():
#         for _ in range(hand[letter]):
#             print(letter, end=" ")       # print all on the same line
#     print()                             # print an empty line
# display_hand({'a':1, 'x':2, 'l':3, 'e':1})
 
# Problem #2: Make sure you understand how this function works and what it does!
#
 
 
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.
 
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
 
    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n // 3
 
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
 
    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
 
    return hand
 
print(deal_hand(HAND_SIZE))
 
# #
# # Problem #2: Update a hand by removing letters]
def update_hand(hand: dict, word: str):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
 
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
 
    Has no side effects: does not modify hand.
 
    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
 
 
    """"
    make a hand.copy()
    for every letter in word
        use the letter as a key to look up in the hand dict
        and subtract one from the dict values letter counts
        what to do if letter count is 0 ?
    return handcopy
 
    """
    assert isinstance(word,str), "word must be a string"
    
    if len(word) > 0:
        word = word.lower()
        assert word.islower(), "lower() conversion failed"
 
    new_hand = hand.copy()
 
    for letter in word:
        if new_hand.get(letter) <= 0:
            del new_hand[letter]
        else:
            new_hand[letter] -= 1
    
    return new_hand
            
# testcases
print(update_hand({'a': 0, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}, "quail"))
 
 
 
# #
# # Problem #3: Test word validity
# #
def is_valid_word(word: str, hand: dict, word_list: list) -> bool:
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
 
    Does not mutate hand or word_list.
 
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
 
    # check pre-condition
    word : str
    "hello".count('l') #2
 
    """
    for each letter in word
        if letter not in hand
            return false
        else
            find the count of letter in word
            and make sure that count is also in your hand(letter)
                if not return false
 
    if word not in word_list
        return false
 
    return True
    """
    assert isinstance(word,str), "word must be a string"
    
    if len(word) > 0:
        word = word.lower()
        assert word.islower(), "lower() conversion failed"
    
    new_hand = hand.copy()
 
    for letter in word:
        if letter not in new_hand or new_hand[letter] == 0:
            return False
        else:
            new_hand[letter] -= 1
    
    if word not in word_list:
        return False
    
    return True
    # check post-condition
    # Does not mutate hand or word_list.
 
    #testcases
print(is_valid_word("hello", {'h': 1, 'e':1, 'l':2, 'o':1, 'u':1, 'i':1}, ["hello", "hero"]))
print(is_valid_word("hello", {'h': 1, 'e':1, 'l':1, 'o':2, 'u':1, 'i':1}, ["hello", "hero"]))
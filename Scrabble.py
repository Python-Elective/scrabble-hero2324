import random
import string
 
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
 
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
 
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
 
WORDLIST_FILENAME = "words.txt"
 
 
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
 
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list
 
 
def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
 
    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq
 
 
# (end of helper code)
# -----------------------------------
 
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
    for letter in hand.keys():
        for _ in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print()                             # print an empty line
 
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
    assert isinstance(word, str), "word must be a string"
   
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
#
# Problem #4: Playing a hand
#
 
def calculate_hand_len(hand):
    """
    Returns the length (number of letters) in the current hand.
 
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    handCount = 0
 
    for letter in hand:
        handCount += hand.get(letter)
    return handCount
 
 
def play_hand(hand: dict, word_list: list, n: int):
    """
    Allows the user to play the given hand, as follows:
 
    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."
 
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
 
    """
 
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
 
    assert isinstance(hand, dict), "Hand must be a dictionary"
    assert isinstance(n, int), "Hand size must be an integer"
    assert n >= 0, "Hand size must not be negative"
 
    totalScore = 0
 
    while calculate_hand_len(hand) > 1:
        display_hand(hand)
        Guess = input('Enter word, or a "." to indicate that you are finished: ').lower()
 
        assert isinstance(Guess, str), "Input word must be a string"
 
        if Guess == ".":
            break
        elif is_valid_word(Guess, hand, word_list) == False:
            print(f"Invalid Word, Try Again")
        else:
            totalScore += get_word_score(Guess, n)
            print('"'+Guess+'"', "earned", get_word_score(Guess, n), "points. Total:", totalScore, "points", '\n')
            hand = update_hand(hand, Guess)
 
    print(f"Goodbye! Total Score: {totalScore} points")
    return totalScore
 
           
 
# #
# # Problem #5: Playing a game
# #
 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    # <-- Remove this line when you code the function
 
 
#
# Build data structures used for entire session and play game
 
    assert isinstance(word_list, list)
 
    hand = {}
 
    while True:
        userInput = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:' )
        assert isinstance(userInput, str)
        if userInput == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list, HAND_SIZE)
        elif userInput == 'r':
            if not hand:
                print(f"Please play a new hand first")
            else:
                play_hand(hand, word_list, HAND_SIZE)
        elif userInput == 'e':
            print('Goodbye, game have ended')
            break
        else:
            print('Invalid Command')
 
   
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
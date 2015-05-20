def init ():
    '''Initializes the recursive sequence of guesses to track down mystery number'''
    print "Hello, I am going to try to guess the number you are thinking of."
    print "Please respond to my questions with higher, lower, or correct."
    print "Ready, set, go!"
    #low = raw_input("What is the LOW value you would like to have? > ")
    #high = raw_input("What is the HIGH value you would like to have? > ")
    inp = raw_input("What is the LOW, HIGH value you would like to test > ")
    low, high = inp.split(",")
    guesses = find_number(int(low), int(high), 0)
    print "Woo! Thanks for playing, that took %d guesses!" % guesses

def find_number (low, high, guesses):
    '''recursive function to track down the mystery number, keeps track of # of guesses'''
    hilo = find_middle (low, high)
    answer = raw_input("Is your number %d > " % hilo)
    if (answer == "correct"):
        return guesses
    elif (answer == "higher"):
        final_guesses = find_number (hilo+1, high, guesses+1)
    elif (answer == "lower"):
        final_guesses = find_number (low, hilo-1, guesses+1)
    else:
        print "Sorry, I didn't catch that."
        find_number (low, high, guesses)
    return final_guesses

def find_middle (low, high):
    '''returns the middle value rounded down using the built in floor division'''
    hilo = high-low
    return low + hilo // 2

init ()

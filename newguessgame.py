import random
def guess(rounds,randomN,tries):
    number = raw_input(" Guess a number: ")
    if int(number) == randomN:
        print "Thats Correct You must be a psychic"
    elif int(number) < randomN:
        print " That's too low "
        attempts(rounds,randomN,tries-1)
    elif int(number) > randomN:
        print " That's too high "
        attempts(rounds,randomN,tries-1)
    else:
        print " Hi, Im bored do you wanna play truth or dare? "

def attempts(rounds,randomN,tries):
    if tries == 0:
        print "{} rounds remaining".format(rounds)
        rounds -= 1
        guess(rounds,randomN,tries)
    else:
        guess(rounds,randomN,tries)
    
def main():
    print "Guess a number from 0 to 100 including 0 and 100"
    randomN = random.randint(0,100)
    tries = 5
    rounds = 3
    print "{} rounds remaining".format(rounds)
    attempts(rounds,randomN,tries)

main()

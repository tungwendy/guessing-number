from random import randint

def main():
  print "Welcome to the number guessing game!"
  print "You have 5 chances to guess! Good luck!"
  number = randint(1,10)
  count = 0
  while True:
    guess = raw_input("Guess a number between one and ten: ")
    count = count + 1
    if int(guess) == number:
      print "That's right!"
      break
    elif int(guess) > number:
      print "Sorry, that's too high.  Guess again please!"
    elif int(guess) < number:
      print "Sorry, that's too low.  Guess again please!"
    if count = 5:
    	"Sorry! Five trials done!"
    	break  
if __name__ == '__main__':
  main()
  

import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  i = 0
  while i < 3:
    last = len(quotes) - 1
    rnd = random.randint(0, last)

    print(quotes[rnd], end='')
    i += 1

if __name__== "__main__":
  primary()

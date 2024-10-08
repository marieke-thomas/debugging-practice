def encrypt(key, message):
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  
  result = ""
  for letter in message:
    if letter in alpha:
      letter_index = (alpha.find(letter) + key)%len(alpha)
      result = result + alpha[letter_index]
    else:
      result = result + letter
  return result


def main():
  word = "Secret code"
  encrypted = encrypt(3,word)
  print(word)
  print(encrypted) #should print "VHFUHW PBVWHUB PHVVDJH"

if __name__ == "__main__":
  main()


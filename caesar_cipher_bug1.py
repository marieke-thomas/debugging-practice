def encrypt(key, message):
  message = message.upper()
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  
  result = ""
  for letter in message:
    if letter in alpha:
      letter_index = (alpha.find(letter) + key)
      print(letter_index)
      result = result + alpha[letter_index]
    else:
      result = result + letter
  return result


def main():
  word = "Secret Mystery Message"
  encrypted = encrypt(3,word)
  print(word)
  print(encrypted) #should print "VHFUHW PBVWHUB PHVVDJH"

if __name__ == "__main__":
  main()


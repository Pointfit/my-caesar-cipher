from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
play = True

def caesar(direction, text, shift):
  change = ""
  for n in text:
    if n in alphabet:
      if direction == "encode":
        change += alphabet[alphabet.index(n) + shift]
      elif direction == "decode":
        change += alphabet[alphabet.index(n) - shift]
    else:
      change += n
  print(f"The {direction}d text is {change}")

while play:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) % 26
  
  caesar(direction, text, shift)
  proceed = input("Do you want to go again? Yes or no\n").lower()
  if proceed == "no":
    play = False
    print("Goodbye.")
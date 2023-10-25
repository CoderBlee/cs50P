message = input("snakeCase: ")

for letter in the message:
  if letter.isupper():
    message = message.replace(letter, "_" + letter.lower())
    
    print(message)
import time

input = input("Enter a phrase: ")
output = ""

characters = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


print(input)

for i in range(len(input)):
    for j in range(len(characters)):
      print(output+characters[j])
      time.sleep(0.01)
      if input[i] == characters[j]:
        output = output + characters[j]
      if output == input:
        break
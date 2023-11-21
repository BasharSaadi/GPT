# Character Level Language Model


with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
print("\n")
#print("The length of data in characters is: ", len(text))

# first 100 chars
#print(text[:1000])

# here all the unique characters in the file
chars = sorted(list(set(text)))
vocab_size = len(chars)
#print(''.join(chars))
#print(vocab_size)

# create a mapping from characters to integers (Tokaenization)
stoi = { ch:i for i, ch in enumerate(chars)}
itos = { i:ch for i,ch in enumerate(chars)} 
encode = lambda s: [stoi[c] for c in s] # encoder: takes a string, outputs a list of integers
decode = lambda l: ''.join([itos[c] for c in l]) # decoder: takes a list of integers, outputs a string

print(encode('I am Bashar, the Warrior of Light'))
print(decode(encode('I am Bashar, the Warrior of Light')))
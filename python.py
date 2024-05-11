import random
'''
def generate_random_text():
    text = ''
    # Define characters you want to include in the random text
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-'
    for i in range(7):
        text = text + random.choice(characters)
    print(text)

#random_text = generate_random_text()
generated_texts = []

def generate_unique_random_text():
    while True:
        text = generate_random_text()
        if text not in generated_texts:
            generated_texts.append(text)
            print(text)
            print(generated_texts)
#generate_unique_random_text()
print(generated_texts)

# Example usage:
for i in range(1): # Generate 10 unique random texts
    random_text = generate_unique_random_text()
    print(random_text)




'''

import random

f=open('Urlname.txt','w+')
s=f.read()


def generate_random_text():
    text = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-'
    for i in range(6):
        text += random.choice(characters)
        return text
       
generated_texts = []
#generate_random_text()

def generate_unique_random_text():
    while True:
        text = generate_random_text()
        if text not in s:
            f.write(text)
            return text
a=''
# Example usage:
for _ in range(6):
    random_text = generate_unique_random_text()
    print(random_text)
    a=a+random_text
print(a)

f.close()

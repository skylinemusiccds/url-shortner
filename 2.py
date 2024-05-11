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

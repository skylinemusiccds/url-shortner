#                          URL Shortner Service In Python

def custom_url_name_function():
    customurlname = input("Enter your Custom Url Name: ")
    url_file=open(f"./RidirectUrl/{customurlname}.html",'w+')
    #url_file.write(url_code)
    url_file.write(f'<!DOCTYPE html><html><script>window.location.href = "{redirect_url}" ;</script></html>')
    url_file.close()
    final_url=f'uni.verse/{customurlname}'
    print(final_url)
    #while True:
        #customurlname = input("Enter your Custom Url Name: ")
        #exists=open(f"./RidirectUrl/{customurlname}.html")
        #if exists:
        #    print("Entered Custom Name Is Not Available\nTry Again With Different Name")
        #else:
            

def random_url_name_function():
    import random
    file=open('Urlname.txt','w+')
    s=file.read()
    def generate_random_text():
        text = ''
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-'
        for i in range(6):
            text += random.choice(characters)
            return text
    generated_texts = []
    
    def generate_unique_random_text():
        while True:
            text = generate_random_text()
            if text not in s:
                file.write(text)
                return text
    randomurlname=''
    for _ in range(6):
        random_text = generate_unique_random_text()
        randomurlname=randomurlname+random_text
    file.close()

    final_url=f'uni.verse/{randomurlname}'
    url_file=open(f"./RidirectUrl/{randomurlname}.html",'w+')
    #url_file.write(url_code)
    url_file.write(f'<!DOCTYPE html><html><script>window.location.href = "{redirect_url}" ;</script></html>')
    print(final_url)
    url_file.close()

def url_shorting_function():
    #redirect_url = input("Enter Your Url: ")
    #if redirect_url.startswith('https://'):
    #    redirect_url=redirect_url
    #else:
    #    redirect_url='https://'+redirect_url
    url_code = f'<!DOCTYPE html><html><script>window.location.href = "{redirect_url}" ;</script></html>'
    ask = input('Want Custom Url Ridirect Name (Y/N): ')
    if ask in 'Yy':
        custom_url_name_function()
    else:
        random_url_name_function()
redirect_url = input("Enter Your Url: ")
if redirect_url.startswith('https://'):
        redirect_url=redirect_url
else:
    redirect_url='https://'+redirect_url
url_shorting_function()

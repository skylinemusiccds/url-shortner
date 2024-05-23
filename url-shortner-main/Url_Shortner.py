#                          URL Shortner Service In Python

import os
import qrcode

def custom_url_name_function():
    while True:
        customurlname = input("Enter your Custom Url Name: ")
        folder_path = f'./RidirectUrl/{customurlname}'
        if os.path.exists(folder_path):
            print(" 😢😢 Custom Name Not Available 😢😢")
        else:
            break
    os.makedirs(folder_path)
    with open(f"./RidirectUrl/{customurlname}/index.html", 'w+') as url_file:
        print("🤗🤗 File created successfully. 🤗🤗")
        url_file.write(f'<html><script>window.location.href = "{redirect_url}" ;</script></html>')
        url_file.close()
        final_url=f'127.0.0.1:8000/{customurlname}'
        print(f"🎊 🎉 🎊 🎉 🎊 🎉 🎊 🎉 🎊 🎉\n\nYour Shorten URL: {final_url}\n\n 🎊 🎉 🎊 🎉 🎊 🎉 🎊 🎉 🎊 🎉")
        generate_qr_code(final_url,f"./RidirectUrl/{customurlname}/{customurlname}.png")
            

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
    randomurlname = ''
    for _ in range(6):
        random_text = generate_unique_random_text()
        randomurlname=randomurlname+random_text
    file.close()

    final_url = f'localhost:8000/{randomurlname}'
    folder_path = f'./RidirectUrl/{randomurlname}'
    os.makedirs(folder_path)
    url_file = open(f"./RidirectUrl/{randomurlname}/index.html",'w+')
    url_file.write(f'<html><script>window.location.href = "{redirect_url}" ;</script></html>')
    print(f"🎊 🎉 🎊 🎉 🎊 🎉 🎊 🎉 🎊🎉\n\nYour Shorten URL: {final_url}\n\n 🎊 🎉 🎊 🎉 🎊 🎉 🎊 🎉 🎊 🎉")
    generate_qr_code(final_url,f"./RidirectUrl/{randomurlname}/{randomurlname}.png")
    url_file.close()

def url_shorting_function():
    ask = input('Want Custom Url Ridirect Name (Y/N): ')
    if ask in 'Yy':
        custom_url_name_function()
    else:
        random_url_name_function()

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10, border=4
        )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)


print('='*64)
print('='," "*(64//4),"UniVerse ShrinkEase"," "*(64//4+7),'=')
print('='*(64))


redirect_url = input("Enter Your Url: ")
if redirect_url.startswith('https://'):
        redirect_url=redirect_url
else:
    redirect_url='https://'+redirect_url
url_shorting_function()




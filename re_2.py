import re 

with open('Transecations.txt', encoding='UTF-8') as f :
    dates = re.findall(r'([\d.0-9]+)\/([\d.0-9])\/([\d.0-9]+)', f.read())
    print('===='*10 +'\n'+'Account Holders Name is : ')
    name = re.findall(r'\w+', f.read(), re.IGNORECASE)
    print(name)
    # else :
    #     print('Not Found')
    print('===='*10 +'\n'+'Dates are : ')
    for date in dates:
        print(date[0]+'-'+date[1]+'-'+date[2])


    
import re

import requests

links_passados = set()

conjunto_de_emails = set()

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}
#sucesso !!!
def pegador_de_semente(dork):
    resposta = requests.get('https://google.com/search', headers=header ,params={'q' : dork})
    cod = resposta.text
    primeiro = re.findall(r'(?<=href=["\'])https?:.+?(?=["\'])', cod)
    return primeiro


def escrever_txt(emails):
    for email in emails:
        arquivo = open('emails.txt','a')
        arquivo.write(email)
        arquivo.write('\n')


print('''Py-Busca\n''')

dork = input('coloque a dork : ')
limite = int(input('coloque o limite da busca : '))
semente = pegador_de_semente(dork)

for i in range(limite):
    url = semente[0]
    try:
        req = requests.get(url, headers=header)
    except:
        semente.remove(url)
        links_passados.add(url)
        continue

    html = req.text
    links = re.findall(r'(?<=href=["\'])https?:.+?(?=["\'])', html)
    print ('Crawling:', url)

    emails = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.]+', html)

    semente.remove(url)
    links_passados.add(url)

    for link in links:
        if link not in links_passados and link not in semente:
            semente.append(link)

    for email in emails:
        conjunto_de_emails.add(email)

arquivo = open('emails.txt','w')
escrever_txt(conjunto_de_emails)
#print(conjunto_de_emails)
#fazer função que salva os txt
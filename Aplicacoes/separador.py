print ("Py-Separa\n")
palavra = input("Digite o provedor:")


#Achar emails
arq = open('emails.txt','r')
contador = 0
for linha in arq:
	linha = linha.rstrip()
	if palavra in linha:
		contador = contador +1
		

#Salvar e deletar duplicados
		arquivo = open('emails.txt','w')
		arquivo = open('emails.txt','a')
		arquivo.write(linha)
		arquivo.write('\n')

		print(linha)

print ("\nForam Retornados", contador, "emails")

c = input('')
#TCC BUNITO

arq.close()

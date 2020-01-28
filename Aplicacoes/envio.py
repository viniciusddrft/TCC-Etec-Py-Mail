import mimetypes
import os
import smtplib
import getpass

from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def adiciona_anexo(msg, filename):
	if not os.path.isfile(filename):
		return

	ctype, encoding = mimetypes.guess_type(filename)

	if ctype is None or encoding is not None:
		ctype = 'application/octet-stream'

	maintype, subtype = ctype.split('/', 1)

	if maintype == 'text':
		with open(filename) as f:
			mime = MIMEText(f.read(), _subtype=subtype)
	elif maintype == 'image':
		with open(filename, 'rb') as f:
			mime = MIMEImage(f.read(), _subtype=subtype)
	elif maintype == 'audio':
		with open(filename, 'rb') as f:
			mime = MIMEAudio(f.read(), _subtype=subtype)
	else:
		with open(filename, 'rb') as f:
			mime = MIMEBase(maintype, subtype)
			mime.set_payload(f.read())

		encoders.encode_base64(mime)
	mime.add_header('Content-Disposition', 'attachment', filename=filename)
	msg.attach(mime)
print('''Py-Envio
''')
try:
	print('====' * 10)
	meu_email = input('[*]Seu Gmail: ')
	print('====' * 10)
	senha = getpass.getpass('[*]Sua senha: ')
	print('====' * 10)
	assunto = input('[*]Assunto: ')
	print('====' * 10)
	menssagem = input('[*]Menssagem: ')
	print('====' * 10)
	anexo = input('[*]coloque o nome do arquivo de anexo(opcional): ')
	print('====' * 10)
	quantidade = int(input('[*]Quantidade de pessoas que vao receber os emails: '))
except:
	print('erro')
#O naruto pode ser duro as vezes...
#-----------------------------------------
arquivo = open('emails.txt','r')
emails = arquivo.read()
emails = emails.split()
i = 0
#-----------------------------------------
while (i < quantidade):
	msg = MIMEMultipart()
	msg['From'] = meu_email
	msg['To'] = ', '.join(emails[i])
	msg['Subject'] = assunto

# Corpo da mensagem
	msg.attach(MIMEText(menssagem, 'html', 'utf-8'))

# Arquivos anexos.
	adiciona_anexo(msg, anexo)
	raw = msg.as_string()

	smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp.login(meu_email, senha)
	print('login')
	smtp.sendmail(meu_email, emails[i], raw)
	print('[{}]Enviando para : {}'.format(i,emails[i]))
	i += 1
	smtp.quit()


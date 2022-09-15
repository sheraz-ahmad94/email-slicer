import valid_email

def email_slicer(email):
    (username, domain) = email.split("@")
    (domain, extension) = domain.split(".")

    print('Username:', username, '\nDomain:', domain, '\nExtension:', extension)

while True:
    email = input('Enter an Email (-1 to Exit): ')
    if email == '-1':
        exit()
    elif(valid_email.email_checker(email)):
        email_slicer(email)
    else:
        print('Enter a Valid Email...')
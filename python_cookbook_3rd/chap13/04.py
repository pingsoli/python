# 13.4 Prompting for a Password at Runtime

import getpass

#user = getpass.getuser()    # Won't prompt to input username,
                            # get the name from local machine
#passwd = getpass.getpass()

# if svc_login(user, passwd):  # You must write svc_login
#     print('user:', user)
#     print('passwd:', passwd)
#     print('Yay!')
# else:
#     print('Boo!')

#print('user:', user)
#print('passwd:', passwd)
# user: pingsoli
# passwd: what the fuck

# If you want to prompt inputing username, you can do like this.
user = input('Enter your username: ')
passwd = getpass.getpass()

print(user)
print('paaswd', passwd)

# Enter your username: pingsoli
# paaswd what the fuck

import os

user = os.environ['USERNAME']


def internet_check():
    if not os.path.exists('C:\\Users\\{0}\\Windows32\\i_v4'.format(user)):
        with open('C:\\Users\\{0}\\Windows32\\i_v4'.format(user), 'w')as internetwarning:
            internetwarning.close()

        return 'id'
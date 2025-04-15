import webbrowser
while 1 == 1:
    ans = input('would you like to install the apps? \n [y / n] \n ')
    if ans == 'y':
        webbrowser.open('https://github.com/rickastley10/allinstaller/archive/refs/heads/main.zip')
        quit()
    elif ans == 'n':
        quit()

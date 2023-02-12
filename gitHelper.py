import subprocess
import os
choice = input("Que voulez-vous faire ?\n 1 - commit et push sur la branche actuelle \n 2 - git  \n 4 - test3 \n 5 - Créer une nouvelle branche \n 6 - git push setupstream \n 7 - choix de branch + git merge \n 8 - test7 \n 9 - test8 \n 0 - pull depuis master \n q - Quitter \n Votre choix :")

if choice == "1":
    message = input("Entrez le message de commit : ")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    push = input("Commit effectué, veut tu push ? \n y/n : ")
    while push != "y" and push != "n":
        push = input("y/n : ")
    if push == "y":
        subprocess.run(["git", "push"])
    elif push == "n":
        print("Ok, n'oublie pas de push avant de partir !")
elif choice == "2":
    current_directory = os.getcwd()
    print("The current working directory is:", current_directory)
elif choice == "3":
    print("test3")
elif choice == "4":
    print("test4")
elif choice == "5":
    branchName = str(input("Entrez le nom de la branche : "))
    subprocess.run(["git", "checkout", "-b", branchName ])
elif choice == "6":
    branchName = str(input("Entrez le nom de la branche : "))
    subprocess.run(["git", "push", "--set-upstream", "origin", branchName ])
elif choice == "7":
    choiceForPull = input("Voulez vous pull avant de merge ? \n y/n : ")
    while choiceForPull != "y" and choiceForPull != "n":
        choiceForPull = input("y/n : ")
    if choiceForPull == "y":
        subprocess.run(["git", "pull"])
        choiceBranch = input("Voulez vous merge sur la branche actuelle ? \n y/n : ")
        while choiceBranch != "y" and choiceBranch != "n":
            choiceBranch = input("y/n : ")
        if choiceBranch == "y":
            subprocess.run(["git", "merge"])
        elif choiceBranch == "n":
            branchName = str(input("Entrez le nom de la branche : "))
            subprocess.run(["git", "checkout", branchName ])
            subprocess.run(["git", "merge"])
    elif choiceForPull == "n":
        choiceBranch = input("Voulez vous merge sur la branche actuelle ? \n y/n : ")
        while choiceBranch != "y" and choiceBranch != "n":
            choiceBranch = input("y/n : ")
        if choiceBranch == "y":
            subprocess.run(["git", "merge"])
        elif choiceBranch == "n":
            branchName = str(input("Entrez le nom de la branche : "))
            subprocess.run(["git", "checkout", branchName ])
            subprocess.run(["git", "merge"])
elif choice == "8":
    print("test8")
elif choice == "9":
    print("test9")
elif choice == "0":
    subprocess.run(["git", "pull"])
elif choice == "q":
    print("Bye")
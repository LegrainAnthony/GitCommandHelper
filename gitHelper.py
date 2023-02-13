import subprocess
import os
choice = input("Que voulez-vous faire ?\n 1 - commit et push sur la branche actuelle \n 2 - Créer une nouvelle branch  \n 3 - git push setupstream \n 4 - choix de branch + git merge \n 5 - Voir la branch actuellement \n 6 - git pull \n 7 - changer de branch \n q - Quitter \n Votre choix :")

def gitHelper():

    def get_current_branch():
        process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
        branch_name, _ = process.communicate()
        return branch_name.decode().strip()

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
        branchName = str(input("Entrez le nom de la branche : "))
        subprocess.run(["git", "checkout", "-b", branchName ])
    elif choice == "3":
        currentBranch = str(get_current_branch())
        print("La branche actuelle est : ", currentBranch)
        subprocess.run(["git", "push", "--set-upstream", "origin", currentBranch ])
    elif choice == "4":
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
                currentBranch = get_current_branch()
                branchName = str(input("Entrez le nom de la branche : "))
                subprocess.run(["git", "checkout", branchName ])
                mergeLastBranch = input("Voulez vous merge depuis la branche depuis la quel vous venez? \n y/n : ")
                while mergeLastBranch != "y" and mergeLastBranch != "n":
                    mergeLastBranch = input("y/n : ")
                if mergeLastBranch == "y":
                    subprocess.run(["git", "merge", currentBranch])
    elif choice == "5":
        print(get_current_branch())
    elif choice == "6":
        origin = input("Voulez vous pull depuis main ? \n y/n : ")
        while origin != "y" and origin != "n":
            origin = input("y/n : ")
        if origin == "y":
            subprocess.run(["git", "pull", "origin", "main"])
        elif origin == "n":
            origin = input("Depuis quelle branche voulez vous pull ? : ")
        subprocess.run(["git", "pull", "origin", origin])
    elif choice == "7":
        branchName = str(input("Entrez le nom de la branche : "))
        subprocess.run(["git", "checkout", branchName ])
    elif choice == "q":
        print("Bye")

if __name__ == "__main__":
    gitHelper()
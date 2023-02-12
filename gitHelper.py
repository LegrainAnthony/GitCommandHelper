import subprocess


choice = input("Que voulez-vous faire ?\n 1 - commit et push sur la branche actuelle \n 2 - test2 \n 4 - test3 \n 5 - test4 \n 6 - test5 \n 7 - test6 \n 8 - test7 \n 9 - test8 \n 0 - test9 \n q - Quitter \n Votre choix :")

if choice == "1":
    message = input("Entrez le message de commit : ")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push"])
elif choice == "2":
    print("test2")
elif choice == "3":
    print("test3")
elif choice == "4":
    print("test4")
elif choice == "5":
    print("test5")
elif choice == "6":
    print("test6")
elif choice == "7":
    print("test7")
elif choice == "8":
    print("test8")
elif choice == "9":
    print("test9")
elif choice == "0":
    print("test10")
elif choice == "q":
    print("Bye")
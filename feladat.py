import random
import time
import os

def tisztit():
    os.system('cls' if os.name == 'nt' else 'clear')

def orosz_rulett():
    tisztit()
    print("=== Orosz Rulett ===")
    input("Nyomj Entert a játék indításához...")
    
    patron_pozicio = random.randint(1, 6)
    jelenlegi_kamra = 1

    while True:
        tisztit()
        print(">>> Meghúzod a ravaszt... 🔫")
        time.sleep(1)

        if jelenlegi_kamra == patron_pozicio:
            print("\n💥 BAMM! Meghaltál.")
            break
        else:
            print("\nKatt... élsz még. 😅")
            jelenlegi_kamra += 1
            if jelenlegi_kamra > 6:
                jelenlegi_kamra = 1
            cont = input("Tovább játszol? (i/n): ")
            if cont.lower() != 'i':
                print("Kiléptél a játékból. 👋")
                break

if __name__ == "__main__":
    orosz_rulett()

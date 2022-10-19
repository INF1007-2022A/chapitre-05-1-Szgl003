#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    number = abs(number)

    return number


def use_prefixes() -> List[str]:

    liste_nom = []
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    for lettre in prefixes:

        liste_nom.append(lettre + suffixe)


    return liste_nom


def prime_integer_summation() -> int:
    prime = [2,3,5]
    number = 6

    while len(prime) < 100:
        is_prime = True
        for i in range(2, number//2):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:

            prime.append(number)

        number+=1

    return sum(prime)



def factorial(number: int) -> int:
   valeur_factoriel = 1

   for i in range (2, number+1):

       valeur_factoriel *= i

   return valeur_factoriel


def use_continue() -> None:
    for num in range(1, 11):
        if num ==5:
               pass
        print(num)




def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance = []
    for liste in groups:

        if 25 in liste:
            acceptance.append(True)
            continue

        if len(liste) > 10 or len(liste) < 3:
               acceptance.append(False)
               continue

        if min(liste) < 18:
                acceptance.append(False)
                continue



        if max(liste) > 70 and 50 in liste:
                acceptance.append(False)
                continue

        acceptance.append(True)
    return acceptance





def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()

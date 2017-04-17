"""CP1404/CP5632 Practical - Do it from scratch Exercise - test."""

from guitars import Guitar

def main():
    guitars = []
    count = 0
    valid_input = False
    while not valid_input:
        print("My guitars")
        name = input("Name: ")
        if name == "":
            break
        year = input("Year: ")
        cost = input("Cost: ")
        guitar_entered = Guitar(name, year, cost)
        guitars.append(Guitar(name, year, cost, guitar_entered.is_vintage()))
        print(guitar_entered)
    print("Thease are my guitars:")
    for row in guitars:
        count += 1
        print("Guitar" + count + ":  {:<20}  ({}), worth ${:10,.2f} ({})".format(*row))

main()
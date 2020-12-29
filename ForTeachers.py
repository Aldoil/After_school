import math
def pri(var, kom="Sekwencja zawiera: "):
    """ function for printing values """
    print(kom)
    for i in var:
        print(i, end=' ')

def average(arg):
    """ function for calculate the average """
    l = 0
    for i in arg:
        l += i
    l = l/len(arg)
    return l

def median(arg):
    """ function for calculate the median """
    arg.sort()
    if len(arg) % 2 == 0:
        c = len(arg) / 2
        med = (arg[int(c + 0.5)] + arg[int(c - 0.5)]) / 2
        return med
    else:
        return arg[int(len(arg) / 2)]


def standard_deviation(arg, s):
    """ function for calculate the standard deviation """
    l =0
    for i in arg:
        l += (i-s)**2
    std = math.sqrt((l/len(arg)))
    return round(std,2)



def main():
    subjects = set(['polski', 'matematyka'])
    pri(subjects, "Przedmioty, które znajdują się w liście: ")

    print("\nAby zakończyć dodawanie przedmiotu naciśnij Enter.")
    while True:
        subject = input("Podaj nazwę przedmiotu: ")
        if len(subject):
            if subject in subjects:
                print("Podany przedmiot znajduje sie juz w zbiorze.")
            subjects.add(subject)
        else:
            pri(subjects, "\nPodane przedmioty: ")
            subject = input("\nWybierz przedmiot, dla którego chcesz wprowadzić oceny. ")
            if subject not in subjects:
                print("Brak podanego przedmiotu w zbiorze. Dodaj nowy przedmiot jeśli chcesz.")
            else:
                break

    grades = []
    grade = 0
    print("\nAby przerwać wprowadzanie ocen napisz 0.")

    while not grade:
        try:
            grade = int(input("Podaj ocenę (1-6): "))
            if (grade > 0 and grade < 7):
                grades.append(float(grade))
            elif grade == 0 :
                break
            else:
                print("Błędna ocena.")
            grade = 0

        except ValueError:
            print("Błędne dane!")

    pri(grades, subject.capitalize() + " - wprowadzone oceny: ")
    av = average(grades)
    med = median(grades)
    std = standard_deviation(grades, av)
    print("\nŚrednia: {:.2f}".format(av))
    print("Mediana: {0:.2f}\nOdchylenie: {1:.2f}".format(med, std))

if __name__ == '__main__':
    main()



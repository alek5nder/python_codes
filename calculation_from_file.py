import math

# Funkcja do obliczenia wartości y(x)
def calculate_y(x1, x2, x3):
    return math.exp(-( ( (x1 - x2) / x3)**2) )

# Otwarcie pliku danych do odczytu
try:
    with open("Dane.dat", "r", encoding="ISO-8859-1") as file:
        lines = file.readlines()
        # Otwarcie pliku wynikowego do zapisu
        with open("Wyniki.dat", "w") as output_file:
            output_file.write('"Opis", "y(x)"\n')
            error_count = 0
            for line in lines[1:]:  # Pominięcie nagłówka
                try:
                    data = line.strip().split(',')
                    opis = data[0].strip('"')
                    x1 = float(data[1])
                    x2 = float(data[2])
                    x3 = float(data[3])
                    y = calculate_y(x1, x2, x3)
                    output_file.write(f'"{opis}", {y}\n')
                except (IndexError, ValueError):
                    error_count += 1
        if error_count > 0:
            print(f"Wystąpiło {error_count} błędów w danych.")
        else:
            print("Przetwarzanie danych zakończone bez błędów.")
except FileNotFoundError:
    print("Nie można znaleźć pliku 'Dane.dat'.")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
finally:
    print("Koniec programu.")

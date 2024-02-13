import random

ROWS=3
COLS=3
symbol_count={"A":2,"B":4,"C":6,"D":8}

MAX_LINES = 3
MAX_BET=100
MİN_BET=10


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    colums=[]
    for _ in range(cols):
        colum=[]
        current_symbol=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbol)
            current_symbol.remove(value)
            colum.append(value)

        
        colums.append(colum)
    return colums

def print_slot_machine(colums):
    for row in range(len(colums[0])):
        for i,colum in enumerate(colums):
            if i!= len(colums) -1:
                print(colums[row],"|")
            else:
                print(colums[row])



def depozito():
    while True:
        amount =input("Oynicağin Parayi Gir: $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Paraniz 0 dan büyük olmali")
        else:
            print("sayi giriniz.")
    return amount  #fonksiyonu tanımladın ve amount değerini return yaptın neden amount değerini başka bir yerde bir daha kullanabilmek için

def get_number_of_lines():
    while True:
        lines =input(f"Oynicağin Sira Sayisi: 1-{MAX_LINES}:  ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("doğru değerleri giriniz")
        else:
            print("sayi giriniz.")
    return lines

def get_bet():
    while True:
        amount =input("Oynicağin Parayi Gir: $")
        if amount.isdigit():
            amount = int(amount)
            if MİN_BET<= amount <=MAX_BET:
                break
            else:
                print(f"betiniz: {MİN_BET}-{MAX_BET} arasinda olmali..")
        else:
            print("sayi giriniz.")
    return amount




def main():
    balance=depozito()
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print("paraniz kadar bet oynayin")
        else:
          break
    print(f"oynicak paran=$ {balance}  ,  oynadiğin bet=$ {total_bet}  ")

    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)

main()

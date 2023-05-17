#Elabore um algoritmo que obetenha o mínimo múltiplo comum(MMC) entre dois numeros fornecidos.
first_number = int(input())
second_number = int(input())
multiplication = first_number*second_number
number_mmc = 0
for mmc in range (first_number, multiplication+1):
  if mmc%first_number == 0 and mmc% second_number == 0 :
    number_mmc = mmc
    break
print(number_mmc)
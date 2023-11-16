def shift_list_elements(lst, n):
    n = n % len(lst)  # Modulus alarak etkili kaydırmayı hesapla
    shifted_list = lst[-n:] + lst[:-n]  # Listeyi kaydır

    return shifted_list

# Kullanıcıdan liste girişi al
input_list = input("Enter a list of numbers separated by spaces: ")
# Girişi boşluklara göre böl ve integer'a dönüştür
input_list = [int(x) for x in input_list.split()]

# Kullanıcıdan kaydırma miktarı girişi al
shift_value = int(input("Enter the shift value: "))

# Kaydırma işlemi
output = shift_list_elements(input_list, shift_value)

# Sonucu yazdır
print(f"Input: {input_list}, Shift: {shift_value}, Output: {output}")

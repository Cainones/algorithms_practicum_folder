def huffman_decode(code_dict, encoded_str):
    #-Создание словаря для кодов символов.
    reverse_code_dict = {v: k for k, v in code_dict.items()}
    
    current_code = ''
    decoded_str = ''
    
    #-Проще всего пройти по каждому биту в закодированной строке.
    for bit in encoded_str:
        current_code += bit
        #-Если текущий код есть в словаре, переводим символ в результат.
        if current_code in reverse_code_dict:
            decoded_str += reverse_code_dict[current_code]
            current_code = ''
    
    return decoded_str

code_dict = {
    ' ': '1011',
    '.': '1110',
    'D': '1000',
    'c': '000',
    'd': '001',
    'e': '1001',
    'i': '010',
    'm': '1100',
    'n': '1010',
    'o': '1111',
    's': '011',
    'u': '1101'
}

encoded_str = '100011110001001101000111111011001010011000010110011010111110'

decoded_str = huffman_decode(code_dict, encoded_str) #-Декодирование строки.
print(decoded_str)
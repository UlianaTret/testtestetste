def open_key(s_key, c, N):  #создаём открытый ключ на основе закрытого
   p_key = []
   for s in s_key:
       p_key.append(pow(s*c, 1, N))
   return p_key

def encryption(text, p_key):  #шифрование символа
   text = list(bin(text))[2:]
   text.reverse()
   p_key.reverse()
   ciphertext = 0
   for i in range(len(text)):
       ciphertext += int(text[i]) * p_key[i]
   p_key.reverse()
   return ciphertext

# return (d, x, y) for ax - by = d  #алгоритм Евклида
def gcdex(a, b):
   if b == 0:
       return a, 1, 0
   else:
       d, x, y = gcdex(b, a % b)
       return d, y, x - y * (a // b)

def decryption(ciphertext, s_key, c, N):  #дешифровка рюкзака
   text = []
   res = gcdex(c, N)
   print(res)
   if res[0] == 1:  #проверка на наименьший общий делитель равный единице
       s = N+res[1]
   cipher = pow(ciphertext*s, 1, N)
   s_key = list(s_key)
   s_key.reverse()
   for k in s_key:
       if cipher-k >= 0:
           text.append(1)
           cipher -= k
       else:
           text.append(0)
   text.reverse()
   return text

def key(filename):  #помещаем параметры работы из файла в переменные
   f_inp = open(filename, 'r')
   key = []
   for line in f_inp.readlines():
       key.append(line)
   c = int(key[0])
   N = int(key[1])
   P = list((key[2].split(' ')))
   for i in range(len(P)):
       P[i] = int(P[i])
   f_inp.close()
   return c, N, P

c, N, P = key('key.txt')
action = input('Выберите шифрование или дешифровку: ')  #выбираем ход работы
if action == 'Шифрование':  #для шифрования вводим “Шифрование”
   openkey = open_key(P, c, N)  #помещаем открытый ключ в переменную
   f_inp = open('text.txt', 'r')  #открываем файл с исходным текстом
   f_out = open('enc.txt', 'w')  #открываем файл, куда поместим зашифрованный текст
   for char in f_inp.read():  #цикл для посимвольного шифрования из файла
       enc_text = encryption(ord(char), openkey)
       f_out.write(str(enc_text) + '\n')  #запись зашифрованного текста
   f_inp.close()
   f_out.close()
elif action == 'Дешифровка':  #для дешифровки вводим “Дешифровка”
   f_inp = open('enc.txt', 'r')  #открываем файл с зашифрованным текстом
   f_out = open('dec.txt', 'w')  #открываем файл, куда поместим дешифрованный текст
   for line in f_inp.readlines():  #цикл для посимвольной дешифровки и записи
       dec_text = decryption(int(line), P, c, N)
       dec = 0
       for i in range(len(dec_text)):  #перевод в буквы
           dec += (2**(7-i)) * dec_text[i]
       dec = int(dec)
       f_out.write(chr(dec))  #запись в файл
   f_inp.close()
   f_out.close()


#Goal: remove vowels unless they start the word, remove consecutive letters. 

f = 'Hello everybody. I wanted to say something. If it were true that life had meaning, then life must have a higher power as meaning is constructed through being.'

def vowel_remove(text):
    new_text = ''
    for char in text:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
             char = ''
             new_text += char
        new_text += char
    return new_text

def vowel_remove_mod(text):
    text = text.lower()
    end_text = text[::-1]
    ind = 0 
    new_text = ''
    while ind != -1:
        word = text[ind:ind + 2]
        for char in text[ind + 2:text.find(' ', ind + 1)]:
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                char = ''
                word += char
            else:
                word += char
        new_text += word
        ind = text.find(' ', ind + 1)
    return new_text + end_text[0]

def cons_remove(text):
    count = -1
    new_text = ''
    for char in text:
        if char == text[count]:
            char = ''
            new_text += char
            count += 1
        else:
            new_text += char
            count += 1
    return new_text

def polish(text):
    inc_text = vowel_remove_mod(cons_remove(text))
    first_word = inc_text[0:inc_text.find(' ')]
    first_letter = first_word[0]
    rest_word = vowel_remove(first_word[1::])
    new_word = first_letter + rest_word
    new_text = new_word + inc_text[inc_text.find(' ')::]
    return new_text

print(polish(f))
# print(vowel_remove(f))
#--------------------

#Goal: Prime Number
def prime(maxval):
    lst = []
    for val in range(1, maxval):
        count = 0
        for fac in range(2,val):
            if val % fac == 0:
                break
            else:
                count += 1 
        if count == val-2:
            lst.append(val)
    return lst

def special_prime(lst):
    frst_ind = 0
    scnd_ind = 1
    new_lst = []
    x = 0
    while x + 1 < len(lst):
        check_num = lst[frst_ind] + lst[scnd_ind] + 1
        if check_num in lst:
            new_lst.append(check_num)
            frst_ind += 1
            scnd_ind += 1 
            x += 1
        else:
            frst_ind += 1
            scnd_ind += 1 
            x += 1
    return new_lst

#mx_val = 1000
#print(prime(mx_val))
#print(special_prime(prime(mx_val)))
#print(len(special_prime(prime(mx_val))))
#print(len(special_prime(special_prime(prime(mx_val)))))

#--------------------

#Goal: Dice roller- takes number of faces, number of rolls, number of dice
import random
def roll(num_rolls, *args):
    lst = []
    count = 0
    while count != num_rolls:
        for arg in args:
            lst.append(random.randint(1,arg))
        count += 1
    return sum(lst)
#print(roll(1,3,6,7,20,3,12))


import random
import time
start_time = time.time()
vowels = ['a', 'e', 'i', 'o', 'u']


def vowelCheck(char: chr) -> bool:
    for vowel in vowels:
        if(char.lower() == vowel):
            return True

    return False


def Change() -> bool:
    return random.randint(0, 1)


#key words generating are teacher- Good- student
encryptedMessage = "Yiov laeuzwj-klavifl jadiliofkzih, uzijaulejirev tq zayz denedk ix udekifekk, hdaqk af aulinw jodw af lza venediheifl ax tilz laauzejk afv kluviflk, ozauz uifljitulek lo kluveflk’ kouiad-weoliofad, tazaniojad, afv auaveeiu avbikleifl"


def countingVowels(msg: str) -> int:
    c: int = 0

    for var in msg:
        if var.lower() != ' ':
            if(vowelCheck(var)):
                c += 1

    return c

index: int = 8

encryptedMessage = encryptedMessage.replace("-", " ")
encryptedMessage = encryptedMessage.replace("’", "")
encryptedMessage = encryptedMessage.replace(",", "")
flag: bool = False
VowelsCount: int = countingVowels(encryptedMessage)

iteration: int = 0
print()

while not flag:
    for y in range(VowelsCount*5):
        iteration += 1
        guessedMessage = ''

        for var in encryptedMessage:
            var = var.lower()
            if var != ' ':
                if(vowelCheck(var)):
                    if Change():
                        var = random.choice(vowels)
                    else:
                        var = var
                else:

                    if ord(var)+index <= 122:
                        var = chr(ord(var)+index)
                    else:
                        var = chr(ord(var)+index-26)

            guessedMessage = guessedMessage + var


        if 'teacher' in guessedMessage:
            print("Teacher flag in message after", iteration, " no of iterations")
            print("Decrytped Message now is : ", guessedMessage)
            flag = True

        if 'good' in guessedMessage and 'student' in guessedMessage:
            print("student and good flag in message after ", iteration, " no of iterations")
            print("Decrytped Message now is : ", guessedMessage)
            flag = True
        else:
            print("Not found. Founding in process...")

        
        if flag:
            break

print("Time taken by the algorithm program %s seconds ::: " % (time.time() - start_time))

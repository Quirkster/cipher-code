import pyperclip, sys, random
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
    myMessage = 'If a man is offred a fact which goes against his instincts, he will scrutinize it closely, unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained this way. Betrand Russel'
    myKey ='LWOAYUISVKMNXPBDCRJOEGHZ'
    myMode = 'encrypt'
    if keyIsValid(myKey):
        sys.exit('There is an error in the key or symbol set.')
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is: '% (myMode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard.')
def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    return keyList == lettersList
def encryptMessage(key,message):
    return translatedMessage(key,message,'encrypt')
def translatedMessage(key,message,mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA
    for symbol in message:
        if symbol.upper in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated
def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return''.join(key)
if __name__ == '__main__':
    main()

import hashlib


dictionary = " /usr/share/dict/words"
crackme = "PATH TO CRACKME" #PATH to the text file we want to crack.


def Brutus():

    passToCrack = hashlib.sha256()
    
    #Reads + Stores the crack me text
    with open (crackme) as c:
        hashedPassword = c.read().split()

    #reads and parses the dictionary file. Puts everyword into a list.
    with open(dictionary) as f:
        words = f.read().split()

    #opens the file and sets it up 
    cracked = open('cracked.txt','w')


    #stores the password hash in an array. first index is the username the second the hash.
    usersAndPassHashed = ['','','','','','']
    for i in hashedPassword:
        usersAndPassHashed[i] = i.split(':')

        for word in words: #Compares the hash file recieved with the one we just generate. Returns if the word is the same.   
        
            #Hash every seven char word from /usr/share/dict/words (Linux or Mac)
            #which gets the first letter capitalized and a 1-digit number appended
            if len(word)==7 and word[0].isupper() and word[-1].isDigit():
                if Compare(usersAndPassHashed[i][1],passToCrack.update(word)):
                    print (usersAndPassHashed[i][1] + ":" + word+"\n")
                    cracked.write(usersAndPassHashed[i][1] + ":" + word +"\n")

#how to brute force numbers
            #Hash every four digit password with at least one of the following
            #special characters in the beginning: *, ~, !, #.
            elif word[0]=="*" and len(word)==5:
                if Compare(usersAndPassHashed[i][1],passToCrack.update('*' + word)):
                    print (usersAndPassHashed[i][1] + ":" + word+"\n")
                    cracked.write(usersAndPassHashed[i][1] + ":" + word+"\n")
        
            elif word[0]=="~" and len(word)==5:
                if Compare(usersAndPassHashed[i][1],passToCrack.update('~' + word)):
                    print (usersAndPassHashed[i][1] + ":~" + word+"\n")
                    cracked.write(usersAndPassHashed[i][1] + ":~" + word+"\n")
        
            elif word[0]=="!" and len(word)==5:
                if Compare(usersAndPassHashed[i][1],passToCrack.update('!' + word)):
                    print (usersAndPassHashed[i][1] + ":!" + word+"\n")
                    cracked.write(usersAndPassHashed[i][1] + ":!" + word+"\n")

            elif word[0]=="#" and len(word)==5:
                if Compare(usersAndPassHashed[i][1],passToCrack.update('#' + word)):
                    print (usersAndPassHashed[i][1] + ":#" + word+"\n")
                    cracked.write(usersAndPassHashed[i][1] + ":#" + word+"\n")


            #Similarly for all five char word from /usr/share/dict/words
            #with the letter 'a' in it which gets replaced with the special
            #character @ and the character ‘l’ is substituted by the number '1'
            elif len(word)==5:
                word.replace("a","@")
                word.replace("l","1")
                if Compare(usersAndPassHashed[i][1],passToCrack.update(word)):
                    print (usersAndPassHashed[i][0] + ":" + word+"\n")
                    cracked.write(usersAndPassHashed[i][0] + ":" + word+"\n")
        
            else:
                if Compare(usersAndPassHashed[i][1],passToCrack.update(word)):
                    print (usersAndPassHashed[i][0] + ":" + word+"\n")
                    cracked.write(usersAndPassHashed[i][0] + ":" + word+"\n")
  
    
    print("\nThat are all the passwords that were found.")
    cracked.close()        
    return 0
            
        

    

def Compare(hash, word):

    if hash == word:
        return True
    return False
     


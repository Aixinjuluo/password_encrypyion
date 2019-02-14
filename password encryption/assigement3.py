import hashlib


##create a digit.txt file to hash all the possible digit words and put them in to digit.txt file.
##write as <64 length string>:<password>
with open ("digit.txt", "w") as w:
    for i in range(1000000):
        x = str(i)
        six = x.zfill(6)
        PassW = hashlib.sha256(six.encode('utf-8')).hexdigest()
        w.write("{}:{}".format(PassW,six))
        w.write("\n")
    for i1 in range(100000):
        x = str(i1)
        five = x.zfill(5)
        PassW = hashlib.sha256(five.encode('utf-8')).hexdigest()
        w.write("{}:{}".format(PassW,five))
        w.write("\n")
    for f in range(10000):
        n = str(f)
        four = n.zfill(4)
        for Mark in ["*", "~", "!", "#"]:
            W = Mark + four
            PassW = hashlib.sha256(W.encode('utf-8')).hexdigest()
            w.write("{}:{}".format(PassW,W))
            w.write("\n")
    for i2 in range(1000):
        x = str(i2)
        three = x.zfill(3)
        PassW = hashlib.sha256(three.encode('utf-8')).hexdigest()
        w.write("{}:{}".format(PassW,three))
        w.write("\n")
    for i3 in range(100):
        x = str(i3)
        two = x.zfill(2)
        PassW = hashlib.sha256(two.encode('utf-8')).hexdigest()
        w.write("{}:{}".format(PassW,two))
        w.write("\n")
    for i4 in range(10):
        x = str(i4)
        one = x.zfill(2)
        PassW = hashlib.sha256(one.encode('utf-8')).hexdigest()
        w.write("{}:{}".format(PassW,one))
        w.write("\n")
        
##read the dicitionary,implement all the rules and up the hashed words into test.txt file.
##write as <64 length string>:<password>
with open("words.txt", "r") as Wordsfile, open("Writeword.txt", "w") as Writewords:
    Wordsfile_content = Wordsfile.read().splitlines()
    for line1 in Wordsfile_content:
        if (len(line1) == 7 ):
            line2 = line1.capitalize()
            for Num in range(0,10):
                i = str(Num)
                line3 = line2 + i
                m = hashlib.sha256(line3.encode('utf-8')).hexdigest()
                Writewords.write("{}:{}".format(m,line3))
                Writewords.write("\n")
                
        if (len(line1) == 5):
            R=line1.replace("a", "@").replace("l", "1")
            m = hashlib.sha256(R.encode('utf-8')).hexdigest()  
            Writewords.write("{}:{}".format(m, R))
            Writewords.write("\n")
        else:
             d = hashlib.sha256(line1.encode('utf-8')).hexdigest()
             Writewords.write("{}:{}".format(d,line1))
             Writewords.write("\n")
##read the test file.
##read each line,and split each by ":"
##put the parts if each line in to the list
##read the second part of each list and put them into input,txt file
##below is the way you read the dictionary. 
##with open ("/usr/share/dict/words", "r") as InputTestFile
with open("password.txt", "r") as InputTestFile, open ("input.txt", "w") as WriteInput:
    InputTestFile_content = InputTestFile.read().splitlines()
    for line5 in InputTestFile_content:
        au = line5.split(":")
        WriteInput.write(au[1])
        WriteInput.write("\n")

##compare all the result from test.txt and digit.txt with the hashing string from test file.
##if we find the same, we seve them into dound.txt file
##after finding all the same, we compare them with the original txt files to get the password.
with open ("input.txt", "r") as ReadInput, open ("Writeword.txt", "r") as ReadTestFile, open ("digit.txt", "r") as ReadDigitFile,\
     open ("output.txt", "w") as OutPutFile:
     ReadInput_content = ReadInput.read().splitlines()
     ReadTestFile_content = ReadTestFile.read().splitlines()
     ReadDigitFile_content = ReadDigitFile.read().splitlines()
     for line6 in ReadInput_content:
        for line7 in ReadTestFile_content:
             if line6 in line7:
                 OutPutFile.write("password: "+line7[65:])
                 OutPutFile.write("\n")
                 print("password: "+line7[65:]) 
     for line8 in ReadInput_content:
         for line9 in ReadDigitFile_content:
             if line8 in line9:
                 OutPutFile.write("password: "+line9[65:])
                 OutPutFile.write("\n")
                 print("password: "+line9[65:])

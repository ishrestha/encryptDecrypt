__author__ = 'Ivaan'
''' This is the first individual project. This is an encryption and decryption program that allows
user to use three types of method of encryption and decryption. The methods are caesar, substituti-
on and enigma. The user will be prompt to ask for a file name, encryption type and to decrypt or
to encrypt.
Prof. Coy and Dr. Tarplee'''


def caesar(file, s, enOrde):
    '''encrypts and decrypts file caesar method'''
    val = ""  # main place to store value
    main = list("abcdefghijklmnopqrstuvwxyz ")  # main list of words
    main_read = main[s:28]+ main[0:s]
    '''decryption'''
    if enOrde == "d":  # checks if it is decryption
        for eachLine in file:  # this section decrypts the file
            b= len(main_read)
            for i in range(0,b):
                if eachLine == main_read[i]:
                    val += main[i]
                elif eachLine not in main_read:
                    val += eachLine
                    break
                else:
                    pass
        fout = open("caesar-decrypted", "w")  # this section writes to the file
        fout.write(val)
        fout.close()
    '''encryption'''
    if enOrde == "e":  # checks if it is encryption
        for eachLine in file:  # this section encrypts the file
            b = len(main_read)
            for i in range(0,b):
                if eachLine == main[i]:
                    val += main_read[i]
                elif eachLine not in main:
                    val += eachLine
                    break
                else:
                    pass
        fout = open("caesar-encrypted", "w")  # this section writes to the file
        fout.write(val)
        fout.close()
    return val


def substitution(file, enOrde):
    '''encrypts and decrypts file using substitution method'''
    val=""
    main = list("abcdefghijklmnopqrstuvwxyz ")  # main list of letters
    main_read = list("ebcdifghojklmnupqrstavwxyz ")  # main list of substituted letters
    '''decryption'''
    if enOrde == "d":  # if decryption
        for eachLetter in file:  #this section decrypts the file
            b= len(main_read)
            for i in range(0,b):
                if eachLetter == main_read[i]:
                    val += main[i]
                elif eachLetter not in main_read:
                    val += eachLetter
                    break
                else:
                    pass
        fout = open("substitution-decrypted", "w")  # this section writes the string to new file
        fout.write(val)
        fout.close()
    '''encryption'''
    if enOrde == "e":  # if encryption
        for eachLetter in file:  # this section encrypts the file
            b = len(main_read)
            for i in range(0, b):
                if eachLetter == main[i]:
                    val += main_read[i]
                elif eachLetter not in main:
                    val += eachLetter
                    break
                else:
                    pass
        fout = open("substitution encrypted", "w")  # this section writes the string to new file
        fout.write(val)
        fout.close()
    return val  # returns val to function


def enigma(file, enOrde):
    '''encrypts and decrypts files using enigma method'''
    in_read = " gnuahovbipwcjqxdkryelszfmt"
    mid_read = " ejotychmrwafkpuzdinsxbglqv"
    out_read = " bdfhjlnprtvxzacegikmoqsuwy"
    count_in = 0
    count_mid = 0
    count_out = 0
    val = ""
    '''encryption'''
    if enOrde == "e":  # if encryption
        for eachLetter in file:  # reads each letter in a
             if eachLetter not in out_read:
                val += eachLetter
                count_in += 1
                in_read = in_read[-1] + in_read[:-1]  # rotates the inner ring
                if count_in%27 == 0:
                    count_mid += 1
                    count_in = 0
                    mid_read = mid_read[-1] + mid_read[:-1]  # rotates the mid ring
                    assert len(mid_read) == 27  # to test the length once it is rotated
                    if count_mid%27 == 0:
                        count_mid = 0
                        count_out += 1
                        out_read = out_read[-1]+ out_read[:-1]  # rotates the outer ring
                        assert len(out_read)== 27  # to test the length once it is rotated
                        if out_read%27 == 0:
                            out_read = 0
             else:
                i = in_read.find(eachLetter)  # index where eachLetter is in in_read
                get_in = out_read[i]  # get letter from index in out read and store in get_in
                j = mid_read.find(get_in)  # find in mid_read the get_in
                val += out_read[j]
                in_read = in_read[-1] + in_read[:-1]  # rotates the inner ring
                count_in += 1
                assert len(in_read)== 27   # to test the length once it is rotated
                if count_in%27 == 0:

                    count_mid += 1
                    count_in = 0
                    mid_read = mid_read[-1] + mid_read[:-1]  # rotates the mid ring
                    assert len(mid_read) == 27  # to test the length once it is rotated
                    if count_mid%27 == 0:
                        count_mid = 0
                        count_out += 1
                        out_read = out_read[-1]+ out_read[:-1]  # rotates the outer ring
                        assert len(out_read)== 27  # to test the length once it is rotated
                        if out_read == 27:
                            out_read = 0
        fout = open("3ring-encrypted","w")
        fout.write(val)
        fout.close()
    ''' Decryption'''
    if enOrde =="d":
        for eachLetter in file:
            if eachLetter not in out_read:
                val += eachLetter
                count_in += 1
                in_read = in_read[-1] + in_read[:-1]  # rotates the inner ring
                if count_in%27 == 0:
                    count_mid += 1
                    count_in = 0
                    mid_read = mid_read[-1] + mid_read[:-1]  # rotates the mid ring
                    assert len(mid_read) == 27  # to test the length once it is rotated
                    if count_mid%27 == 0:
                        count_mid = 0
                        count_out += 1
                        out_read = out_read[-1]+ out_read[:-1]  # rotates the outer ring
                        assert len(out_read)== 27  # to test the length once it is rotated
                        if out_read%27 == 0:
                            out_read = 0
            else:
                i = out_read.find(eachLetter)  # index where eachLetter is in out_read
                get_in = mid_read[i]  # get letter from index in mid read and store in get_in
                j = out_read.find(get_in)  # find in out_read the get_in
                val += in_read[j]
                in_read = in_read[-1] + in_read[:-1]  # rotates the inner ring
                count_in += 1
                assert len(in_read)== 27   # to test the length once it is rotated
                if count_in%27 == 0:

                    count_mid += 1
                    count_in = 0
                    mid_read = mid_read[-1] + mid_read[:-1]  # rotates the mid ring
                    assert len(mid_read) == 27  # to test the length once it is rotated
                    if count_mid%27 == 0:
                        count_mid = 0
                        count_out += 1
                        out_read = out_read[-1]+ out_read[:-1]  # rotates the outer ring
                        assert len(out_read)== 27  # to test the length once it is rotated
                        if out_read == 27:
                            out_read = 0
        fout = open("3ring-decrypted","w")
        fout.write(val)
        fout.close()
    return val


def main():
    loop =""
    while loop !="exit":  # loop begins to ask for file names
        fileName = input("Please input the file name?")
        loop = fileName
        if loop == "exit": #if loop is = "exit"
            print("Thank you for using the encryption")
            break  # it breaks the while loop
        s = 0
        enType = input("Please input the encryption type caesar, substitution or enigma?").lower()
        enOrde = input("Please input e for encryption or d for decryption?").lower()
        fin = ""
        if enType == "caesar":  # if encryption type is caesar asks for number of substitution
            s = int(input("Please input the number of place for substitution?"))
        try:  # try catch to check if file exists
            fin = open(fileName)
        except IOError:
            print("File could not opened.")
        readfile = fin.read()  # reads the file
        readfile.lower()
        if enType == "caesar":  # this sections checks which method was used.
            caesar(readfile, s, enOrde)
        elif enType == "substitution":
            substitution(readfile, enOrde)
        elif enType == "enigma":
            enigma(readfile, enOrde)
        else:  # if does not match prints it does not match
            print("That's not a encryption or decryption")



'''Standard boilerplate'''
if __name__== '__main__':
    main()

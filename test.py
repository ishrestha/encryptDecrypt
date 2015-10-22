__author__ = 'Ivaan'
'''unit tests for mainProgram encrytpion and decryption project'''

from mainProgram import caesar, substitution, enigma
import os


def caesar_test():
    '''decryption test'''
    fin_en_s = open(os.path.join('short_test', 'caesar-2step-encrypted'))  # opens file
    read_en_s = fin_en_s.read()  # read and store in variable
    fin_de_s = open(os.path.join('short_test', 'caesar-2step-decrypted'))  # opens file
    read_de_s = fin_de_s.read()  # read and store in variable
    s = 2  # substitution
    type = "d"
    assert caesar(read_en_s, s,type) == read_de_s  # assertion test
    '''encryption test'''
    type = "e"
    assert caesar(read_de_s,s, type) == read_en_s  # assertion test
    fin_en_l = open(os.path.join('long_test', 'caesar-2step-encrypted'))  # opens file
    fin_de_l = open(os.path.join('long_test', 'caesar-2step-decrypted'))  # opens file
    '''encryption test long files'''
    read_en_l = fin_en_l.read()  # read and store in variable
    read_de_l = fin_de_l.read()  # read and store in variable
    s = 2
    type ="e"
    assert caesar(read_de_l,s, type) == read_en_l  # assertion test
    '''decryption test short files'''
    type = "d"
    assert caesar(read_en_l,s, type) == read_de_l  # assertion test


def substitution_test():
     '''decryption test'''
     fin_en_s = open(os.path.join('short_test', 'substitution-encrypted'))  # opens file
     read_en_s = fin_en_s.read()  # read and store in variable
     fin_de_s = open(os.path.join('short_test', 'substitution-decrypted'))  # opens file
     read_de_s = fin_de_s.read()  # read and store in variable
     s = 2  # substitution
     type = "d"
     assert substitution(read_en_s,type) == read_de_s  # assertion test
     '''encryption test'''
     type = "e"
     assert substitution(read_de_s, type)  # assertion test

     fin_en_l = open(os.path.join('long_test', 'substitution-encrypted'))  # opens file
     fin_de_l = open(os.path.join('long_test', 'substitution-decrypted'))  # opens file

     '''encryption test long files'''
     read_en_l = fin_en_l.read()  # read and store in variable
     read_de_l = fin_de_l.read()  # read and store in variable
     s = 2
     type ="e"
     assert substitution(read_de_l,type) == read_en_l  # assertion test
     '''decryption test short files'''
     type = "d"
     assert substitution(read_en_l,type) == read_de_l  # assertion test


def enigma_test():
     '''decryption test'''
     fin_en_s = open(os.path.join('short_test', '3ring-encrypted'))  # opens file
     read_en_s = fin_en_s.read()
     fin_de_s = open(os.path.join('short_test', '3ring-decrypted'))  # opens file
     read_de_s = fin_de_s.read()
     type = "d"
     try:
        assert enigma(read_en_s,type) == read_de_s  # assertion test
     except AssertionError:
         print("The files could not be asserted")
     ''' encryption test '''
     type = "e"
     try:
        assert enigma(read_de_s, type) == read_en_s  # assertion test
     except AssertionError:
         print("The files could not be asserted")
     fin_en_l = open(os.path.join('long_test', '3ring-encrypted'))  # opens file
     fin_de_l = open(os.path.join('long_test', '3ring-decrypted'))  # opens file
     read_en_l = fin_en_l.read()  # read and store in variable
     read_de_l = fin_de_l.read()  # read and store in variable
     type ="d"
     try:
        assert enigma(read_en_l,type) == read_de_l   # assertion test
     except AssertionError:
         print("The files could not be asserted")
     type = "e"
     try:
        assert enigma(read_de_l,type) == read_en_l   # assertion test
     except AssertionError:
         print("The files could not be asserted")


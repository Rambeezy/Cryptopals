import binascii
import codecs

a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"

def XORfunction():
    bina = codecs.encode(codecs.decode(a, 'hex'), 'base64').decode()
    binb = codecs.encode(codecs.decode(b, 'hex'), 'base64').decode()

    product = int(bina,2) ^ int(binb,2)

    final = binascii.hexlify(product)

    print(final)

XORfunction()

#bs = codecs.encode(codecs.decode(s, 'hex'), 'base64').decode()
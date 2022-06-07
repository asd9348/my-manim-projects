import hashlib
import binascii
# import bi
m = hashlib.sha256()
m.update("BTC".encode('utf-8'))
print(m.hexdigest())

hex_string = m.hexdigest()
print(hex_string)
print(type(hex_string))

hex2int = int(hex_string, 16)

print(hex2int)
print(type(hex2int))

# int2bin =
hex_string='0x'+hex_string
print(format(hex2int,'b'))
# print(int(hex_string, 2))
#
# 2진수: 0b
# 8진수: 0o
# 16진수: 0x
ascii=
print(ascii)
print(bin(0xda))
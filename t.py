
# https://www.pycryptodome.org/en/latest/src/cipher/aes.html
from Crypto.Cipher import AES

import os
import time

RND_UNIT_SIZE = 4 # 32bit
RND_COUNT = 2 ** 27

def print_res(msg, begin, end):
    elapse = end - begin
    print('{}: {:,.2}s ({:,.1f}MB/s)'.format(
        msg,
        elapse,
        (RND_UNIT_SIZE * RND_COUNT) / (1024 * 1024) / elapse))

print('unit = {} byte, count = {:,}'.format(RND_UNIT_SIZE, RND_COUNT))

key = bytes(32) # 256 bit

begin = time.time()
r = os.urandom(RND_UNIT_SIZE * RND_COUNT)
end = time.time()
print_res('/dev/urandom', begin, end)

cipher = AES.new(key, AES.MODE_CTR, nonce = bytes(1), use_aesni = False)
begin = time.time()
r = cipher.encrypt(bytes(RND_UNIT_SIZE * RND_COUNT))
end = time.time()
print_res('AES (no use AES-NI)', begin, end)

cipher = AES.new(key, AES.MODE_CTR, nonce = bytes(1), use_aesni = True)
begin = time.time()
r = cipher.encrypt(bytes(RND_UNIT_SIZE * RND_COUNT))
end = time.time()
print_res('AES (use AES-NI)', begin, end)


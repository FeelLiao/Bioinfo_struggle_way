import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from lib import common
# import time
# rec_size=0
# total_size=2093211
# while rec_size<total_size:
#     time.sleep(0.1)
#     rec_size+=1024
#     percent=rec_size/total_size
#     common.progress(percent)

# s=common.RandomVerificationCode(10)
# print(s)
# a=common.hash_encipher("abcdefg")
# print(a)
import time
import datetime

now = time.time()
f = 3

estimated = now + f

balance = estimated - now
# print(estimated)

# now = time.localtime(now)
# inSecs = time.localtime(estimated)

print(now, estimated, balance)
niceTimeNow = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(now))
niceTime = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(estimated))
# niceTimeLT = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(estimated))

print("flight is estimated to arrive on {} GMT".format(niceTimeNow), '\n\r' "That is {} in LT".format(niceTime))

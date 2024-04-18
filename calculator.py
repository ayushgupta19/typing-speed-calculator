import sys
from time import *
import random as r
 
def mistake(partest,usertest):
	error =0
	for i in range(len(partest)) :
		try :
			if partest[i] != usertest[i]:
				error = error+1
		except :
			error = error + 1
	return error

def speed_time(time_start,time_end,usertest):
	time_delay = time_end - time_start
	time_r = round(time_delay,2)
	speed = len(usertest)/time_r
	return round(speed)	

if __name__ == '__main__':
	

	while True:
		ck = input(" set to test : yes / no :")
		if ck == "yes":
			test =["There was a boy named John who was so lazy he couldn't even change his clothes","hello whats your name","hiiiiiiiiiiiiiii"]
			test1 = r.choice(test)
			print("======= typing speed======")

			print(test1)

			print()
			print()
			time_1= time()
			test_input = input(" type :")
			time_2 = time()

			print('speed=', speed_time(time_1,time_2,test_input), 'words/sec')

		elif ck == "no":
			print(" try next time thank you !!!")
			break
		else: 
			print(" wrong input ")
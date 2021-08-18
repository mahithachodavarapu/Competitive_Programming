# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
		l=[x for x in msg]
		k=[]
		for i in l:
			if(i==" "):
				k.append(" ")
			else:
				o=ord(i)
				sh=o+shift
				if(sh>122 and i.islower()):
					sh=sh-26
				elif(sh<97 and i.islower()):
					sh=sh+26
				elif(sh<65 and i.isupper()):
					sh=sh+26
				elif(sh>90 and i.isupper()):
					sh=sh-26
				k.append(chr(sh))
		res="".join(k)
		return res




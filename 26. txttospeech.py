import gtts #  google text to speech
import playsound # importing for to playing the sound 
import googletrans # to do google translate

# print(googletrans.LANGUAGES)bov daayo maro bhai

text=input("Enter something here -> ") # taking the input as the text 

sound=gtts.gTTS(text,lang='gu') # for english -> en gujarati -> gu hindi -> hi
# sound is the variable over here which takes gtts takes form this module means google translator gTTS 
# which taking the text as input and translate to desire language at here gu -> means gujarati
sound.save("s1.mp3") # save the audio in s1.mp3 file 
# the s1.mp3 is not already created 
# after running the program it will automatically created here
playsound.playsound("s1.mp3") # from that play the sound


# Python program to demonstrate langdetect

# from langdetect import detect


# # Specifying the language for
# # detection
# print(detect("Geeksforgeeks is a computer science portal for geeks"))
# print(detect("Geeksforgeeks - это компьютерный портал для гиков"))
# print(detect("Geeksforgeeks es un portal informático para geeks"))
# print(detect("Geeksforgeeks是面向极客的计算机科学门户"))
# print(detect("Geeksforgeeks geeks के लिए एक कंप्यूटर विज्ञान पोर्टल है"))
# print(detect("Geeksforgeeks geeks તમે કેમ છો"))
# print(detect("Geeksforgeeksは、ギーク向けのコンピューターサイエンスポータルです。"))

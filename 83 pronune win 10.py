# # Files
# # Commands
# # Search
# # Packager files
# # Write a program to pronounce list of names using win32 API. If you are given a list l as follows:

# # l = ["Rahul", "Nishant", "Harry"]

# # Your program should pronouce:

# # Shoutout to Rahul
# # Shoutout to Nishant
# # Shoutout to Harry

# # Note: If you are not using windows, try to figure out how to do the same thing using some other package
# import win32com.client as wincl

# spk = wincl.Dispatch("SAPI.SpVoice")
# vcs = spk.GetVoices()

# print("Available voices:")
# for index, voice in enumerate(vcs):
#     print(f"Voice {index}: {voice.GetDescription()}") 

from win32com.client import Dispatch
Windows_Speak = Dispatch('SAPI.Spvoice')

Windows_Speak.Voice = Windows_Speak.GetVoices().Item(2)
Windows_Speak.Rate = 1
print(Windows_Speak.GetVoices().Item(2).GetDescription()) #just to see what voice is used

Windows_Speak.Speak('konichiwa')
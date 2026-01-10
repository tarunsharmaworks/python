from win32com.client import Dispatch
from deep_translator import GoogleTranslator
import win32com.client as wincl
# spk = wincl.Dispatch("SAPI.SpVoice")
# vcs = spk.GetVoices()

# print("Available voices:")
# for index, voice in enumerate(vcs):
#     print(f"Voice {index}: {voice.GetDescription()}") 

# Text to translate
sentence = input("enter word to translate:")
# Create a translator instance, letting it auto-detect the source language
# and specifying the target language (e.g., 'fr' for French or 'french' by name)
translator = GoogleTranslator(source='auto', target='ja')

# Perform the translation
translation = translator.translate(sentence)

# Print the result
print(f"Original Text: {sentence}")
print(f"Translated Text: {translation}")
# Expected output:
# Original Text: Hello, how are you?
# Translated Text: Bonjour, comment allez-vous?

Windows_Speak = Dispatch('SAPI.Spvoice')

Windows_Speak.Voice = Windows_Speak.GetVoices().Item(2)
# Windows_Speak.Rate = 1
print(Windows_Speak.GetVoices().Item(2).GetDescription()) 

Windows_Speak.Speak(translation)
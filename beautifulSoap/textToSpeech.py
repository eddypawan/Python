# import pyttsx3

# # initialize the engine
# engine = pyttsx3.init()

# # set the voice
# voices = engine.getProperty('voices')
# # use the first voice from the list (index 0)
# engine.setProperty('voice', voices[2].id)

# # define the text to be spoken
# text = "Hello, how are you today?"

# # speak the text
# engine.say(text)

# # set the voice to the second voice from the list (index 1)
# engine.setProperty('voice', voices[1].id)

# # define the text to be spoken
# text = "I'm doing well, thank you for asking."

# # speak the text
# engine.say(text)

# # run the engine
# engine.runAndWait()

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

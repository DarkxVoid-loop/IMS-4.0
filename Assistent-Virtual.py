import speech_recognition as sr             
import pyttsx3                                           

test1 = ("Olá Jarvis")

r = sr.Recognizer()


mic = sr.Microphone()

while(1):

	with mic as fonte:
	    
	    r.adjust_for_ambient_noise(fonte)
	    print("Fale alguma coisa")
	   
	    audio = r.listen(fonte)
	    print("Enviando para reconhecimento")

	   
	   
	    try:
	        
	        text = r.recognize_google(audio, language= "pt-BR")

	        
	        print("Você disse: {}".format(text))
	      
	        if text == test1:
		        engine = pyttsx3.init('sapi5')
		        
		        engine.say("Olá Senhor Diego")
		        
		        engine.runAndWait()

		        engine.stop()

	    except:
	        engine = pyttsx3.init('espeak')
	        engine.say("Desculpa, não entendi o que você disse, pode repetir?")
	        engine.runAndWait()
	        engine.stop()
	        print("Não entendi o que você disse")
	        
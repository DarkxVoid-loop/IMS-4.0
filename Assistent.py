import speech_recognition as sr

#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
 
 #Habilita o microfone para ouvir o usuario
 Microfone = sr.Recognizer()
 
 with sr.Microphone() as source:
 
  #Chama a funcao de reducao de ruido disponivel na speech_recognition
  Microfone.adjust_for_ambient_noise(source)
 
  #Avisa ao usuario que esta pronto para ouvir
  print("Diga alguma coisa: ")
 
  #Armazena a informacao de audio na variavel
  Audio = Microfone.listen(source)

  try:
  
  #Passa o audio para o reconhecedor de padroes do speech_recognition
  Frase =  Microfone.recognize_google(Audio,language='pt-BR')
 
  #Após alguns segundos, retorna a frase falada
  print("Você disse: " + Frase)

  #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
  except sr.UnkownValueError:
  print("Não entendi")

ouvir_microfone()
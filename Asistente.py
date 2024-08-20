from calendar import c
from copy import copy
from email.mime import audio
from traceback import print_tb
import pyttsx3 as asistente
import speech_recognition as reconocimiento
import subprocess 
import pyautogui as bot
from time import sleep
import Dibujo
import BotWhatsapp
import teclas


#Configuracion del asistente
voz = asistente.init()
voces = voz.getProperty('voices')
voz.setProperty('voice', voces[0].id)
voz.setProperty('rate', 130)

sigue = True

def habla(text):
    voz.say(text)
    print("\n"+">> " + text)
    voz.runAndWait()

Dibujo.cara()
habla(f'Buenas Alejandro, bienvenido')

while sigue:
    escucha = reconocimiento.Recognizer()
    #Activando microfono
    with reconocimiento.Microphone() as source:
        
        print(">> Escuchando... ")
        audio=escucha.listen(source, phrase_time_limit=4)
    # Si se entiende nuestra peticion entramos a la logica principal
    try:
        encendido = escucha.recognize_google(audio, language='es-ES')
        print(f'>> He reconocido: {encendido} \n')
        encendido=encendido.lower()
        encendido=encendido.split(' ')
        if ("hey" in encendido or "ey" in encendido or "oye" in encendido) and 'robot' in encendido:

            escucha3 = reconocimiento.Recognizer()
            #Activando microfono
            with reconocimiento.Microphone() as source:
        
                habla("¿Dime, en que puedo ayudar?")
                audio=escucha3.listen(source, phrase_time_limit=4)
                comando = escucha3.recognize_google(audio, language='es-ES')
                print(f'He reconocido: {comando}')
                comando=comando.lower()
                comando=comando.split(' ')
                if 'cambiar' in comando or 'cambia' in comando:
                    objetos = {'aplicación': 1,
                    'teclado': 2,
                    'manual': 3}
                    for i in list(objetos.keys()):
                        if i in comando:
                            habla(f'cambiando {i}')
                            teclas.funcion(objetos[i])

                elif 'búsqueda' in comando or 'buscar' in comando:

                    habla(f'Buscando en google')
                    subprocess.call(f'start chrome.exe https://www.google.com/', shell=True)
                    sleep(1)
                    habla("¿Que quieres buscar?")
                    escucha2 = reconocimiento.Recognizer()
                    #Activando microfono
                    with reconocimiento.Microphone() as source2:
                        print("Escuchando... ")
                        audio2=escucha2.listen(source2, phrase_time_limit=4)
                        busca=escucha.recognize_google(audio2, language='es-ES')
                        habla(f'Buscando  {busca}')
                        busca=busca.lower()
                        bot.typewrite(busca)
                        bot.press("enter")
                    
                elif 'abre' in comando or 'abrir' in comando:

                    sitios= {'google': 'https://www.google.com',
                    'youtube': 'https://www.youtube.com',
                    'instagram': 'https://www.instagram.com',
                    'tryhackme': 'https://www.tryhackme.com',
                    "whatsapp": "https://web.whatsapp.com/"}

                    for i in list(sitios.keys()):
                        if i in comando:
                            habla(f'Abriendo {i}')
                            sleep(1.5)
                            subprocess.call(f'start chrome.exe {sitios[i]}', shell=True)
                elif 'ventana' in comando or ('abrir' in comando and 'ventana'in comando ):
                    ventanas={'visual': 'Code'}
                    for i in list(ventanas.keys()):
                        if i in comando:
                            habla(f'Abriendo {i}')
                            subprocess.call(f'start {ventanas[i]}', shell=True)

                    for i in list(contacto.keys()): 
                        if i in comando:
                            habla(f'Hablando a {i}')
                            BotWhatsapp.habla(contacto[i])

                elif 'protocolo' in comando:

                    protocolos = {'fiesta': 'https://www.youtube.com/watch?v=ikFFVfObwss',
                    'relajante': 'https://www.youtube.com/results?search_query=asmr+relajante'}

                    for i in list(protocolos.keys()):
                        if i in comando:
                            habla(f'Ahora mismo Señor')
                            subprocess.call(f'start chrome.exe {protocolos[i]}', shell=True)
        elif 'apagar' in encendido or 'apaga' in encendido:
            habla(f'Un placer.')
            sigue=False

        elif 'cállate' in encendido:
            print("        ಠ_ಠ")
            habla(f'callate tu que eres un pesao.')
            

    except: 
        print(".-.-.-.-.")

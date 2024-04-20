import json
import requests
import speech_recognition as sr 
import winsound
import googletrans
import urllib.request
import keyboard

model='maidchan'


def generate(user_input, context):

    msg = ""
    r = requests.post('http://127.0.0.1:11434/api/generate',
    json={
        'model':model,
        'prompt':user_input,
        'context': context,
    },
    stream=True)
    r.raise_for_status()

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response','')
        #print(response_part,end='',flush=True)
        #print("-------")
        msg += response_part

        if 'error' in body:
            raise Exception(body['error'])
        if body.get('done',False):
            return body['context'], msg
        

def RmyVoice(): 
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Dites quelque chose...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Analyse de l'audio...")
        user_input = recognizer.recognize_google(audio, language='fr-FR')
        return user_input
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio.")
        return ""
    except sr.RequestError as e:
        print("Erreur lors de la requête à l'API de reconnaissance vocale ; {0}".format(e))
        return ""

def sc_parle(fr,jp):

    global is_speaking 
    katana = jp
    print(katana)
    params = urllib.parse.urlencode({'text':katana,'speaker':46})
    req = requests.post(f'http://127.0.0.1:50021/audio_query?{params}')
    params = urllib.parse.urlencode({'speaker':46,'enable_interrogative_upspeak': True})
    req = requests.post(f'http://127.0.0.1:50021/synthesis?{params}',json=req.json())

    with open("output.wav","wb") as outfile:
        outfile.write(req.content)

    is_speaking = True
    winsound.PlaySound("output.wav",winsound.SND_FILENAME)
    is_speaking = False



def traductionJap(text):
    try:
        translator = googletrans.Translator()
        result = translator.translate(text, src="fr", dest="ja")
        return result.text
    except TranslatorError as e:
        print("Erreur lors de la traduction:", e)
        return None


def main():
    context = []
    while True:
        if keyboard.is_pressed(','):
            user_input = RmyVoice()
            if user_input:
                context, rep = generate(user_input, context)
                tr = traductionJap(rep)
                print(rep)
                sc_parle(rep,tr)


if __name__ == "__main__" :
    main()
    
from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize_speech', methods=['POST'])
def recognize_speech():
    # Проверяем, что пришел POST запрос
    if request.method == 'POST':
        # Создаем объект recognizer
        recognizer = sr.Recognizer()
        # Запускаем запись аудио
        with sr.Microphone() as source:
            print("Говорите что-нибудь...")
            audio_data = recognizer.listen(source)

        try:
            # Пытаемся распознать речь
            text = recognizer.recognize_google(audio_data, language='ru-RU')
            return text
        except sr.UnknownValueError:
            return "Не удалось распознать речь"
        except sr.RequestError as e:
            return "Ошибка сервиса распознавания: {0}".format(e)

if __name__ == '__main__':
    app.run(debug=True)

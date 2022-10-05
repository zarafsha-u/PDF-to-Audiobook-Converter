
import fitz
import pyttsx3


class PdfToAudio():
    def __init__(self, book):
        """Enter your pdf name as its been downloaded/it's filepath"""
        speaker = pyttsx3.init()
        with fitz.open(book) as doc:
            self.text = ""
            for page in doc:
                self.text+= page.get_text()
        print(self.text)
        speaker.setProperty('rate', 150)
        speaker.say(self.text)
        speaker.runAndWait()












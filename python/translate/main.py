from googletrans import Translator



def text_translator(text='Hello world', dest='ru', src='en'):
    try:
        translaitor = Translator()

        translate = translaitor.translate(text=text, src=src, dest=dest)

        return translate.text
    except Exception as ex:
        return ex
    
print(text_translator())
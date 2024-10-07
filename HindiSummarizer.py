# from googletrans import Translator
# from summarizer import textrank

# f=open('HindiText.txt','r')
# hinText=f.read()
# print(hinText)
# f.close()

# engText=Translator().translate(hinText,'en')
# engSum=textrank(engText.text)

# for sentence in engSum:
# 	hinSent=Translator().translate(sentence,'hi')	
# 	temp=hinSent.text	
# 	f=open('HindiSum.txt','a')
# 	f.write(temp)
# 	f.close()


		
from googletrans import Translator
from summarizer import textrank
from deep_translator import GoogleTranslator

# Initialize translator
translator = GoogleTranslator(source='auto', target='mr')

# Read the Hindi text with proper encoding
try:
    with open('HindiText', 'r', encoding='utf-8') as f:
        hinText = f.read()
except UnicodeDecodeError as e:
    print(f"Error reading file: {e}")
    hinText = ""  # Handle the error as needed

print(hinText)

# Translate Hindi text to English
# translator = Translator()
# x=translator.translate('안녕하세요.',dest='en')
# print(x)
try:
    engText = translator.translate(hinText, dest='mr')
    print(engText)
except Exception as e:
    print(f"Error during translation: {e}")
    engText = ""

# Summarize the English text
try:
    engSum = textrank(engText)
except Exception as e:
    print(f"Error during summarization: {e}")
    engSum = []

# Translate the summary back to Hindi and write to file
try:
    with open('HindiSum', 'a', encoding='utf-8') as f:
        for sentence in engSum:
            hinSent = translator.translate(sentence, dest='mr')
            f.write(hinSent + '\n')
except Exception as e:
    print(f"Error during file writing: {e}")


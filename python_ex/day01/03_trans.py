import googletrans
#googleTrans는 구글 번역기를 사용하게되면
#번역기는 구글에서 제공하는 
translator = googletrans.Translator()

input_text = input("한글을 입력하세요 : ")

translated = translator.translate(input_text,dest='en').text

print(f"입력한 한글 : {input_text}")
print(f"번역된 영어 : {translated}")

# You simply need to enter the text you want to convert in first line amd the name of language in second line in which you want to translate
"""For IDE users there is a GUI code given below"""
# example
""" 
i am 
hi
"""
# output :


"""
languages supported here are
type language name directly or else
type af for afrikaans
type sq for albanian
type am for amharic
type ar for arabic
type hy for armenian
type az for azerbaijani
type eu for basque
type be for belarusian
type bn for bengali
type bs for bosnian
type bg for bulgarian
type ca for catalan
type ceb for cebuano
type ny for chichewa
type zh-cn for chinese (simplified)
type zh-tw for chinese (traditional)
type co for corsican
type hr for croatian
type cs for czech
type da for danish
type nl for dutch
type en for english
type eo for esperanto
type et for estonian
type tl for filipino
type fi for finnish
type fr for french
type fy for frisian
type gl for galician
type ka for georgian
type de for german
type el for greek
type gu for gujarati
type ht for haitian creole
type ha for hausa
type haw for hawaiian
type iw for hebrew
type he for hebrew
type hi for hindi
type hmn for hmong
type hu for hungarian
type is for icelandic
type ig for igbo
type id for indonesian
type ga for irish
type it for italian
type ja for japanese
type jw for javanese
type kn for kannada
type kk for kazakh
type km for khmer
type ko for korean
type ku for kurdish (kurmanji)
type ky for kyrgyz
type lo for lao
type la for latin
type lv for latvian
type lt for lithuanian
type lb for luxembourgish
type mk for macedonian
type mg for malagasy
type ms for malay
type ml for malayalam
type mt for maltese
type mi for maori
type mr for marathi
type mn for mongolian
type my for myanmar (burmese)
type ne for nepali
type no for norwegian
type or for odia
type ps for pashto
type fa for persian
type pl for polish
type pt for portuguese
type pa for punjabi
type ro for romanian
type ru for russian
type sm for samoan
type gd for scots gaelic
type sr for serbian
type st for sesotho
type sn for shona
type sd for sindhi
type si for sinhala
type sk for slovak
type sl for slovenian
type so for somali
type es for spanish
type su for sundanese
type sw for swahili
type sv for swedish
type tg for tajik
type ta for tamil
type te for telugu
type th for thai
type tr for turkish
type uk for ukrainian
type ur for urdu
type ug for uyghur
type uz for uzbek
type vi for vietnamese
type cy for welsh
type xh for xhosa
type yi for yiddish
type yo for yoruba
type zu for zulu
"""
text = input() or "my name is "
des = input() or "bengali"
if len(text) ==0:
    text = "hi how are you guys"
if len(des) ==0:
   des = "en"
import subprocess,sys
def install(package):
    subprocess.call([sys.executable, "-m","pip","--disable-pip-version-chec","-q", "install", package])

install("googletrans")
import googletrans
translator = googletrans.Translator()
result = translator.translate(text ,dest=des)
print("detected language is "+googletrans.LANGUAGES[result.src]+"\n")
print(result.origin)
print("\n"+"-"*40+"\n")
print("translated text to "+googletrans.LANGUAGES[result.dest]+"\n")
print(result.text)





"""IDE Users can copy and use following code for better experience"""

"""

try :
    import googletrans
except :
    print("oops you dont have some important packages...")
    print("This process will done for first time only so please wait ...")
    import subprocess,sys
    def install(package):
        subprocess.call([sys.executable, "-m","pip","--disable-pip-version-chec","-q", "install", package])
    print("downloading modules ...")
    install("googletrans")
    print("download completed succesfully...")
import googletrans,time
from tkinter import *
from tkinter.ttk import Combobox  
translator = googletrans.Translator()
languages = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

def translate():
    text = e1.get("1.0",END)
    des = languages[ls.get()]
    result = translator.translate(text ,dest=des)
    l1.config(text=googletrans.LANGUAGES[result.src])
    e2.delete("1.0",END)
    e2.insert("1.0",result.text)
root = Tk()
root['bg'] = "#ffffff"

f0 = Frame(root,bg="white",height=1)
l1 = Label(f0,height=1,width=10,bg="white",bd=1,relief="groove")
l1.config(text="Unknown")
l1.grid(row=0,column=0,padx=(0,5),pady=10)
l2 = Label(f0,height=1,width=2,bg="white")
l2.config(text="⇨")
l2.grid(row=0,column=1,padx=(5,5),pady=10)
ls = Combobox(f0,height=20,width=12,values=[i for i in languages])
ls.current(37)
ls.grid(row=0,column=2,padx=(5,30),pady=10)
b1 = Button(f0,text="⇄ Translate",height=1,width=8,bg="white",fg="#080808",activebackground="#e0e0e0",activeforeground="#080808",command=translate)
b1.grid(row=0,column=3,padx=(5,0),pady=10)
f0.pack()

f1 = Frame(root)
e1 = Text(f1,width=43,height=15,bg="white")
h1 = Scrollbar(f1,
                          orient=VERTICAL,
                          command=e1.yview,
                          activebackground="white",
                          bg="white",
                          bd=0.5,
                          repeatdelay=300,
                          troughcolor="white",
                          width=3
                          )
e1.configure(yscrollcommand=h1.set)
e1.insert("1.0","Enter Text.")
h1.pack(side=RIGHT,fill=Y)
e1.pack()
f1.pack(pady=20)

f2 = Frame(root)
e2 = Text(f2,width=43,height=15,bg="white")
h2 = Scrollbar(f2,
                          orient=VERTICAL,
                          command=e1.yview,
                          activebackground="white",
                          bg="white",
                          bd=0.5,
                          repeatdelay=300,
                          troughcolor="white",
                          width=3
                          )
e2.configure(yscrollcommand=h2.set)
e2.insert("1.0","See your translated text here.")
h2.pack(side=RIGHT,fill=Y)
e2.pack()
f2.pack(pady=20)
root.mainloop()
"""
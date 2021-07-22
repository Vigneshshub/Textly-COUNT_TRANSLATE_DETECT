import nltk
from nltk.corpus import stopwords
nltk.download('punkt') # Download for Tokenize
from numpy.lib.function_base import insert
from textblob import TextBlob
from textblob import Word
import spacy
nlp = spacy.load('en_core_web_sm')

from flask  import Flask,render_template,request
from werkzeug.utils import html

app = Flask(__name__)

#Count Number of Words

@app.route('/')
def welcome():
     return render_template('home.html')

@app.route("/Count_Words",methods = ['POST'])
def CountWords():
        return render_template('CountWords.html' )

@app.route("/Count_Words_Results",methods = ['POST'])
def Count():
    inString = request.form.get('Write Something')
    inString=str(inString)
    doc = nlp(inString)
    count= len(doc)
    return render_template('CountWords.html' ,prediction_text = f"count: {count}")


#For Sentence Count

@app.route("/Count_Sentences",methods = ['POST'])
def CountSentences():
        return render_template('CountSentences.html' )

@app.route("/Count_Sentences_Results",methods = ['POST'])
def CountSentences_Results():
    inString = request.form.get('Write Something')
#     inString=str(inString)
    count=  len(nltk.sent_tokenize(inString))
    return render_template('CountSentences.html' ,prediction_text = f"count: {count}")

#Dictionary

@app.route("/Dictionary",methods = ['POST'])
def Dict():
        return render_template('Dictionary.html' )

@app.route("/Dictionary_Results",methods = ['POST'])
def Dict_Results():
    StopWords = stopwords.words('english')
    inString = request.form.get('Write Something')
    inString=str(inString)
    Inp = Word(str(inString))
    Dict= Inp.definitions
    return render_template('Dictionary.html' ,prediction_text = f"{Dict}")

#Dictionary Mapping for Language

DictLang = {"English":"en","Tamil":"ta","Malayalam":"ml","Hindi":"hi","French" : "fr" ,"telegu" :"te"}
key_list = list(DictLang.keys())
val_list = list(DictLang.values())

#Translate

@app.route("/Translate",methods = ['POST'])
def Translate():
        return render_template('Translate.html' )

@app.route("/Translate_Results",methods = ['POST'])
def Translate_Results():
    inString = request.form.get('Write Something')
    inString=str(inString)
    blob = TextBlob(inString)
    if inString != "":
        LanSelected = str(request.form.get('Lang'))
        try:
                Translated = blob.translate(to=DictLang[LanSelected])
                return render_template('Translate.html' ,prediction_text = f"{str(Translated)}")
        except:
                return render_template('Translate.html' ,prediction_text = "Given Text and Selected language are same")



#Detect Language

@app.route("/Detect_Language",methods = ['POST'])
def Detect_Language():
        return render_template('Detect_Language.html' )

@app.route("/Detect_Language_Results",methods = ['POST'])
def Detect_Language_Results():
        inString = request.form.get('Write Something')
        inString=str(inString)
        blob = TextBlob(inString)
        Detected = blob.detect_language()
        position = val_list.index(str(Detected))
        return render_template('Detect_Language.html' ,prediction_text = f"{str(key_list[position])}" )

if __name__=='__main__':
    app.run(debug=True)
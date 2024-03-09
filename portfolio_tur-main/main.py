# Import
from flask import Flask, render_template,request, redirect
from record import detect_audio



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')

# İçerik sayfasını çalıştırma
@app.route('/#home')
def home():
    return render_template('index.html')

# Dinamik beceriler
@app.route('/', methods=['POST'])
def index2():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)



@app.route('/record')
def recordaudio():
    try:
        text = detect_audio()
        if text=="discord botu" or text=="Discord botu":
                return redirect("./#home")
        if text=="discord botu ile alakalı" or text=="Discord botu ile alakalı":
                return redirect("./#about")
        if text=="sunucunuza botu eklemek için link" or text=="Sunucunuza botu eklemek için link":
                return redirect("./#skills")
        else:
                return redirect("/")

    except:
        text = "BİR HATA OLUŞTU! LÜTFEN TEKRAR DENEYİN!"
#home
    
    
    return render_template('index.html')

    
    

if __name__ == "__main__":
    app.run(debug=True)    
from flask import Flask, render_template,jsonify
app = Flask(__name__)

Volne_pozice = [
      {
      'id': 1,
      'title': 'Datový analytik',
      'location': 'Kladno, Česká republika',
       'mzda':'  ' '80,0000Kč'
      },
      {
          'id': 2,
           'title': 'Vědecký analytik',
           'location': 'Praha, Česká republika',
            'mzda':' ' '100,0000 Kč'
      },
      {
          'id': 3,
             'title': 'Fronted Engineer',
             'location': 'Remote',
              'mzda':' ' '90,0000 Kč'
       },
        {
            'id': 4,
               'title': 'Backend Engineer',
               'location': 'San Francisco, USA',
                'mzda':' ' '$120,0000'
         }
  ]

@app.route("/")
def hello_daniel():
    return render_template('home.html',
                            Volne_pozice = Volne_pozice,
                            company_name ='Martina')
@app.route("/Volne_pozice")    
def list_volne_pozice():          
    return jsonify(Volne_pozice) 

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
         
 
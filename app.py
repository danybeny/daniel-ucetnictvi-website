from flask import Flask, render_template,jsonify
app = Flask(__name__)

Volné_pozice = [
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
                            Volné_pozice = Volné_pozice,
                            company_name ='Daniel')
@app.route("/Volné_pozice")    
def list_volne_pozice():          
    return jsonify(Volné_pozice) 

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
         
 
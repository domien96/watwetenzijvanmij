from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField
import lookup
import monitor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone = request.form['phone']
        lookup_result = do_lookup(phone)
        monitor.save_request(phone, lookup_result)
        
        leaked, unleaked = prepare_search_result(lookup_result)
        return render_template('index.html', show_result=True, request_count=monitor.get_total_requests(), leaked=leaked, unleaked=unleaked)
    else: # GET
        return render_template('index.html', request_count=monitor.get_total_requests())
        


def do_lookup(phone): # ex. : +32 486 41 48 49, returns matching line
    phone = phone.replace(' ','').replace('+','')
    lookup_result = lookup.lookup(phone)
    return lookup_result 

def prepare_search_result(res):
    names = ['Telefoonnummer', 'idx', 'Voornaam', 'Achternaam', 'Geslacht', 'Woonplaats', 'Geboorteplaats', 
    'Relatie status', 'Werkgever', 'leakage day', 'lkge hour', 'lkge sec', 'E-mailadres', 'Geboortedag']
    irrelevant_names = ['idx', 'leakage day', 'lkge hour', 'lkge sec']
    idx_in_record = [0, 1, 2, 3, 4, 5, -8, -7, -6, -5, -4, -3, -2, -1]
    if (res == None):
        return [],[n for n in names if n not in irrelevant_names]
    res = res.replace('\n', '').split(',')
    resmap = {}
    for i in range(len(names)):
        name = names[i]
        if (name not in irrelevant_names):
            resmap[name] = res[idx_in_record[i]]
    leaked = [key  for (key, val) in resmap.items() if val != '']   
    unleaked = [key for (key, val) in resmap.items() if val == '']
    unleaked.append('Rekeningnummer')
    return leaked, unleaked

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

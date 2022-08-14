from click import confirm
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)

@app.route('/person_delete/<string:indexOfId>')
def people_delete(indexOfId):
    indexId=int(indexOfId)
    for i in model:
        i2=0
        print(int(i.id_person) is indexId)
        if int(i.id_person) == indexId:
            model.pop(i2)
            print(model)
        i2+1
    return render_template('index.html')

@app.route('/person_update/<string:indexOfId>')
def people_update(indexOfId):
    indexID = int(indexOfId)
    for i in model:
        i2 = 0
        print(int(i.id_person) is indexID,53)
        if int(i.id_person) == indexID:
            Data = (i.id_person, i.name, i.last_name)
            return render_template('personUpdate.html', value = Data)
        i2+1
    return

@app.route('/person_update2', methods=['POST'])
def person_update2():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    for i in model:
        print(int(i.id_person) is int(id_person))
        if int(i.id_person) == int(id_person):
            i.name=first_name
            i.last_name=last_name
            return render_template('person_detail.html', value=p)
        else:
            return render_template('people.html')
        #aqui en el codigo cuando se cambie el ID lo devolvera a la lista de usuarios
if __name__ == '__main__':
    app.run()
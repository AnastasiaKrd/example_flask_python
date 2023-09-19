from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    
  {
    "id" : 0,
    "author": "Chinua Achebe",
    "title": "Things Fall Apart",
    "year": 1958
  },
  {
    "id" : 1,
    "author": "Hans Christian Andersen",
    "title": "Fairy tales",
    "year": 1836
  },
  {
    "id" : 2,
    "author": "Dante Alighieri",
    "title": "The Divine Comedy",
    "year": 1315
  }
]

@app.route('/books', methods = ['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing found', 404

    if request.method == 'POST':
        id = books_list[-1]['id']+1
        new_author = request.form['author']
        new_title = request.form['title']
        new_year = request.form['year']

        new_obj = {
            "id" : id,
            "author": new_author,
            "title": new_title,
            "year": new_year    
        }
        books_list.append(new_obj)
        return jsonify(books_list), 201

if __name__ == '__main__':
    app.run()       
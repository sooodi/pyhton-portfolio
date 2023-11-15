from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)


# @app.route('/<username>/<int:postid>')
# def hello_world(username=None, postid=None):
#     return render_template('index.html', name=username, post_id=postid)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:pagensme>')
def components(pagensme):
    return render_template(pagensme)


@app.route('/sumbit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
        data = request.form.to_dict()
        print(data)
        # write_to_file(data)
        write_to_csv(data)
        return redirect('thankyou.html')
        except:
    else:
        return 'somrthing went wrong'


def write_to_csv(data):
    with open('database.csv',newline="", mode='a') as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # spamwriter = csv.writer(csvfile, delimiter=',',
        #                         quotechar='"', quoting=csv.QUOTE_MINIMAL)
        headers = ['email', 'subject', 'message']
        spamwriter = csv.DictWriter(csvfile, fieldnames=headers)
        spamwriter.writeheader()

        spamwriter.writerow(
            {'email': email, 'subject': subject, 'message': message})

    #  csv_writer.writeheader()
    #    csv_writer = csv.writer(csvfile,  delimiter=",",
    #                             quotechar='', quoting=csv.QUOTE_MINIMAL)
    # csv_writer.writerow([email, subject, message])


def write_to_file(data):
    with open('database.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = db.write(f'\n{email},{subject} ,{message}')

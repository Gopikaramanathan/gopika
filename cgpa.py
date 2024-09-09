from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    cgpa = ""
    if request.method == 'POST':
        grades = list(map(float, request.form.getlist('grades')))
        credits = list(map(float, request.form.getlist('credits')))
        cgpa = calculate_cgpa(grades, credits)
    return render_template_string('''
        <html>
            <body>
                <h1>CGPA Calculator</h1>
                <form method="post">
                    <label>Grades:</label><br>
                    <input type="text" name="grades"><br>
                    <label>Credits:</label><br>
                    <input type="text" name="credits"><br>
                    <input type="submit" value="Calculate CGPA">
                </form>
                <h2>Your CGPA is: {{ cgpa }}</h2>
            </body>
        </html>
    ''', cgpa=cgpa)

def calculate_cgpa(grades, credits):
    total_points = sum(grade * credit for grade, credit in zip(grades, credits))
    total_credits = sum(credits)
    cgpa = total_points / total_credits
    return round(cgpa, 2)

if __name__ == '__main__':
    app.run(debug=True)

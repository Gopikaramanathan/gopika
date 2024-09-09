from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        value = float(request.form['value'])
        input_scale = request.form['input_scale']
        output_scale = request.form['output_scale']
        result = convert_temperature(value, input_scale, output_scale)
    return render_template_string('''
        <html>
            <body>
                <h1>Temperature Converter</h1>
                <form method="post">
                    <label>Value:</label>
                    <input type="text" name="value"><br>
                    <label>Input Scale:</label>
                    <select name="input_scale">
                        <option value="C">Celsius</option>
                        <option value="F">Fahrenheit</option>
                        <option value="K">Kelvin</option>
                    </select><br>
                    <label>Output Scale:</label>
                    <select name="output_scale">
                        <option value="C">Celsius</option>
                        <option value="F">Fahrenheit</option>
                        <option value="K">Kelvin</option>
                    </select><br>
                    <input type="submit" value="Convert">
                </form>
                <h2>Result: {{ result }}</h2>
            </body>
        </html>
    ''', result=result)

def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else:
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request
from matplotlib import pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    chart_url = None
    total_kcals = None

    if request.method == 'POST':
        try:
            fats = float(request.form['fats'])
            carbs = float(request.form['carbs'])
            protein = float(request.form['protein'])

            protein_kcal = protein * 4
            carbs_kcal = carbs * 4
            fats_kcal = fats * 9
            total_kcals = int(protein_kcal + carbs_kcal + fats_kcal)

            macros = [protein_kcal, fats_kcal, carbs_kcal]
            labels = ['Protein', 'Fats', 'Carbs']
            colors = ['#ff9999', '#66b3ff', '#99ff99']

            plt.figure()
            plt.pie(macros, labels=labels, colors=colors,
                    autopct=lambda p: '{:.1f}%'.format(p), startangle=90)
            plt.title(f'Macro Break Down', pad=20)
            plt.axis('equal')

            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            chart_url = base64.b64encode(img.getvalue()).decode()

        except ValueError:
            pass  # You could handle this more elegantly

    return render_template('index.html', chart_url=chart_url, total_kcals=total_kcals)

if __name__ == '__main__':
    app.run(debug=True)

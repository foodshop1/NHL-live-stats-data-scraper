from flask import Flask, render_template
from nhl_data import stats
from graph import save_plot

app = Flask(__name__)

# Route to display the graph
@app.route('/')
def index():
  image_path = save_plot()  # Save the plot and get the image path
  return render_template("index.html", image_path=image_path)

if __name__ == "__main__":
  app.run(debug=True)
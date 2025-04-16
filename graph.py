from nhl_data import stats
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for script-only usage
from nhl_data import stats
import matplotlib.pyplot as plt
import os

json_data = stats()

def plot_nhl_points(json_data):
    team_data = [(team, json_data[team]['points']) for team in json_data.keys()]
    team_data.sort(key=lambda x: x[1], reverse=True)

    team_names, points = zip(*team_data)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(team_names, points, color='skyblue')
    ax.set_title('NHL Teams by Points')
    ax.set_xlabel('Teams')
    ax.set_ylabel('Points')
    plt.xticks(rotation=90)
    plt.tight_layout()

    return fig

def save_plot():
    fig = plot_nhl_points(json_data)
    image_path = os.path.join('static', 'nhl_plot.png')
    fig.savefig(image_path)
    plt.close(fig)
    return image_path


from nhl_data import stats
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for script-only usage
from nhl_data import stats
import matplotlib.pyplot as plt
import os
from matplotlib.patches import Patch


json_data = stats()

def plot_nhl_points(json_data):
    team_data = [(team, json_data[team]['points']) for team in json_data.keys()]
    team_data.sort(key=lambda x: x[1], reverse=True)

    team_names, points = zip(*team_data)
    colors = ['green' if i < 16 else 'orange' for i in range(len(team_names))]

    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot()
    ax.bar(team_names, points, color=colors)
    ax.set_title('NHL Teams by Points')
    ax.set_xlabel('Teams')
    ax.set_ylabel('Points')
    plt.xticks(rotation=90)
    plt.tight_layout()
    
    legend_elements = [
        Patch(facecolor='green', label='Playoff Spot'),
        Patch(facecolor='orange', label='Non-Playoff')
    ]
    ax.legend(handles=legend_elements, loc='upper right')

    return fig

def save_plot():
    fig = plot_nhl_points(json_data)
    image_path = os.path.join('static', 'nhl_plot.png')
    fig.savefig(image_path)
    plt.close(fig)
    return image_path


from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def root():
    # Read the CSV data
    df = pd.read_csv('data.csv')  # Ensure the path to your data.csv is correct
    name = df['Name']
    usn = df['USN']
    
    # Create a plot
    plt.plot(name, usn,marker='o')
    plt.xlabel('Name')
    plt.ylabel('USN')
    plt.title('Name and USN')
    
    # Save the plot as an image
    plot_path = 'static/plot.png'
    plt.savefig(plot_path)
    
    # Pass the image path to the template
    return render_template('index.html', name=name, usn=usn, plot_image=plot_path)

if __name__ == '__main__':
    app.run(debug=True)

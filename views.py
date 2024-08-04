from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_csv(file)
            context = process_data(df)
            plots = generate_plots(df)
            context['plots'] = plots
            return render(request, 'results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def process_data(df):
    # Display the rows of the data
    first_rows = df.head().to_html()

    # Calculate summary statistics for numerical columns
    summary_stats = df.describe().to_html()

    # Identify missing values and convert to DataFrame
    missing_values = df.isnull().sum()
    missing_values_df = missing_values.reset_index()
    missing_values_df.columns = ['Column', 'Missing Values']
    missing_values_html = missing_values_df.to_html(index=False)

    # Dropping rows with missing values
    df_cleaned = df.dropna()

    # Add data and results to the context
    context = {
        'first_rows': first_rows,
        'summary_stats': summary_stats,
        'missing_values': missing_values_html,
        'cleaned_data': df_cleaned.to_html()
    }

    return context

def generate_plots(df):
    plots = []
    
    for column in df.select_dtypes(include='number').columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column],color='green')
        plot_path = os.path.join(settings.MEDIA_ROOT, f'{column}_histogram.png')
        plt.savefig(plot_path)
        plt.close()
        plots.append(f'{settings.MEDIA_URL}{column}_histogram.png')

    return plots

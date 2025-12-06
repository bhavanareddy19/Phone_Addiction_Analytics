"""
Standalone Chart Generation Script
Creates individual visualizations that can be used in presentations or reports

This script generates all charts as separate image files that can be
inserted into PowerPoint presentations or other documents.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Create output directory for charts
os.makedirs('charts_output', exist_ok=True)

# Load datasets
print("Loading datasets...")
df_addiction = pd.read_csv('Students_Social_Media_Addiction.csv')
df_screentime = pd.read_csv('screen_time_app_usage_dataset.csv')

# Preprocess
df_addiction['Addiction_Category'] = pd.cut(
    df_addiction['Addicted_Score'], 
    bins=[0, 3, 6, 9], 
    labels=['Low', 'Moderate', 'High']
)

print("Generating charts...")

# Chart 1: Platform Distribution
print("1. Creating platform distribution chart...")
platform_counts = df_addiction['Most_Used_Platform'].value_counts().head(10)
fig = go.Figure(data=[
    go.Bar(
        y=platform_counts.index,
        x=platform_counts.values,
        orientation='h',
        marker=dict(color=platform_counts.values, colorscale='Viridis'),
        text=platform_counts.values,
        textposition='outside'
    )
])
fig.update_layout(
    title='Top 10 Most Used Social Media Platforms',
    xaxis_title='Number of Users',
    yaxis_title='Platform',
    height=600,
    width=1200,
    template='plotly_white',
    font=dict(size=14)
)
fig.write_image('charts_output/1_platform_distribution.png', scale=2)
fig.write_html('charts_output/1_platform_distribution.html')
print("   ✓ Saved: 1_platform_distribution.png/html")

# Chart 2: Usage vs Addiction Scatter Plot
print("2. Creating usage vs addiction correlation chart...")
# Add jitter to reduce overlap
df_plot = df_addiction.copy()
np.random.seed(42)
df_plot['Addicted_Score_Jitter'] = df_plot['Addicted_Score'] + np.random.normal(0, 0.15, len(df_plot))
df_plot['Usage_Jitter'] = df_plot['Avg_Daily_Usage_Hours'] + np.random.normal(0, 0.1, len(df_plot))

fig = px.scatter(
    df_plot,
    x='Usage_Jitter',
    y='Addicted_Score_Jitter',
    color='Most_Used_Platform',
    hover_data=['Age', 'Gender', 'Sleep_Hours_Per_Night', 'Avg_Daily_Usage_Hours', 'Addicted_Score'],
    title='Daily Usage Hours vs. Addiction Score by Platform (r = 0.87)',
    labels={
        'Usage_Jitter': 'Average Daily Usage (Hours)',
        'Addicted_Score_Jitter': 'Addiction Score (0-9)'
    },
    height=600,
    width=1200,
    opacity=0.6
)

# Add trendline
from scipy import stats as sp_stats
slope, intercept, r_value, p_value, std_err = sp_stats.linregress(
    df_addiction['Avg_Daily_Usage_Hours'], 
    df_addiction['Addicted_Score']
)
x_trend = np.linspace(df_addiction['Avg_Daily_Usage_Hours'].min(), 
                      df_addiction['Avg_Daily_Usage_Hours'].max(), 100)
y_trend = slope * x_trend + intercept

fig.add_trace(
    go.Scatter(
        x=x_trend,
        y=y_trend,
        mode='lines',
        name=f'Trendline (r={r_value:.2f})',
        line=dict(color='red', width=3, dash='dash')
    )
)

fig.update_traces(marker=dict(size=8, line=dict(width=0.5, color='white')), selector=dict(mode='markers'))
fig.update_layout(template='plotly_white', font=dict(size=14))
fig.write_image('charts_output/2_usage_addiction_correlation.png', scale=2)
fig.write_html('charts_output/2_usage_addiction_correlation.html')
print("   ✓ Saved: 2_usage_addiction_correlation.png/html")

# Chart 3: Mental Health Impact
print("3. Creating mental health impact chart...")
health_impact = df_addiction.groupby('Addiction_Category').agg({
    'Mental_Health_Score': 'mean',
    'Sleep_Hours_Per_Night': 'mean'
}).round(2).reset_index()

fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=('Mental Health Score (0-10)', 'Sleep Hours Per Night'),
    specs=[[{"type": "bar"}, {"type": "bar"}]]
)

# Mental Health Score
fig.add_trace(
    go.Bar(
        x=health_impact['Addiction_Category'],
        y=health_impact['Mental_Health_Score'],
        name='Mental Health',
        marker_color=['#00CC96', '#FFA15A', '#EF553B'],
        text=health_impact['Mental_Health_Score'],
        textposition='outside',
        texttemplate='%{text:.2f}',
        showlegend=False
    ),
    row=1, col=1
)

# Sleep Hours
fig.add_trace(
    go.Bar(
        x=health_impact['Addiction_Category'],
        y=health_impact['Sleep_Hours_Per_Night'],
        name='Sleep Hours',
        marker_color=['#00CC96', '#FFA15A', '#EF553B'],
        text=health_impact['Sleep_Hours_Per_Night'],
        textposition='outside',
        texttemplate='%{text:.2f}',
        showlegend=False
    ),
    row=1, col=2
)

# Add reference lines
fig.add_hline(y=7, line_dash="dash", line_color="gray", opacity=0.5, row=1, col=1)
fig.add_hline(y=7, line_dash="dash", line_color="gray", opacity=0.5, row=1, col=2)

fig.update_layout(
    title='Mental Health & Sleep Impact by Addiction Level',
    template='plotly_white',
    height=600,
    width=1200,
    showlegend=False,
    font=dict(size=14)
)
fig.update_xaxes(title_text='Addiction Category', row=1, col=1)
fig.update_xaxes(title_text='Addiction Category', row=1, col=2)
fig.update_yaxes(title_text='Score', range=[0, 10], row=1, col=1)
fig.update_yaxes(title_text='Hours', range=[0, 9], row=1, col=2)

fig.write_image('charts_output/3_mental_health_impact.png', scale=2)
fig.write_html('charts_output/3_mental_health_impact.html')
print("   ✓ Saved: 3_mental_health_impact.png/html")

# Chart 4: App Category Distribution
print("4. Creating category distribution chart...")
df_screentime['date'] = pd.to_datetime(df_screentime['date'])
category_data = df_screentime.groupby('category')['screen_time_min'].sum().reset_index()

fig = go.Figure(data=[
    go.Pie(
        labels=category_data['category'],
        values=category_data['screen_time_min'],
        hole=0.4,
        marker=dict(colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']),
        textinfo='label+percent',
        textposition='outside'
    )
])

fig.update_layout(
    title='Screen Time Distribution by App Category',
    height=600,
    width=1200,
    template='plotly_white',
    font=dict(size=14)
)

fig.write_image('charts_output/4_category_distribution.png', scale=2)
fig.write_html('charts_output/4_category_distribution.html')
print("   ✓ Saved: 4_category_distribution.png/html")

# Chart 5: Academic Performance Impact
print("5. Creating academic performance chart...")
academic_impact = df_addiction.groupby('Affects_Academic_Performance').size().reset_index(name='Count')
colors = ['#00CC96' if x == 'No' else '#EF553B' for x in academic_impact['Affects_Academic_Performance']]

fig = go.Figure(data=[
    go.Bar(
        x=academic_impact['Affects_Academic_Performance'],
        y=academic_impact['Count'],
        marker_color=colors,
        text=academic_impact['Count'],
        textposition='outside'
    )
])

fig.update_layout(
    title='Academic Performance Impact',
    xaxis_title='Affects Academic Performance',
    yaxis_title='Number of Students',
    height=500,
    width=1000,
    template='plotly_white',
    font=dict(size=14)
)

fig.write_image('charts_output/5_academic_impact.png', scale=2)
fig.write_html('charts_output/5_academic_impact.html')
print("   ✓ Saved: 5_academic_impact.png/html")

# Chart 6: Gender Comparison
print("6. Creating gender comparison chart...")
gender_stats = df_addiction.groupby(['Gender', 'Addiction_Category']).size().reset_index(name='Count')

fig = px.bar(
    gender_stats,
    x='Gender',
    y='Count',
    color='Addiction_Category',
    barmode='group',
    title='Addiction Levels by Gender',
    color_discrete_map={
        'Low': '#00CC96',
        'Moderate': '#FFA15A',
        'High': '#EF553B'
    },
    height=600,
    width=1200
)

fig.update_layout(template='plotly_white', font=dict(size=14))
fig.write_image('charts_output/6_gender_comparison.png', scale=2)
fig.write_html('charts_output/6_gender_comparison.html')
print("   ✓ Saved: 6_gender_comparison.png/html")

# Chart 7: Top Apps by Screen Time
print("7. Creating top apps chart...")
top_apps = df_screentime.groupby('app_name')['screen_time_min'].sum().sort_values(ascending=False).head(15)

fig = go.Figure(data=[
    go.Bar(
        x=top_apps.values,
        y=top_apps.index,
        orientation='h',
        marker=dict(color=top_apps.values, colorscale='Blues'),
        text=top_apps.values.round(0),
        textposition='outside'
    )
])

fig.update_layout(
    title='Top 15 Apps by Total Screen Time',
    xaxis_title='Total Screen Time (Minutes)',
    yaxis_title='App Name',
    height=700,
    width=1200,
    template='plotly_white',
    font=dict(size=14)
)

fig.write_image('charts_output/7_top_apps.png', scale=2)
fig.write_html('charts_output/7_top_apps.html')
print("   ✓ Saved: 7_top_apps.png/html")

# Chart 8: Correlation Matrix
print("8. Creating correlation matrix...")
numeric_cols = ['Age', 'Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night', 
                'Mental_Health_Score', 'Conflicts_Over_Social_Media', 'Addicted_Score']
correlation = df_addiction[numeric_cols].corr()

fig = go.Figure(data=go.Heatmap(
    z=correlation.values,
    x=correlation.columns,
    y=correlation.columns,
    colorscale='RdBu',
    zmid=0,
    text=correlation.values.round(2),
    texttemplate='%{text}',
    textfont={"size": 12},
    colorbar=dict(title="Correlation")
))

fig.update_layout(
    title='Correlation Matrix of Key Metrics',
    height=700,
    width=1200,
    template='plotly_white',
    font=dict(size=14)
)

fig.write_image('charts_output/8_correlation_matrix.png', scale=2)
fig.write_html('charts_output/8_correlation_matrix.html')
print("   ✓ Saved: 8_correlation_matrix.png/html")

# Chart 9: Hourly Usage Pattern
print("9. Creating hourly usage pattern heatmap...")
df_screentime['hour'] = df_screentime['date'].dt.hour
hourly_usage = df_screentime.groupby(['hour', 'category'])['screen_time_min'].sum().reset_index()
hourly_pivot = hourly_usage.pivot(index='hour', columns='category', values='screen_time_min').fillna(0)

fig = go.Figure(data=go.Heatmap(
    z=hourly_pivot.values,
    x=hourly_pivot.columns,
    y=hourly_pivot.index,
    colorscale='YlOrRd',
    text=hourly_pivot.values.round(0),
    texttemplate='%{text}',
    textfont={"size": 10},
    colorbar=dict(title="Minutes")
))

fig.update_layout(
    title='Hourly Usage Patterns by App Category',
    xaxis_title='App Category',
    yaxis_title='Hour of Day',
    height=700,
    width=1200,
    template='plotly_white',
    font=dict(size=14)
)

fig.write_image('charts_output/9_hourly_pattern.png', scale=2)
fig.write_html('charts_output/9_hourly_pattern.html')
print("   ✓ Saved: 9_hourly_pattern.png/html")

# Chart 10: Platform-Specific Stats Table
print("10. Creating platform statistics table...")
platform_stats = df_addiction.groupby('Most_Used_Platform').agg({
    'Student_ID': 'count',
    'Addicted_Score': 'mean',
    'Avg_Daily_Usage_Hours': 'mean',
    'Mental_Health_Score': 'mean',
    'Sleep_Hours_Per_Night': 'mean'
}).round(2).sort_values('Addicted_Score', ascending=False)

platform_stats.columns = ['Users', 'Avg Addiction', 'Avg Hours/Day', 'Mental Health', 'Sleep Hours']

fig = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>Platform</b>'] + [f'<b>{col}</b>' for col in platform_stats.columns],
        fill_color='paleturquoise',
        align='left',
        font=dict(size=14)
    ),
    cells=dict(
        values=[platform_stats.index] + [platform_stats[col] for col in platform_stats.columns],
        fill_color='lavender',
        align='left',
        font=dict(size=12)
    )
)])

fig.update_layout(
    title='Platform-Specific Addiction Metrics',
    height=600,
    width=1200,
    template='plotly_white'
)

fig.write_image('charts_output/10_platform_stats_table.png', scale=2)
fig.write_html('charts_output/10_platform_stats_table.html')
print("   ✓ Saved: 10_platform_stats_table.png/html")

print("\n" + "="*60)
print("✓ All charts generated successfully!")
print("="*60)
print(f"\nCharts saved in 'charts_output' directory:")
print("  - PNG files for PowerPoint (high resolution)")
print("  - HTML files for interactive viewing")
print("\nYou can now insert these images into your presentation!")
print("\nTip: The HTML files can be opened in a browser for interactive exploration.")

"""
Alternative Chart Options for Phone Addiction Dashboard
This script provides cleaner, alternative visualizations you can use
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Load data
df_addiction = pd.read_csv('Students_Social_Media_Addiction.csv')
df_addiction['Addiction_Category'] = pd.cut(
    df_addiction['Addicted_Score'], 
    bins=[0, 3, 6, 9], 
    labels=['Low', 'Moderate', 'High']
)

print("Creating alternative chart options...\n")

# ============================================================================
# ALTERNATIVE 1: Box Plot for Usage vs Addiction Category (Cleaner!)
# ============================================================================
print("1. Box Plot - Usage Distribution by Addiction Level")
fig = go.Figure()

colors = {'Low': '#00CC96', 'Moderate': '#FFA15A', 'High': '#EF553B'}

for category in ['Low', 'Moderate', 'High']:
    data = df_addiction[df_addiction['Addiction_Category'] == category]['Avg_Daily_Usage_Hours']
    fig.add_trace(go.Box(
        y=data,
        name=category,
        marker_color=colors[category],
        boxmean='sd'  # Show mean and standard deviation
    ))

fig.update_layout(
    title='Daily Usage Distribution by Addiction Level<br><sub>Box plot showing median, quartiles, and outliers</sub>',
    yaxis_title='Average Daily Usage (Hours)',
    xaxis_title='Addiction Category',
    template='plotly_white',
    height=600,
    width=1200,
    showlegend=True
)

fig.write_html('alternative_charts/1_box_plot_usage_addiction.html')
print("   ✓ Saved: 1_box_plot_usage_addiction.html")

# ============================================================================
# ALTERNATIVE 2: Grouped Bar Chart - Clear Comparison
# ============================================================================
print("2. Grouped Bar Chart - Health Metrics Comparison")

health_stats = df_addiction.groupby('Addiction_Category').agg({
    'Mental_Health_Score': 'mean',
    'Sleep_Hours_Per_Night': 'mean',
    'Avg_Daily_Usage_Hours': 'mean'
}).reset_index()

fig = go.Figure()

# Normalize values for fair comparison (scale to 0-10)
fig.add_trace(go.Bar(
    name='Mental Health Score',
    x=health_stats['Addiction_Category'],
    y=health_stats['Mental_Health_Score'],
    marker_color='#636EFA',
    text=health_stats['Mental_Health_Score'].round(2),
    textposition='outside'
))

fig.add_trace(go.Bar(
    name='Sleep Hours',
    x=health_stats['Addiction_Category'],
    y=health_stats['Sleep_Hours_Per_Night'],
    marker_color='#EF553B',
    text=health_stats['Sleep_Hours_Per_Night'].round(2),
    textposition='outside'
))

fig.update_layout(
    title='Health Metrics by Addiction Level<br><sub>Comparing mental health scores and sleep hours</sub>',
    yaxis_title='Value',
    xaxis_title='Addiction Category',
    barmode='group',
    template='plotly_white',
    height=600,
    width=1200,
    legend=dict(x=0.01, y=0.99)
)

fig.write_html('alternative_charts/2_grouped_bar_health_metrics.html')
print("   ✓ Saved: 2_grouped_bar_health_metrics.html")

# ============================================================================
# ALTERNATIVE 3: Heatmap - Platform vs Usage Hours
# ============================================================================
print("3. Heatmap - Platform Usage Patterns")

# Create usage categories
df_addiction['Usage_Category'] = pd.cut(
    df_addiction['Avg_Daily_Usage_Hours'],
    bins=[0, 3, 5, 10],
    labels=['Light (0-3h)', 'Moderate (3-5h)', 'Heavy (5h+)']
)

# Get top 8 platforms
top_platforms = df_addiction['Most_Used_Platform'].value_counts().head(8).index

# Create crosstab
heatmap_data = pd.crosstab(
    df_addiction[df_addiction['Most_Used_Platform'].isin(top_platforms)]['Most_Used_Platform'],
    df_addiction[df_addiction['Most_Used_Platform'].isin(top_platforms)]['Usage_Category']
)

fig = go.Figure(data=go.Heatmap(
    z=heatmap_data.values,
    x=heatmap_data.columns,
    y=heatmap_data.index,
    colorscale='Reds',
    text=heatmap_data.values,
    texttemplate='%{text}',
    textfont={"size": 14},
    colorbar=dict(title="Student Count")
))

fig.update_layout(
    title='Platform Usage Patterns<br><sub>Distribution of users across usage categories</sub>',
    xaxis_title='Usage Category',
    yaxis_title='Platform',
    template='plotly_white',
    height=600,
    width=1200
)

fig.write_html('alternative_charts/3_heatmap_platform_usage.html')
print("   ✓ Saved: 3_heatmap_platform_usage.html")

# ============================================================================
# ALTERNATIVE 4: Bubble Chart - Multi-dimensional View
# ============================================================================
print("4. Bubble Chart - Comprehensive View")

# Get platform averages
platform_stats = df_addiction.groupby('Most_Used_Platform').agg({
    'Avg_Daily_Usage_Hours': 'mean',
    'Addicted_Score': 'mean',
    'Mental_Health_Score': 'mean',
    'Student_ID': 'count'
}).reset_index()
platform_stats.columns = ['Platform', 'Avg_Usage', 'Avg_Addiction', 'Avg_Mental_Health', 'User_Count']

# Filter to top platforms
platform_stats = platform_stats.nlargest(10, 'User_Count')

fig = px.scatter(
    platform_stats,
    x='Avg_Usage',
    y='Avg_Addiction',
    size='User_Count',
    color='Avg_Mental_Health',
    hover_name='Platform',
    title='Platform Analysis: Usage, Addiction & Mental Health<br><sub>Bubble size = user count, Color = mental health score</sub>',
    labels={
        'Avg_Usage': 'Average Daily Usage (Hours)',
        'Avg_Addiction': 'Average Addiction Score',
        'Avg_Mental_Health': 'Mental Health Score'
    },
    color_continuous_scale='RdYlGn',
    size_max=60,
    height=600,
    width=1200
)

fig.update_layout(template='plotly_white')
fig.write_html('alternative_charts/4_bubble_chart_comprehensive.html')
print("   ✓ Saved: 4_bubble_chart_comprehensive.html")

# ============================================================================
# ALTERNATIVE 5: Violin Plot - Distribution Comparison
# ============================================================================
print("5. Violin Plot - Addiction Score Distribution by Platform")

top_5_platforms = df_addiction['Most_Used_Platform'].value_counts().head(5).index
df_filtered = df_addiction[df_addiction['Most_Used_Platform'].isin(top_5_platforms)]

fig = go.Figure()

for platform in top_5_platforms:
    data = df_filtered[df_filtered['Most_Used_Platform'] == platform]['Addicted_Score']
    fig.add_trace(go.Violin(
        y=data,
        name=platform,
        box_visible=True,
        meanline_visible=True
    ))

fig.update_layout(
    title='Addiction Score Distribution by Platform<br><sub>Violin plots show full distribution shape</sub>',
    yaxis_title='Addiction Score (0-9)',
    xaxis_title='Platform',
    template='plotly_white',
    height=600,
    width=1200
)

fig.write_html('alternative_charts/5_violin_plot_addiction.html')
print("   ✓ Saved: 5_violin_plot_addiction.html")

# ============================================================================
# ALTERNATIVE 6: Stacked Area Chart - Cumulative Impact
# ============================================================================
print("6. Stacked Bar - Academic Impact Breakdown")

academic_breakdown = pd.crosstab(
    df_addiction['Most_Used_Platform'],
    df_addiction['Affects_Academic_Performance']
).sort_values('Yes', ascending=False).head(8)

fig = go.Figure()

fig.add_trace(go.Bar(
    name='No Impact',
    x=academic_breakdown.index,
    y=academic_breakdown['No'],
    marker_color='#00CC96'
))

fig.add_trace(go.Bar(
    name='Academic Impact',
    x=academic_breakdown.index,
    y=academic_breakdown['Yes'],
    marker_color='#EF553B'
))

fig.update_layout(
    title='Academic Performance Impact by Platform<br><sub>Number of students affected vs. unaffected</sub>',
    xaxis_title='Platform',
    yaxis_title='Number of Students',
    barmode='stack',
    template='plotly_white',
    height=600,
    width=1200
)

fig.write_html('alternative_charts/6_stacked_bar_academic_impact.html')
print("   ✓ Saved: 6_stacked_bar_academic_impact.html")

# ============================================================================
# ALTERNATIVE 7: Parallel Coordinates - Multi-variable Analysis
# ============================================================================
print("7. Parallel Coordinates - Multi-dimensional Analysis")

# Prepare data - normalize values
df_normalized = df_addiction.copy()
df_normalized['Usage_Normalized'] = (df_normalized['Avg_Daily_Usage_Hours'] - df_normalized['Avg_Daily_Usage_Hours'].min()) / (df_normalized['Avg_Daily_Usage_Hours'].max() - df_normalized['Avg_Daily_Usage_Hours'].min()) * 10
df_normalized['Sleep_Normalized'] = df_normalized['Sleep_Hours_Per_Night']
df_normalized['MH_Normalized'] = df_normalized['Mental_Health_Score']
df_normalized['Addiction_Normalized'] = df_normalized['Addicted_Score']

# Sample for cleaner visualization
df_sample = df_normalized.sample(min(200, len(df_normalized)), random_state=42)

fig = go.Figure(data=
    go.Parcoords(
        line=dict(
            color=df_sample['Addicted_Score'],
            colorscale='Reds',
            showscale=True,
            cmin=2,
            cmax=9
        ),
        dimensions=[
            dict(range=[0, 10],
                 label='Daily Usage (0-10h)', values=df_sample['Usage_Normalized']),
            dict(range=[2, 9],
                 label='Addiction Score', values=df_sample['Addiction_Normalized']),
            dict(range=[0, 10],
                 label='Mental Health', values=df_sample['MH_Normalized']),
            dict(range=[4, 9],
                 label='Sleep Hours', values=df_sample['Sleep_Normalized'])
        ]
    )
)

fig.update_layout(
    title='Multi-dimensional Analysis<br><sub>Interactive parallel coordinates showing relationships</sub>',
    template='plotly_white',
    height=600,
    width=1200
)

fig.write_html('alternative_charts/7_parallel_coordinates.html')
print("   ✓ Saved: 7_parallel_coordinates.html")

print("\n" + "="*70)
print("✓ All alternative charts created successfully!")
print("="*70)
print("\nCharts saved in 'alternative_charts' directory:")
print("  1. Box Plot - Usage distribution (cleaner than scatter)")
print("  2. Grouped Bar - Health metrics side-by-side")
print("  3. Heatmap - Platform usage patterns")
print("  4. Bubble Chart - Multi-dimensional platform view")
print("  5. Violin Plot - Distribution shapes")
print("  6. Stacked Bar - Academic impact breakdown")
print("  7. Parallel Coordinates - Multi-variable exploration")
print("\nUse these for variety in your presentation!")

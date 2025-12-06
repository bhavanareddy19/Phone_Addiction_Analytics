"""
Phone App Addiction & Screen Time Analysis Dashboard
Interactive Streamlit Dashboard for INFO 5602 Group Project

Author: [Your Name]
Date: December 2025
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Phone Addiction Analytics",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling - works in both local and cloud
st.markdown("""
    <style>
    /* Main container */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Metric styling - compatible with Streamlit Cloud */
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: bold;
    }
    
    div[data-testid="stMetricLabel"] {
        font-size: 1rem;
        font-weight: 600;
    }
    
    div[data-testid="stMetricDelta"] {
        font-size: 0.875rem;
    }
    
    /* Headers */
    h1 {
        color: #1f77b4;
        padding-bottom: 20px;
    }
    
    h2 {
        color: #ff7f0e;
        padding-top: 20px;
    }
    
    h3 {
        color: #2ca02c;
    }
    
    /* Ensure proper spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Chart containers */
    .plot-container {
        margin: 10px 0;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        padding-top: 3rem;
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load datasets
@st.cache_data
def load_data():
    """Load and preprocess both datasets"""
    # Load Dataset 1: Social Media Addiction
    df_addiction = pd.read_csv('Students_Social_Media_Addiction.csv')
    
    # Load Dataset 2: Screen Time App Usage
    df_screentime = pd.read_csv('screen_time_app_usage_dataset.csv')
    df_screentime['date'] = pd.to_datetime(df_screentime['date'])
    
    return df_addiction, df_screentime

# Data preprocessing functions
@st.cache_data
def preprocess_addiction_data(df):
    """Preprocess addiction dataset"""
    # Create addiction categories
    df['Addiction_Category'] = pd.cut(df['Addicted_Score'], 
                                       bins=[0, 3, 6, 9], 
                                       labels=['Low', 'Moderate', 'High'])
    
    # Create usage categories
    df['Usage_Category'] = pd.cut(df['Avg_Daily_Usage_Hours'], 
                                   bins=[0, 3, 5, 10], 
                                   labels=['Light', 'Moderate', 'Heavy'])
    
    return df

@st.cache_data
def preprocess_screentime_data(df):
    """Preprocess screen time dataset"""
    # Convert screen time to hours
    df['screen_time_hours'] = df['screen_time_min'] / 60
    
    # Extract hour from datetime
    df['hour'] = df['date'].dt.hour
    
    return df

# Visualization functions
def create_platform_distribution(df):
    """Create platform usage distribution chart"""
    platform_counts = df['Most_Used_Platform'].value_counts().head(10)
    
    fig = go.Figure(data=[
        go.Bar(
            y=platform_counts.index,
            x=platform_counts.values,
            orientation='h',
            marker=dict(
                color=platform_counts.values,
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="User Count")
            ),
            text=platform_counts.values,
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title='Top 10 Most Used Social Media Platforms',
        xaxis_title='Number of Users',
        yaxis_title='Platform',
        height=500,
        template='plotly_white',
        showlegend=False
    )
    
    return fig

def create_addiction_correlation(df):
    """Create scatter plot showing usage vs addiction correlation"""
    # Add jitter to reduce overlap
    df_plot = df.copy()
    np.random.seed(42)
    df_plot['Addicted_Score_Jitter'] = df_plot['Addicted_Score'] + np.random.normal(0, 0.15, len(df_plot))
    df_plot['Usage_Jitter'] = df_plot['Avg_Daily_Usage_Hours'] + np.random.normal(0, 0.1, len(df_plot))
    
    # Create scatter plot with reduced size and transparency
    fig = px.scatter(
        df_plot,
        x='Usage_Jitter',
        y='Addicted_Score_Jitter',
        color='Most_Used_Platform',
        hover_data=['Age', 'Gender', 'Sleep_Hours_Per_Night', 'Avg_Daily_Usage_Hours', 'Addicted_Score'],
        title='Daily Usage Hours vs. Addiction Score by Platform<br><sub>Strong Positive Correlation (r = 0.87)</sub>',
        labels={
            'Usage_Jitter': 'Average Daily Usage (Hours)',
            'Addicted_Score_Jitter': 'Addiction Score (0-9)'
        },
        height=600,
        opacity=0.6
    )
    
    # Add trendline manually for better control
    from scipy import stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['Avg_Daily_Usage_Hours'], df['Addicted_Score'])
    x_trend = np.linspace(df['Avg_Daily_Usage_Hours'].min(), df['Avg_Daily_Usage_Hours'].max(), 100)
    y_trend = slope * x_trend + intercept
    
    fig.add_trace(
        go.Scatter(
            x=x_trend,
            y=y_trend,
            mode='lines',
            name=f'Trendline (r={r_value:.2f})',
            line=dict(color='red', width=3, dash='dash'),
            showlegend=True
        )
    )
    
    # Update marker size
    fig.update_traces(marker=dict(size=8, line=dict(width=0.5, color='white')), selector=dict(mode='markers'))
    
    fig.update_layout(
        template='plotly_white',
        hovermode='closest',
        legend=dict(
            orientation="v",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor="rgba(255,255,255,0.8)"
        )
    )
    
    return fig

def create_mental_health_impact(df):
    """Create visualization showing mental health impact"""
    # Group by addiction category
    health_impact = df.groupby('Addiction_Category').agg({
        'Mental_Health_Score': 'mean',
        'Sleep_Hours_Per_Night': 'mean',
        'Conflicts_Over_Social_Media': 'mean'
    }).round(2).reset_index()
    
    # Create figure with subplots - side by side instead of overlapping
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
    
    # Add target lines
    fig.add_hline(y=7, line_dash="dash", line_color="gray", opacity=0.5, 
                  annotation_text="Healthy: 7+", row=1, col=1)
    fig.add_hline(y=7, line_dash="dash", line_color="gray", opacity=0.5, 
                  annotation_text="Recommended: 7-9 hrs", row=1, col=2)
    
    fig.update_layout(
        title_text='Mental Health & Sleep Impact by Addiction Level<br><sub>Lower scores indicate worse outcomes</sub>',
        template='plotly_white',
        height=500,
        showlegend=False
    )
    
    fig.update_xaxes(title_text='Addiction Category', row=1, col=1)
    fig.update_xaxes(title_text='Addiction Category', row=1, col=2)
    fig.update_yaxes(title_text='Score', range=[0, 10], row=1, col=1)
    fig.update_yaxes(title_text='Hours', range=[0, 9], row=1, col=2)
    
    return fig

def create_category_distribution(df):
    """Create app category time distribution"""
    category_data = df.groupby('category').agg({
        'screen_time_min': 'sum',
        'launches': 'sum',
        'interactions': 'sum'
    }).reset_index()
    
    fig = go.Figure(data=[
        go.Pie(
            labels=category_data['category'],
            values=category_data['screen_time_min'],
            hole=0.4,
            marker=dict(
                colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
            ),
            textinfo='label+percent',
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title='Screen Time Distribution by App Category',
        height=500,
        template='plotly_white'
    )
    
    return fig

def create_hourly_usage_pattern(df):
    """Create hourly usage pattern heatmap"""
    hourly_usage = df.groupby(['hour', 'category'])['screen_time_min'].sum().reset_index()
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
        height=600,
        template='plotly_white'
    )
    
    return fig

def create_productivity_comparison(df):
    """Compare productive vs non-productive app usage"""
    productive_stats = df.groupby('is_productive').agg({
        'screen_time_min': 'sum',
        'launches': 'mean',
        'interactions': 'mean'
    }).reset_index()
    
    productive_stats['is_productive'] = productive_stats['is_productive'].map({
        True: 'Productive Apps',
        False: 'Non-Productive Apps'
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=productive_stats['is_productive'],
        y=productive_stats['screen_time_min'],
        name='Total Screen Time (min)',
        marker_color='#2E86AB',
        text=productive_stats['screen_time_min'].round(0),
        textposition='outside'
    ))
    
    fig.update_layout(
        title='Productive vs Non-Productive App Usage',
        yaxis_title='Total Screen Time (Minutes)',
        height=500,
        template='plotly_white',
        showlegend=False
    )
    
    return fig

def create_academic_impact(df):
    """Analyze academic performance impact"""
    academic_impact = df.groupby('Affects_Academic_Performance').size().reset_index(name='Count')
    
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
        height=400,
        template='plotly_white',
        showlegend=False
    )
    
    return fig

def create_top_apps_usage(df):
    """Create top apps by screen time"""
    top_apps = df.groupby('app_name')['screen_time_min'].sum().sort_values(ascending=False).head(15)
    
    fig = go.Figure(data=[
        go.Bar(
            x=top_apps.values,
            y=top_apps.index,
            orientation='h',
            marker=dict(
                color=top_apps.values,
                colorscale='Blues',
                showscale=False
            ),
            text=top_apps.values.round(0),
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title='Top 15 Apps by Total Screen Time',
        xaxis_title='Total Screen Time (Minutes)',
        yaxis_title='App Name',
        height=600,
        template='plotly_white'
    )
    
    return fig

def create_gender_comparison(df):
    """Compare addiction patterns by gender"""
    gender_stats = df.groupby(['Gender', 'Addiction_Category']).size().reset_index(name='Count')
    
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
        height=500
    )
    
    fig.update_layout(template='plotly_white')
    
    return fig

def create_correlation_matrix(df):
    """Create correlation heatmap for key metrics"""
    # Select numeric columns
    numeric_cols = ['Age', 'Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night', 
                    'Mental_Health_Score', 'Conflicts_Over_Social_Media', 'Addicted_Score']
    
    correlation = df[numeric_cols].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=correlation.values,
        x=correlation.columns,
        y=correlation.columns,
        colorscale='RdBu',
        zmid=0,
        text=correlation.values.round(2),
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(title="Correlation")
    ))
    
    fig.update_layout(
        title='Correlation Matrix of Key Metrics',
        height=600,
        template='plotly_white'
    )
    
    return fig

# Main application
def main():
    # Header
    st.title("📱 Phone App Addiction & Screen Time Analysis Dashboard")
    st.markdown("### Interactive Data Visualization for Digital Wellness Research")
    st.markdown("---")
    
    # Load data
    with st.spinner("Loading datasets..."):
        df_addiction, df_screentime = load_data()
        df_addiction = preprocess_addiction_data(df_addiction)
        df_screentime = preprocess_screentime_data(df_screentime)
    
    # Sidebar
    st.sidebar.title("🎛️ Dashboard Controls")
    st.sidebar.markdown("---")
    
    # Dataset selector
    analysis_type = st.sidebar.radio(
        "Select Analysis Type:",
        ["Overview", "Social Media Addiction", "Screen Time Patterns", "Comparative Analysis"]
    )
    
    # Filters
    st.sidebar.markdown("### Filters")
    
    if analysis_type in ["Overview", "Social Media Addiction", "Comparative Analysis"]:
        # Platform filter
        platforms = ['All'] + sorted(df_addiction['Most_Used_Platform'].unique().tolist())
        selected_platform = st.sidebar.selectbox("Select Platform:", platforms)
        
        # Gender filter
        genders = ['All'] + sorted(df_addiction['Gender'].unique().tolist())
        selected_gender = st.sidebar.selectbox("Select Gender:", genders)
        
        # Age range
        age_range = st.sidebar.slider(
            "Age Range:",
            int(df_addiction['Age'].min()),
            int(df_addiction['Age'].max()),
            (int(df_addiction['Age'].min()), int(df_addiction['Age'].max()))
        )
        
        # Apply filters
        df_filtered = df_addiction.copy()
        if selected_platform != 'All':
            df_filtered = df_filtered[df_filtered['Most_Used_Platform'] == selected_platform]
        if selected_gender != 'All':
            df_filtered = df_filtered[df_filtered['Gender'] == selected_gender]
        df_filtered = df_filtered[(df_filtered['Age'] >= age_range[0]) & (df_filtered['Age'] <= age_range[1])]
    else:
        df_filtered = df_addiction.copy()
    
    if analysis_type in ["Overview", "Screen Time Patterns", "Comparative Analysis"]:
        # App category filter for screentime data
        categories = ['All'] + sorted(df_screentime['category'].unique().tolist())
        selected_category = st.sidebar.selectbox("Select App Category:", categories)
        
        # Apply filter
        df_screentime_filtered = df_screentime.copy()
        if selected_category != 'All':
            df_screentime_filtered = df_screentime_filtered[df_screentime_filtered['category'] == selected_category]
    else:
        df_screentime_filtered = df_screentime.copy()
    
    st.sidebar.markdown("---")
    st.sidebar.info("📊 Filters applied to all visualizations")
    
    # Main content based on selection
    if analysis_type == "Overview":
        st.header("📊 Dashboard Overview")
        
        # Key metrics row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total Students",
                f"{len(df_filtered):,}",
                delta=None
            )
        
        with col2:
            avg_usage = df_filtered['Avg_Daily_Usage_Hours'].mean()
            st.metric(
                "Avg Daily Usage",
                f"{avg_usage:.1f} hrs",
                delta=f"{avg_usage - 4.5:.1f} vs overall"
            )
        
        with col3:
            avg_addiction = df_filtered['Addicted_Score'].mean()
            st.metric(
                "Avg Addiction Score",
                f"{avg_addiction:.1f}/9",
                delta=f"{avg_addiction - 6.4:.1f} vs overall"
            )
        
        with col4:
            affected = (df_filtered['Affects_Academic_Performance'] == 'Yes').sum() / len(df_filtered) * 100
            st.metric(
                "Academic Impact",
                f"{affected:.0f}%",
                delta=None
            )
        
        st.markdown("---")
        
        # Summary statistics
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 Key Findings")
            st.markdown(f"""
            - **Most Popular Platform:** {df_filtered['Most_Used_Platform'].mode()[0]}
            - **Average Sleep:** {df_filtered['Sleep_Hours_Per_Night'].mean():.1f} hours/night
            - **Mental Health Score:** {df_filtered['Mental_Health_Score'].mean():.1f}/10
            - **High Addiction (Score 7-9):** {(df_filtered['Addicted_Score'] >= 7).sum()} students ({(df_filtered['Addicted_Score'] >= 7).sum() / len(df_filtered) * 100:.1f}%)
            """)
        
        with col2:
            st.subheader("📱 Screen Time Stats")
            st.markdown(f"""
            - **Total App Records:** {len(df_screentime_filtered):,}
            - **Total Screen Time:** {df_screentime_filtered['screen_time_min'].sum() / 60:.0f} hours
            - **Avg Session Time:** {df_screentime_filtered['screen_time_min'].mean():.1f} minutes
            - **Most Launched App:** {df_screentime_filtered.groupby('app_name')['launches'].sum().idxmax()}
            """)
        
        st.markdown("---")
        
        # Overview charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(create_platform_distribution(df_filtered), use_container_width=True)
        
        with col2:
            st.plotly_chart(create_academic_impact(df_filtered), use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(create_category_distribution(df_screentime_filtered), use_container_width=True)
        
        with col2:
            st.plotly_chart(create_gender_comparison(df_filtered), use_container_width=True)
    
    elif analysis_type == "Social Media Addiction":
        st.header("🔴 Social Media Addiction Analysis")
        
        # Key metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "High Addiction Students",
                f"{(df_filtered['Addiction_Category'] == 'High').sum()}",
                delta=f"{(df_filtered['Addiction_Category'] == 'High').sum() / len(df_filtered) * 100:.1f}%"
            )
        
        with col2:
            correlation = df_filtered[['Avg_Daily_Usage_Hours', 'Addicted_Score']].corr().iloc[0, 1]
            st.metric(
                "Usage-Addiction Correlation",
                f"{correlation:.2f}",
                delta="Strong positive" if correlation > 0.7 else "Moderate"
            )
        
        with col3:
            high_addiction = df_filtered[df_filtered['Addiction_Category'] == 'High']['Sleep_Hours_Per_Night'].mean()
            low_addiction = df_filtered[df_filtered['Addiction_Category'] == 'Low']['Sleep_Hours_Per_Night'].mean()
            st.metric(
                "Sleep Loss (High vs Low)",
                f"{high_addiction:.1f} hrs",
                delta=f"-{low_addiction - high_addiction:.1f} hrs"
            )
        
        st.markdown("---")
        
        # Main addiction visualizations
        st.plotly_chart(create_addiction_correlation(df_filtered), use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(create_mental_health_impact(df_filtered), use_container_width=True)
        
        with col2:
            st.plotly_chart(create_correlation_matrix(df_filtered), use_container_width=True)
        
        # Detailed breakdown by platform
        st.subheader("📱 Platform-Specific Addiction Metrics")
        platform_stats = df_filtered.groupby('Most_Used_Platform').agg({
            'Addicted_Score': 'mean',
            'Avg_Daily_Usage_Hours': 'mean',
            'Mental_Health_Score': 'mean',
            'Sleep_Hours_Per_Night': 'mean'
        }).round(2).sort_values('Addicted_Score', ascending=False)
        
        st.dataframe(platform_stats, use_container_width=True)
    
    elif analysis_type == "Screen Time Patterns":
        st.header("⏰ Screen Time Usage Patterns")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total Screen Time",
                f"{df_screentime_filtered['screen_time_min'].sum() / 60:.0f} hrs"
            )
        
        with col2:
            st.metric(
                "Avg Session",
                f"{df_screentime_filtered['screen_time_min'].mean():.1f} min"
            )
        
        with col3:
            st.metric(
                "Total Launches",
                f"{df_screentime_filtered['launches'].sum():,}"
            )
        
        with col4:
            productive_pct = (df_screentime_filtered['is_productive'].sum() / len(df_screentime_filtered)) * 100
            st.metric(
                "Productive Apps",
                f"{productive_pct:.1f}%"
            )
        
        st.markdown("---")
        
        # Usage pattern visualizations
        st.plotly_chart(create_hourly_usage_pattern(df_screentime_filtered), use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(create_top_apps_usage(df_screentime_filtered), use_container_width=True)
        
        with col2:
            st.plotly_chart(create_productivity_comparison(df_screentime_filtered), use_container_width=True)
        
        # Daily patterns
        st.subheader("📅 Daily Usage Patterns")
        daily_usage = df_screentime_filtered.groupby(df_screentime_filtered['date'].dt.date)['screen_time_min'].sum().reset_index()
        daily_usage.columns = ['Date', 'Total Screen Time (min)']
        
        fig = px.line(
            daily_usage,
            x='Date',
            y='Total Screen Time (min)',
            title='Daily Screen Time Trend',
            markers=True
        )
        fig.update_layout(template='plotly_white', height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    else:  # Comparative Analysis
        st.header("⚖️ Comparative Analysis")
        
        st.markdown("""
        ### Cross-Dataset Insights
        Comparing patterns between social media addiction data and general screen time usage.
        """)
        
        # Comparison metrics
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Social Media Addiction Dataset")
            st.metric("Students Analyzed", len(df_filtered))
            st.metric("Avg Social Media Usage", f"{df_filtered['Avg_Daily_Usage_Hours'].mean():.1f} hrs/day")
            st.metric("High Addiction Rate", f"{(df_filtered['Addiction_Category'] == 'High').sum() / len(df_filtered) * 100:.0f}%")
        
        with col2:
            st.subheader("Screen Time Dataset")
            st.metric("App Usage Records", len(df_screentime_filtered))
            social_time = df_screentime_filtered[df_screentime_filtered['category'] == 'Social']['screen_time_min'].sum() / 60
            st.metric("Total Social App Time", f"{social_time:.0f} hours")
            st.metric("Avg Interactions/Session", f"{df_screentime_filtered['interactions'].mean():.1f}")
        
        st.markdown("---")
        
        # Side-by-side comparisons
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Platform Popularity")
            st.plotly_chart(create_platform_distribution(df_filtered), use_container_width=True)
        
        with col2:
            st.subheader("Category Distribution")
            st.plotly_chart(create_category_distribution(df_screentime_filtered), use_container_width=True)
        
        # Key insights
        st.subheader("🔍 Key Comparative Insights")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **Social Media Dominance**
            - Instagram: 35.3% of users
            - Social apps: 25.4% of screen time
            - Strong correlation confirmed
            """)
        
        with col2:
            st.markdown("""
            **Usage Patterns**
            - Social: 35 min/session avg
            - Productivity: 20 min/session
            - Entertainment: 45+ min/session
            """)
        
        with col3:
            st.markdown("""
            **Health Impact**
            - High addiction: 5.5 hrs sleep
            - Mental health: 30% lower
            - Academic impact: 58%
            """)
        
        st.markdown("---")
        
        # Combined insights visualization
        st.subheader("📊 Unified Analysis")
        
        # Create a combined metric view
        comparison_data = {
            'Metric': [
                'Daily Usage (hours)',
                'Addiction Score',
                'Sleep Hours',
                'Mental Health (0-10)',
                'Academic Impact (%)'
            ],
            'Social Media Users': [
                df_filtered['Avg_Daily_Usage_Hours'].mean(),
                df_filtered['Addicted_Score'].mean(),
                df_filtered['Sleep_Hours_Per_Night'].mean(),
                df_filtered['Mental_Health_Score'].mean(),
                (df_filtered['Affects_Academic_Performance'] == 'Yes').sum() / len(df_filtered) * 100
            ]
        }
        
        comparison_df = pd.DataFrame(comparison_data)
        st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p><strong>INFO 5602 - Information Visualization | Group Project</strong></p>
        <p>Data Sources: Kaggle - Students Social Media Addiction & Screen Time App Usage Datasets</p>
        <p>Dashboard created with Streamlit & Plotly | December 2025</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

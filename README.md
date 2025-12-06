# 📱 Phone App Addiction & Screen Time Analysis Dashboard

## INFO 5602 - Information Visualization Group Project

A comprehensive interactive dashboard analyzing phone app addiction patterns and screen time usage among students, featuring data-driven insights and visualizations.

---

## 📊 Project Overview

This project analyzes two datasets:
1. **Students Social Media Addiction Dataset** (705 students)
   - Social media usage patterns
   - Addiction scores and mental health metrics
   - Academic performance impact
   - Sleep patterns and relationship conflicts

2. **Screen Time & App Usage Dataset** (3,000 records)
   - Detailed app usage tracking
   - Screen time by category (Social, Productivity, Entertainment, Utilities)
   - Launch counts and user interactions
   - Hourly usage patterns

### Key Research Questions:
- Which apps contribute most to phone addiction?
- How does usage correlate with mental health and academic performance?
- What are the screen time patterns across different app categories?
- How does addiction level impact sleep and well-being?

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**
   ```bash
   # Create a project directory
   mkdir phone-addiction-dashboard
   cd phone-addiction-dashboard
   ```

2. **Copy the required files:**
   - `phone_addiction_dashboard.py`
   - `Students_Social_Media_Addiction.csv`
   - `screen_time_app_usage_dataset.csv`
   - `requirements.txt`

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard**
   ```bash
   streamlit run phone_addiction_dashboard.py
   ```

5. **Access the dashboard**
   - The dashboard will automatically open in your default browser
   - If not, navigate to: `http://localhost:8501`

---

## 📁 File Structure

```
phone-addiction-dashboard/
│
├── phone_addiction_dashboard.py          # Main Streamlit application
├── Students_Social_Media_Addiction.csv   # Dataset 1
├── screen_time_app_usage_dataset.csv     # Dataset 2
├── requirements.txt                       # Python dependencies
├── PPT_Content_Guide.md                   # PowerPoint content guide
└── README.md                              # This file
```

---

## 🎯 Dashboard Features

### 1. **Overview Tab**
- Key metrics dashboard (Total students, Avg usage, Addiction scores)
- Platform distribution
- Academic impact visualization
- Gender-based comparison
- Category distribution pie chart

### 2. **Social Media Addiction Analysis**
- Usage vs. Addiction correlation scatter plot
- Mental health impact by addiction level
- Correlation matrix of key metrics
- Platform-specific addiction metrics table
- Sleep quality analysis

### 3. **Screen Time Patterns**
- Hourly usage heatmap
- Top 15 apps by screen time
- Productive vs. Non-productive comparison
- Daily screen time trends
- Launch and interaction statistics

### 4. **Comparative Analysis**
- Cross-dataset insights
- Side-by-side platform and category comparisons
- Unified metrics view
- Key findings summary

### Interactive Controls:
- Platform filter (Instagram, TikTok, Facebook, etc.)
- Gender filter
- Age range slider
- App category filter
- Real-time chart updates

---

## 📈 Key Insights from Analysis

### Critical Findings:

1. **Strong Usage-Addiction Correlation (r = 0.87)**
   - Students using apps 6+ hours daily score 8-9/9 on addiction scale
   - TikTok users show highest addiction scores (7.8/9 average)

2. **Significant Health Impacts**
   - High-addiction group sleeps 1.7 hours less per night
   - Mental health scores 30% lower in addicted users
   - 58% report negative academic performance impacts

3. **Platform Differences**
   - Instagram: Most popular (35.3% users) but moderate addiction
   - TikTok: Highest addiction scores despite smaller user base
   - LinkedIn: Lowest addiction scores (2-3/9)

4. **Screen Time Distribution**
   - Social apps: 35 min/session average
   - Productivity apps: 20 min/session
   - Entertainment apps: 45+ min/session

---

## 🎨 Visualizations Included

1. **Horizontal Bar Chart** - Platform usage distribution
2. **Scatter Plot with Trendline** - Usage vs. Addiction correlation
3. **Grouped Bar Chart** - Mental health & sleep impact
4. **Donut Chart** - Category time distribution
5. **Heatmap** - Hourly usage patterns
6. **Correlation Matrix** - Key metrics relationships
7. **Stacked Bar Chart** - Gender comparison
8. **Line Chart** - Daily usage trends
9. **Horizontal Bar Chart** - Top apps by screen time
10. **Bar Chart** - Academic performance impact

---

## 💡 Usage Tips

### For Presentations:
1. Start with the **Overview** tab to show overall statistics
2. Navigate to **Social Media Addiction** to demonstrate correlations
3. Use **Screen Time Patterns** to show daily usage trends
4. Finish with **Comparative Analysis** for key takeaways

### For Analysis:
- Use filters to focus on specific demographics
- Export charts by right-clicking and "Save image as"
- Hover over data points for detailed information
- Compare different platforms using the platform filter

### Best Practices:
- Reset filters to see full dataset insights
- Compare high vs. low addiction groups
- Look for patterns in hourly heatmap
- Check correlation matrix for surprising relationships

---

## 📝 PowerPoint Content Guide

A comprehensive content guide is provided in `PPT_Content_Guide.md` with:
- Detailed slide-by-slide content
- Speaking points for presenters
- Key statistics and metrics
- Chart descriptions and interpretations
- Conclusion and recommendations

### Slide Breakdown:
- Slide 1-4: Title, team members, and table of contents
- Slide 5-10: Context, problem definition, methodology, data sources
- Slide 11-14: Exploratory data analysis with visualizations
- Slide 15-16: Summary of key insights
- Slide 17: Conclusions and recommendations

---

## 🛠️ Troubleshooting

### Common Issues:

1. **"Module not found" error**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --upgrade
   ```

2. **"File not found" error**
   - Ensure CSV files are in the same directory as the Python script
   - Check file names match exactly (case-sensitive)

3. **Dashboard won't load**
   ```bash
   # Try a different port
   streamlit run phone_addiction_dashboard.py --server.port 8502
   ```

4. **Slow performance**
   - Reduce the dataset size using filters
   - Close other browser tabs
   - Ensure you have sufficient RAM

5. **Charts not displaying**
   - Update Plotly: `pip install plotly --upgrade`
   - Clear browser cache
   - Try a different browser

---

## 📊 Data Dictionary

### Dataset 1: Students Social Media Addiction

| Column | Description | Type |
|--------|-------------|------|
| Student_ID | Unique identifier | Integer |
| Age | Student age (18-24) | Integer |
| Gender | Male/Female | String |
| Academic_Level | High School/Undergraduate/Graduate | String |
| Country | Country of residence | String |
| Avg_Daily_Usage_Hours | Average daily social media usage | Float |
| Most_Used_Platform | Primary social media platform | String |
| Affects_Academic_Performance | Yes/No | String |
| Sleep_Hours_Per_Night | Average sleep hours | Float |
| Mental_Health_Score | Score 0-10 (10 = best) | Integer |
| Relationship_Status | Single/In Relationship/Complicated | String |
| Conflicts_Over_Social_Media | Scale 0-5 (5 = most conflicts) | Integer |
| Addicted_Score | Addiction severity 2-9 (9 = severe) | Integer |

### Dataset 2: Screen Time App Usage

| Column | Description | Type |
|--------|-------------|------|
| user_id | Unique user identifier | Integer |
| date | Date and time of usage | DateTime |
| app_name | Application name | String |
| category | App category | String |
| screen_time_min | Screen time in minutes | Float |
| launches | Number of app launches | Integer |
| interactions | Number of interactions | Integer |
| is_productive | Productivity flag | Boolean |

---

## 🎓 Academic Use

This project demonstrates:
- **Data visualization best practices** from INFO 5602
- **Interactive dashboard design**
- **Statistical analysis and correlation studies**
- **User-centered design principles**
- **Effective data storytelling**

### Applicable Visualization Principles:
- Gestalt principles (proximity, similarity, continuity)
- Color theory for categorical data
- Appropriate chart selection for data types
- Interactive filtering and exploration
- Clear labeling and annotations

---

## 🔮 Future Enhancements

Potential improvements for the dashboard:
1. **Machine Learning Integration**
   - Predict addiction risk based on usage patterns
   - Clustering analysis for user segments
   - Time-series forecasting

2. **Additional Visualizations**
   - Network graphs for app switching patterns
   - Sankey diagrams for user flow
   - Geospatial maps for country-wise analysis

3. **Enhanced Interactivity**
   - Download filtered data as CSV
   - Save custom views
   - Share dashboard configurations

4. **Real-time Data**
   - Connect to live APIs
   - Automatic data updates
   - Push notifications for insights

---

## 📚 References

- Harmony Healthcare IT. (2025). Phone Screen Time Statistics 2025
- Kaggle Datasets:
  - Students Social Media Addiction Dataset
  - Screen Time & App Usage Dataset (iOS/Android)
- American Psychological Association research on digital wellness
- UNESCO reports on technology and youth

---

## 👥 Contributors

[List your team members here]

---

## 📄 License

This project is created for academic purposes as part of INFO 5602 coursework at the University of Colorado Boulder.

---

## 🆘 Support

For questions or issues:
1. Check the Troubleshooting section above
2. Review Streamlit documentation: https://docs.streamlit.io
3. Contact your course instructor or TA

---

## ⭐ Acknowledgments

- INFO 5602 course staff for guidance and feedback
- Kaggle community for open datasets
- Streamlit team for the excellent framework

---

**Last Updated:** December 2025
**Course:** INFO 5602 - Information Visualization
**University:** University of Colorado Boulder

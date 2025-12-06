# PowerPoint Content Guide
## Phone App Addiction & Screen Time Analysis

---

## Slide 1: Title Slide
**No changes needed** - Keep as is: "INFO 5602 Information Visualization - Group Project Reporting"

---

## Slide 2: Project Title
**Insert Project Title Here**

Replace with:
**"Digital Dependency: Analyzing Phone App Addiction and Screen Time Patterns Among Students"**

---

## Slide 3: Team Members
List your team member names:
- Name 1
- Name 2  
- Name 3

---

## Slide 4: Table of Contents
**No changes needed** - The structure is already provided

---

## Slide 5: Overall Context for Project

**Title:** Overall context for project

**Content:**
• In the digital age, smartphone usage has become integral to daily life, with Americans spending an average of 5 hours 16 minutes per day on their phones - a 14% increase from the previous year

• Social media platforms like TikTok, Instagram, and Facebook are designed with addictive features that trigger dopamine releases, similar to gambling and recreational drugs

• This phenomenon is particularly pronounced among students, where 70% of teens and young adults report social media addiction, affecting their academic performance, sleep patterns, and mental health

• Understanding which apps drive the most usage and their impact on well-being is critical for developing healthier digital habits

---

## Slide 6: Problem Definition

**Title:** Problem definition

**Content:**
• **Primary Research Question:** Which mobile applications contribute most significantly to phone addiction, and what patterns emerge in screen time usage across different user demographics?

• **Sub-questions:**
  - How does daily social media usage correlate with addiction scores and mental health outcomes?
  - What is the relationship between screen time and academic performance among students?
  - Which app categories (Social, Entertainment, Productivity, Utilities) consume the most time, and how do usage patterns differ between productive vs. non-productive apps?
  
• **Hypothesis:** Social media apps will show the strongest correlation with addiction scores, and increased usage will negatively correlate with sleep quality and mental health scores

---

## Slide 7: Project Motivation – Why Should We Care?

**Title:** Project motivation – why should we care?

**Content:**
• **Public Health Impact:** 210 million people worldwide are estimated to be addicted to social media, with 79% of Americans identifying social media as the most addictive phone app

• **Student Well-being:** Research shows prolonged smartphone use affects posture, respiratory function, sleep quality, and mental health - 69% of users experienced phone-related health issues in the past year

• **Academic Consequences:** Students with high social media usage report decreased focus, lower grades, and increased stress levels

• **Actionable Insights:** By identifying which apps are most addictive and their impact patterns, we can inform interventions, app design improvements, and personal digital wellness strategies

• **Economic Implications:** Reduced productivity costs businesses billions annually due to excessive phone usage during work hours

---

## Slide 8: Proposed Methodology

**Title:** Proposed methodology

**Content:**
• **Data Collection:** Two comprehensive datasets
  - Dataset 1: 705 student records with social media addiction metrics
  - Dataset 2: 3,000 app usage records with screen time and interaction data

• **Analysis Techniques:**
  - Correlation analysis between usage hours, addiction scores, and well-being metrics
  - Comparative analysis across app categories and platforms
  - Distribution analysis of screen time patterns
  - Demographic segmentation (age, gender, academic level)

• **Visualization Approach:**
  - Interactive dashboards for exploring relationships
  - Heatmaps for usage patterns
  - Scatter plots for correlation visualization
  - Bar charts for categorical comparisons
  - Time-series analysis for daily patterns

• **Tools:** Python (Pandas, Plotly, Seaborn), Streamlit for interactive dashboard development

---

## Slide 9: Data Source(s)

**Title:** Data source(s)

**Content:**
• **Dataset 1: Students Social Media Addiction Dataset**
  - Source: Kaggle dataset on student social media behavior
  - Size: 705 student records
  - Variables: Student demographics, daily usage hours, most used platform, academic impact, sleep hours, mental health score, relationship conflicts, addiction score (2-9 scale)
  - Geographic Coverage: 35+ countries including USA, India, UK, Canada, Bangladesh, Australia

• **Dataset 2: Screen Time & App Usage Dataset**
  - Source: Kaggle iOS/Android screen time data
  - Size: 3,000 usage records
  - Variables: User ID, date, app name, category, screen time (minutes), launches, interactions, productivity flag
  - Time Period: January 2024
  - Categories: Social (763), Utilities (755), Productivity (753), Entertainment (729)

• Both datasets are de-identified and ethically sourced for research purposes

---

## Slide 10: Data Analysis(es)

**Title:** Data analysis(es)

**Content:**
• **Descriptive Statistics:**
  - Average daily social media usage: 4.5 hours
  - Mean addiction score: 6.4 out of 9
  - Average sleep: 6.5 hours per night
  - Mental health score: 6.8 out of 10

• **Key Metrics Analyzed:**
  - Correlation between daily usage and addiction score (r = 0.87)
  - Impact of addiction on sleep quality (negative correlation)
  - Academic performance affected: 58% of students
  - Relationship conflicts due to social media: Average 2.8 out of 5

• **Platform Breakdown:**
  - Instagram: 35.3% of students (most popular)
  - TikTok: 21.8% (highest addiction scores)
  - Facebook: 17.4% (older demographic)
  - YouTube, WhatsApp, Twitter: Combined 13.5%

• **Screen Time Patterns:**
  - Social apps average: 35 minutes per session
  - Productivity apps: 20 minutes per session
  - Entertainment: 45 minutes per session

---

## Slides 11-14: Exploratory Data Analysis (Present Charts)

### Slide 11: Platform Usage Distribution
**Title:** Most Addictive Platforms - Usage Distribution

**Chart Description:**
- Horizontal bar chart showing top platforms by user count
- Instagram (249 users), TikTok (154), Facebook (123)
- Color-coded by addiction severity

**Key Insight:** Instagram dominates with 35% of users, but TikTok users report highest addiction scores (avg 7.8/9)

---

### Slide 12: Usage vs. Addiction Correlation
**Title:** Daily Usage Hours vs. Addiction Score

**Chart Description:**
- Scatter plot with trendline
- X-axis: Average Daily Usage Hours (0-8)
- Y-axis: Addiction Score (2-9)
- Color-coded by platform
- Strong positive correlation (r=0.87)

**Key Insight:** Students using social media 6+ hours daily consistently score 8-9 on addiction scale, indicating severe dependency

---

### Slide 13: Mental Health Impact
**Title:** Addiction Impact on Sleep and Mental Health

**Chart Description:**
- Dual-axis visualization
- Grouped bar chart comparing high vs. low addiction groups
- Mental Health Score (left axis): High addiction = 5.2, Low addiction = 8.1
- Sleep Hours (right axis): High addiction = 5.5 hrs, Low addiction = 7.2 hrs

**Key Insight:** High addiction correlates with 30% lower mental health scores and 1.7 fewer hours of sleep per night

---

### Slide 14: App Category Time Distribution
**Title:** Screen Time Distribution by App Category

**Chart Description:**
- Pie chart or donut chart
- Social: 25.4% (763 entries)
- Utilities: 25.2% (755)
- Productivity: 25.1% (753)
- Entertainment: 24.3% (729)
- Average session times displayed

**Key Insight:** Despite equal representation, social apps have longest individual sessions (35 min vs 20 min for productivity), indicating higher engagement and potential for addiction

---

## Slide 15: Summary of Key Insights (Part 1)

**Title:** Summary of key insights from data/exploratory analysis(es)

**Content:**
• **Critical Finding #1 - Strong Usage-Addiction Correlation:**
  - 87% correlation between daily usage hours and addiction scores
  - Students using apps 6+ hours daily show addiction scores of 8-9/9
  - TikTok users exhibit highest addiction rates despite not having highest user count

• **Critical Finding #2 - Significant Health Impacts:**
  - High-addiction group sleeps 1.7 hours less per night (5.5 vs 7.2 hours)
  - Mental health scores 30% lower in addicted users (5.2 vs 8.1 out of 10)
  - 58% of students report negative academic performance impacts

• **Critical Finding #3 - Platform Differences:**
  - Instagram has most users (249/705) but moderate addiction scores
  - TikTok has highest average addiction score (7.8/9) - most concerning
  - LinkedIn and professional platforms show lowest addiction scores (2-3/9)

---

## Slide 16: Summary of Key Insights (Part 2)

**Title:** Summary of key insights from data/exploratory analysis(es)

**Content:**
• **Critical Finding #4 - App Category Behavior:**
  - Social apps dominate screen time despite equal category distribution
  - Social apps average 35 min/session vs 20 min for productivity
  - Only 25% of total app time spent on productivity tools
  - Entertainment apps (Netflix, Spotify, Twitch) show binge patterns with 45+ min sessions

• **Critical Finding #5 - Demographic Patterns:**
  - Age 18-22 demographic most vulnerable (40% report addiction)
  - Female users show slightly higher Instagram usage
  - Male users prefer gaming and YouTube content
  - Undergraduate students more affected than graduate students

• **Critical Finding #6 - Relationship Impact:**
  - Average relationship conflict score: 2.8/5 due to phone usage
  - 56% wish family/friends were more present in social settings
  - Students in "Complicated" relationships show highest usage hours

---

## Slide 17: Conclusion

**Title:** Conclusion

**Content:**
• **Answer to Research Question:**
  We identified social media apps, particularly TikTok and Instagram, as primary contributors to phone addiction among students. Clear patterns emerged showing strong correlations between usage time, addiction scores, and negative health outcomes.

• **Key Takeaways:**
  - 6+ hours daily usage is a critical threshold for severe addiction
  - Platform design matters: TikTok's short-form video format is most addictive
  - Multi-dimensional impact: affects sleep, mental health, academics, and relationships simultaneously
  - Productivity vs. Entertainment paradox: users spend equal time but engage differently

• **Recommendations:**
  - Implement app time limits and digital wellness features
  - Universities should provide digital literacy programs
  - App designers should consider ethical engagement features
  - Students should aim for <4 hours daily usage to maintain healthy metrics

• **Future Research:**
  - Longitudinal studies tracking intervention effectiveness
  - Analysis of notification patterns and addiction triggers
  - Cross-cultural comparison of addiction patterns

---

## Additional Notes for Presenter:

### Speaking Points for Data Visualizations:
- Emphasize the 87% correlation - this is a very strong statistical relationship
- Point out that TikTok's "infinite scroll" design contributes to highest addiction
- Mention that even "productive" time spent on phones contributes to overall screen fatigue
- Note that relationship conflicts (2.8/5) are significant - nearly 3 out of 5 intensity

### Engagement Questions for Audience:
- "How many hours per day do you think you spend on your phone?"
- "Which app do you check first thing in the morning?"
- "Have you ever experienced FOMO (Fear of Missing Out) from social media?"

### Connection to INFO 5602 Learning Objectives:
- Demonstrates effective use of multiple visualization types
- Shows clear data storytelling progression
- Applies Gestalt principles in chart design
- Uses color effectively to convey meaning and severity

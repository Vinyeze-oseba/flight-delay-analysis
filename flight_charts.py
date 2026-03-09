import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

# Load data
df = pd.read_csv(r'C:\Users\User\Desktop\data_analysis\flights_raw.csv')

# Clean data
df = df[df['flight_id'].notna()]
df['distance'] = df['distance'].abs()
df.loc[df['departure_delay'] > 500, 'departure_delay'] = None
df['airline_name'] = df['airline_name'].str.strip().str.title()

# Style
plt.style.use('dark_background')
colors = ['#00c8ff','#ff4d6d','#00ff9d','#ffb700','#a855f7','#ff6b35','#06d6a0','#ffd166']

# ── Chart 1: Airline Delay Rate ──
airline_stats = df[df['departure_delay'].notna()].groupby('airline_name').apply(
    lambda x: pd.Series({
        'delay_rate': (x['departure_delay'] > 15).sum() / len(x) * 100,
        'total': len(x)
    })
).reset_index().sort_values('delay_rate', ascending=True)

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#050a18')
ax.set_facecolor('#0d1526')
bars = ax.barh(airline_stats['airline_name'], airline_stats['delay_rate'],
               color=['#00ff9d' if v < 15 else '#ff4d6d' if v > 40 else '#00c8ff' 
                      for v in airline_stats['delay_rate']], height=0.6)
ax.set_xlabel('Delay Rate (%)', color='#8899bb', fontsize=11)
ax.set_title('Airline Delay Rate — 2023 US Flights', color='white', fontsize=16, fontweight='bold', pad=20)
ax.tick_params(colors='#8899bb')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#1a2540')
ax.spines['bottom'].set_color('#1a2540')
for bar, val in zip(bars, airline_stats['delay_rate']):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{val:.1f}%', va='center', color='white', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig(r'C:\Users\User\Desktop\data_analysis\chart1_airline_delays.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 1 done!")

# ── Chart 2: Monthly Delay Trend ──
month_names = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',
               7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
monthly = df[df['departure_delay'].notna()].groupby('month')['departure_delay'].mean().reset_index()
monthly['month_name'] = monthly['month'].map(month_names)

fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('#050a18')
ax.set_facecolor('#0d1526')
bar_colors = ['#ff4d6d' if v >= 15 else '#00ff9d' if v <= 4 else '#00c8ff' for v in monthly['departure_delay']]
ax.bar(monthly['month_name'], monthly['departure_delay'], color=bar_colors, alpha=0.8, width=0.6)
ax.plot(monthly['month_name'], monthly['departure_delay'], color='#a855f7', linewidth=2.5,
        marker='o', markersize=6, markerfacecolor='#a855f7')
ax.set_ylabel('Avg Delay (minutes)', color='#8899bb', fontsize=11)
ax.set_title('Monthly Delay Trends — Peak in June, Best in September', color='white', fontsize=16, fontweight='bold', pad=20)
ax.tick_params(colors='#8899bb')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#1a2540')
ax.spines['bottom'].set_color('#1a2540')
ax.axhline(y=15, color='#ff4d6d', linestyle='--', alpha=0.4, linewidth=1)
ax.text(11.4, 15.5, 'Delay threshold', color='#ff4d6d', fontsize=9)
plt.tight_layout()
plt.savefig(r'C:\Users\User\Desktop\data_analysis\chart2_monthly_delays.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 2 done!")

# ── Chart 3: On Time Performance ──
ontime = df['on_time'].fillna('Unknown').value_counts()
fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor('#050a18')
ax.set_facecolor('#050a18')
wedge_colors = ['#00ff9d','#ff4d6d','#ffb700','#4a5980']
wedges, texts, autotexts = ax.pie(ontime.values, labels=ontime.index,
                                   autopct='%1.1f%%', colors=wedge_colors,
                                   startangle=90, pctdistance=0.75,
                                   wedgeprops=dict(width=0.6, edgecolor='#050a18', linewidth=3))
for text in texts: text.set_color('#8899bb')
for autotext in autotexts: autotext.set_color('white'); autotext.set_fontweight('bold')
ax.set_title('On Time Performance — 59.5% Flights On Time', color='white', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig(r'C:\Users\User\Desktop\data_analysis\chart3_ontime.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 3 done!")

# ── Chart 4: Top Delayed Routes ──
route_stats = df[df['departure_delay'].notna()].groupby(['origin','destination'])['departure_delay'].mean().reset_index()
route_stats['route'] = route_stats['origin'] + ' → ' + route_stats['destination']
route_stats = route_stats.sort_values('departure_delay', ascending=False).head(8)

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#050a18')
ax.set_facecolor('#0d1526')
bar_colors2 = ['#ff4d6d','#ff6b50','#ff8c42','#ffb700','#00c8ff','#00c8ff','#00c8ff','#00c8ff']
bars = ax.barh(route_stats['route'], route_stats['departure_delay'], color=bar_colors2, height=0.6)
ax.set_xlabel('Avg Departure Delay (minutes)', color='#8899bb', fontsize=11)
ax.set_title('Top 8 Most Delayed Routes — LAS→LAX Worst at 20.7 mins', color='white', fontsize=14, fontweight='bold', pad=20)
ax.tick_params(colors='#8899bb')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#1a2540')
ax.spines['bottom'].set_color('#1a2540')
for bar, val in zip(bars, route_stats['departure_delay']):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            f'{val:.1f}m', va='center', color='white', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig(r'C:\Users\User\Desktop\data_analysis\chart4_routes.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 4 done!")

print("\n✅ All 4 charts saved to your data_analysis folder!")
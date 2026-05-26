import time
import math
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# rng = np.random.default_rng(seed=42)
# print(rng.random(3))

#Принцип работы randn
class NormalDistribution:
    def gen_pseudorand_nums(self, x: int = None, count: int = 2, modulus: int = 10**10, multiplier: int = 1103515245, increment: int = 12345) -> list:
        if x is None:
            x = time.time_ns()

        seq = []
        for _ in range(count):
             res = (multiplier * x + increment) % modulus
             if res == 0:
                 res += increment
             x = res
             seq.append(res / modulus)
        return seq

    def box_muller_algorithm(self, x1: float = None, x2: float = None) -> float | None:
        if x1 <= 0 or x2 <= 0:
            return None
        part1 = math.sqrt(-2 * math.log(x1))
        part2 = math.cos(2 * math.pi * x2)
        return part1 * part2

gauss = NormalDistribution()
base_numbers = gauss.gen_pseudorand_nums(42)
u1 = base_numbers[0]
u2 = base_numbers[1]

normal_random_number = gauss.box_muller_algorithm(u1, u2)

print(f"Базовые числа: {base_numbers}")
print(f"Число по Гауссу: {normal_random_number}")


#---SCATTER---
np.random.seed(42)
x = np.random.randn(100)
y = np.random.randn(100)

sizes = np.random.randint(10, 100, 100)
df = pd.DataFrame({
    'x': x,
    'y': y,
    'category': np.random.choice(['A', 'B', 'C'], 100),
    'size': sizes
})
fig = px.scatter(
    df,
    x='x',
    y='y',
    color='category',
    size='size',
    symbol='category',
    hover_data={
        'x': '0.2f',
        'y': '0.2f',
        'category': True,
        'size': True
    },
    title="Plotly Scatter Plot - Express",
    labels={'x': 'x axis', 'y': 'y axis'}
)

fig.update_traces(
    marker=dict(
        opacity=0.7,
        line=dict(width=1, color='white')
    )
)

fig.update_layout(
    width=1000,
    height=600,
    hovermode='closest'
)

fig.show()


#---LINE---
dates = pd.date_range('2026-01-01', periods=100)

df = pd.DataFrame({
    'date': dates,
    'AMD': np.cumsum(np.random.randint(-10, 15, 100)),
    'NVIDIA': np.cumsum(np.random.randint(-10, 15, 100)),
    'INTEL': np.cumsum(np.random.randint(-10, 15, 100))
})

fig = px.line(
    df,
    x='date',
    y=['AMD', 'NVIDIA', 'INTEL'],
    title="Plotly Line Plot - Express",
    labels={'value': 'Value', 'date': 'Date'},
    markers=True
)

fig.update_layout(
    xaxis=dict(
        dtick=864000000,
        tickformat="%d %A %m %Y",
        tickangle=-45
    ),
    width=1920,
    height=1080,
    hovermode='x unified'
)

fig.show()

#---BAR---
df = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E', 'A', 'A'],
    'value': [15, 46, 64, 43, 23, 17, 27]
})
fig = px.bar(
    df,
    x='category',
    y='value',
    color='category',
    labels={'value': 'Value', 'category': 'Category'},
    title='Plotly Express Bar - Plot'
)

fig.update_yaxes(dtick=5)

fig.update_traces(
    marker_color='steelblue',
    marker_line=dict(color='black', width=1.5),
    texttemplate='%{y} единиц(а/ы)',
    textposition='inside',
    textfont=dict(size=12, color='black')
)

fig.update_layout(
    hovermode='closest',
    width=1200,
    height=900,
)

fig.show()


#---HIST---
data = np.random.normal(100, 10, 500)
df = pd.DataFrame({'values': data})
fig = px.histogram(
    df,
    x='values',
    nbins=30,
    title='Plotly Histogram Chart - Express',
    labels={'value': 'Value'},
    histnorm='density'
)

fig.update_traces(
    marker_line=dict(color='steelblue', width=0.5),
    texttemplate='%{y}',
    textposition='outside',
    textfont=dict(size=9, color='black')
)

fig.update_layout(
    bargap=0.2,
    yaxis_title='Frequency',
    width=1200,
    height=900,
    hovermode='closest',
)

fig.show()


#---PIE---
category = ['A', 'B', 'C', 'D', 'E']
values = [25, 10, 40, 50, 30]
df = pd.DataFrame({
    'category': category,
    'values': values
})

fig = px.pie(
    df,
    names='category',
    values='values',
    color='category',
    hole=0.6,
    title="Plotly Pie Chart - Express"
)

fig.update_traces(
    textposition='outside',
    textinfo='percent+label'
)

fig.update_layout(
    width=1100,
    height=800,
)

fig.show()


#---Box Plot---
np.random.seed(42)
a = np.random.normal(100, 10, 50) #(mu, sigma, size)
b = np.random.normal(120, 15, 50) #(mu, sigma, size)
c = np.random.normal(140, 12, 50) #(mu, sigma, size)

print(np.concatenate([a, b, c]))

df = pd.DataFrame({
    'value': np.concatenate([a, b, c]),
    'group': ['A'] * 50 + ['B'] * 50 + ['C'] * 50
})

fig = px.box(
    df,
    x='group',
    y='value',
    title="Plotly Boxplot Chart - Express",
    labels={'group': 'Group', 'value': 'Value'}
)

fig.update_traces(marker=dict(size=10, opacity=1, color='steelblue'))

fig.update_layout(
    width=1000,
    height=800,
    hovermode='closest'
)

fig.show()


#---Violin Plot---
a = np.random.normal(100, 15, 50)
b = np.random.normal(120, 15, 50)
c = np.random.normal(150, 20, 50)

df = pd.DataFrame({
    'group': ['A'] * 50 + ['B'] * 50 + ['C'] * 50,
    'value': np.concatenate([a, b, c])
})

fig = px.violin(
    df,
    x='group',
    y='value',
    labels={'group': 'Group', 'value': 'Value'},
    box=False,
    points=False,
    title="Plotly Violin Chart - Express"
)

fig.update_layout(
    width=1200,
    height=800,
    hovermode='closest'
)
fig.show()


#---HEATMAP---
df = px.data.tips()
corr = df.select_dtypes(include=['number']).corr()
fig = px.imshow(
    corr,
    text_auto=True,
    aspect='equal',
    color_continuous_scale='RdBu_r',
    zmin=-1, zmax=1,
    labels=dict(
        color='Корреляция',
        x='Признаки x',
        y='Признаки y'
    ),
    title="Plotly HeatMap Chart - Express"
)
fig.update_traces(texttemplate='%{z:.3f}')
fig.update_layout(
    coloraxis_colorbar=dict(
        title="Красное(1) - многое корреляции. Синее(0) - мало корреляции",
        ticks='inside',
        tickvals=[-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1],
        ticktext=["-1", "-0.75", "-0.5", "-0.25", "0", "+0.25", "+0.5", "+0.75", "+1"],
        title_font=dict(size=15, color='steelblue'),
        tickfont=dict(size=10)
    ),
    width=1600,
    height=1200,
    hovermode='closest'
)
fig.show()
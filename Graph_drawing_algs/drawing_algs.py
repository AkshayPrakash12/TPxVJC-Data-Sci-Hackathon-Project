
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tracemalloc # running memory profiler (after hackathon project)
from datetime import datetime #exec time profiler (after hackathon project)

def app():
    df = pd.read_csv('../Datasets/spotify-2023.csv', encoding='latin')
    plt.scatter(df['artist_count'], df['in_spotify_charts'])
    plt.title('scatterplot of artist count vs spotify charts')
    plt.xlabel('artist count')
    plt.ylabel('spotify charts')
    plt.show()
    art1 = 0
    charts1 = []
    charts2 = []
    charts3 = []
    charts4 = []
    charts5 = []
    charts6 = []
    charts7 = []
    charts8 = []
    ite = 0
    chartm1 = 0
    for i in df['artist_count']:
        if i == 1:
            charts1.append(df['in_spotify_charts'][ite])
            art1 += 0
            ite += 1
        elif i == 2:
            charts2.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 3:
            charts3.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 4:
            charts4.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 5:
            charts5.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 6:
            charts6.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 7:
            charts7.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 8:
            charts8.append(df['in_spotify_charts'][ite])
            ite += 1
        else:
            ite += 1
    chartm1 = sorted(charts1)
    chartm1 = list(filter(lambda x: x != 0, chartm1))
    n = len(chartm1)
    if n % 2 == 0:
        median = (chartm1[n // 2 - 1] + chartm1[n // 2]) / 2
    else:
        median = chartm1[n // 2]
    print("chart median of single artist:", median)
    chartm2 = sorted(charts2)
    chartm2 = list(filter(lambda x: x != 0, chartm2))
    n2 = len(chartm2)
    if n2 % 2 == 0:
        median2 = (chartm2[n2 // 2 - 1] + chartm2[n2 // 2]) / 2
    else:
        median2 = chartm2[n2 // 2]
    print("chart median of 2 artists:", median2)
    chartm3 = sorted(charts3)
    chartm3 = list(filter(lambda x: x != 0, chartm3))
    n3 = len(chartm3)
    if n3 % 2 == 0:
        median3 = (chartm3[n3 // 2 - 1] + chartm3[n3 // 2]) / 2
    else:
        median3 = chartm3[n3 // 2]
    print("chart median of 3 artists:", median3)
    chartm4 = sorted(charts4)
    chartm4 = list(filter(lambda x: x != 0, chartm4))
    n4 = len(chartm4)
    if n4 % 2 == 0:
        median4 = (chartm4[n4 // 2 - 1] + chartm4[n4 // 2]) / 2
    else:
        median4 = chartm4[n4 // 2]
    print("chart median of 4 artists:", median4)
    chartm5 = sorted(charts5)
    chartm5 = list(filter(lambda x: x != 0, chartm5))
    n5 = len(chartm5)
    if n5 % 2 == 0:
        median5 = (chartm5[n5 // 2 - 1] + chartm5[n5 // 2]) / 2
    else:
        median5 = chartm5[n5 // 2]
    print("chart median of 5 artists:", median5)
    chartm6 = sorted(charts6)
    chartm6 = list(filter(lambda x: x != 0, chartm6))
    n4 = len(chartm6)
    if n4 % 2 == 0:
        median6 = (chartm6[n4 // 2 - 1] + chartm6[n4 // 2]) / 2
    else:
        median6 = chartm6[n4 // 2]
    print("chart median of 6 artists:", median6)
    chartm7 = sorted(charts7)
    chartm7 = list(filter(lambda x: x != 0, chartm7))
    n7 = len(chartm7)
    if n7 % 2 == 0:
        median7 = (chartm7[n7 // 2 - 1] + chartm7[n7 // 2]) / 2
    else:
        median7 = chartm7[n7 // 2]
    print("chart median of 7 artists:", median7)
    chartm8 = sorted(charts8)
    chartm8 = list(filter(lambda x: x != 0, chartm8))
    n8 = len(chartm8)
    if n8 % 2 == 0:
        median8 = (chartm8[n8 // 2 - 1] + chartm8[n8 // 2]) / 2
    else:
        median8 = chartm8[n8 // 2]
    print("chart median of 8 artists:", median8)
    if median2 > median and median2 > median3 and median2 > median4 and median2 > median5 and median2 > median6 and median2 > median7 and median2 > median8:
        print("2 artist is best option to have the best presences in spotify playlist")
    elif median3 > median2 and median3 > median and median3 > median4 and median3 > median5 and median3 > median6 and median3 > median7 and median3 > median8:
        print("3 artist is best option to have the best presences in spotify playlist")
    elif median4 > median2 and median4 > median3 and median4 > median and median4 > median5 and median4 > median6 and median4 > median7 and median4 > median8:
        print("4 artist is best option to have the best presences in spotify playlist")
    elif median5 > median2 and median5 > median3 and median5 > median4 and median5 > median and median5 > median6 and median5 > median7 and median5 > median8:
        print("5 artist is best option to have the best presences in spotify playlist")
    elif median6 > median2 and median6 > median3 and median6 > median4 and median6 > median5 and median6 > median and median6 > median7 and median6 > median8:
        print("6 artist is best option to have the best presences in spotify playlist")
    elif median7 > median2 and median7 > median3 and median7 > median4 and median7 > median5 and median7 > median6 and median7 > median and median7 > median8:
        print("7 artist is best option to have the best presences in spotify playlist")
    elif median > median2 and median > median3 and median > median4 and median > median5 and median > median6 and median > median7 and median > median8:
        print("1 artist is best option to have the best presences in spotify playlist")
    else:
        print("8 artist is best option to have the best presences in spotify playlist")

    plt.scatter(df['released_month'], df['in_spotify_charts'])
    plt.title('scatterplot of released month vs spotify charts')
    plt.xlabel('released month')
    plt.ylabel('spotify charts')
    plt.show()
    chartsm1 = []
    chartsm2 = []
    chartsm3 = []
    chartsm4 = []
    chartsm5 = []
    chartsm6 = []
    chartsm7 = []
    chartsm8 = []
    chartsm9 = []
    chartsm10 = []
    chartsm11 = []
    chartsm12 = []
    ite = 0
    chartm1 = 0
    for i in df['released_month']:
        if i == 1:
            chartsm1.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 2:
            chartsm2.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 3:
            chartsm3.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 4:
            chartsm4.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 5:
            chartsm5.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 6:
            chartsm6.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 7:
            chartsm7.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 8:
            chartsm8.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 9:
            chartsm9.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 10:
            chartsm10.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 11:
            chartsm11.append(df['in_spotify_charts'][ite])
            ite += 1
        elif i == 12:
            chartsm12.append(df['in_spotify_charts'][ite])
            ite += 1
        else:
            ite += 1
    print(ite)
    print(chartsm8)
    chartmm1 = sorted(chartsm1)
    print(chartmm1)
    chartmm1 = list(filter(lambda x: x != 0, chartmm1))
    print(chartmm1)
    nm = len(chartmm1)
    if nm % 2 == 0:
        medianm = (chartmm1[nm // 2 - 1] + chartmm1[nm // 2]) / 2
    else:
        medianm = chartmm1[nm // 2]
    print("median:", medianm)
    chartmm2 = sorted(chartsm2)
    print(chartmm2)
    chartmm2 = list(filter(lambda x: x != 0, chartmm2))
    print(chartmm2)
    nm2 = len(chartmm2)
    if nm2 % 2 == 0:
        medianm2 = (chartmm2[nm2 // 2 - 1] + chartmm2[nm2 // 2]) / 2
    else:
        medianm2 = chartmm2[nm2 // 2]
    print("median 2:", medianm2)
    chartmm3 = sorted(chartsm3)
    print(chartmm3)
    chartmm3 = list(filter(lambda x: x != 0, chartmm3))
    print(chartm1)
    nm3 = len(chartmm3)
    if nm3 % 2 == 0:
        medianm3 = (chartmm3[nm3 // 2 - 1] + chartmm3[nm3 // 2]) / 2
    else:
        medianm3 = chartmm3[nm3 // 2]
    print("median3:", medianm3)
    chartmm4 = sorted(chartsm4)
    print(chartmm4)
    chartmm4 = list(filter(lambda x: x != 0, chartmm4))
    print(chartmm4)
    nm4 = len(chartmm4)
    if nm4 % 2 == 0:
        medianm4 = (chartmm4[nm4 // 2 - 1] + chartmm4[nm4 // 2]) / 2
    else:
        medianm4 = chartmm4[nm4 // 2]
    print("median4:", medianm4)
    chartmm5 = sorted(chartsm5)
    print(chartmm5)
    chartmm5 = list(filter(lambda x: x != 0, chartmm5))
    print(chartmm5)
    nm5 = len(chartmm5)
    if nm5 % 2 == 0:
        medianm5 = (chartmm5[nm5 // 2 - 1] + chartmm5[nm5 // 2]) / 2
    else:
        medianm5 = chartmm5[nm5 // 2]
    print("median 5:", medianm5)
    chartmm6 = sorted(chartsm6)
    print(chartmm6)
    chartmm6 = list(filter(lambda x: x != 0, chartmm6))
    print(chartmm6)
    nm6 = len(chartmm6)
    if nm6 % 2 == 0:
        medianm6 = (chartmm6[nm6 // 2 - 1] + chartmm6[nm6 // 2]) / 2
    else:
        medianm6 = chartmm6[nm6 // 2]
    print("median 6:", medianm6)
    chartmm7 = sorted(chartsm7)
    print(chartmm7)
    chartmm7 = list(filter(lambda x: x != 0, chartmm7))
    print(chartmm7)
    nm7 = len(chartmm7)
    if nm7 % 2 == 0:
        medianm7 = (chartmm7[nm7 // 2 - 1] + chartmm7[nm7 // 2]) / 2
    else:
        medianm7 = chartmm3[nm7 // 2]
    print("median7:", medianm7)
    chartmm8 = sorted(chartsm8)
    print(chartmm8)
    chartmm8 = list(filter(lambda x: x != 0, chartmm8))
    print(chartmm8)
    nm8 = len(chartmm8)
    if nm8 % 2 == 0:
        medianm8 = (chartmm8[nm8 // 2 - 1] + chartmm8[nm8 // 2]) / 2
    else:
        medianm8 = chartmm8[nm8 // 2]
    print("median8:", medianm8)
    chartmm9 = sorted(chartsm9)
    print(chartmm9)
    chartmm9 = list(filter(lambda x: x != 0, chartmm9))
    print(chartmm9)
    nm9 = len(chartmm9)
    if nm9 % 2 == 0:
        medianm9 = (chartmm9[nm9 // 2 - 1] + chartmm9[nm9 // 2]) / 2
    else:
        medianm9 = chartmm9[nm9 // 2]
    print("median:", medianm9)
    chartmm10 = sorted(chartsm10)
    print(chartmm10)
    chartmm10 = list(filter(lambda x: x != 0, chartmm10))
    print(chartmm10)
    nm10 = len(chartmm10)
    if nm10 % 2 == 0:
        medianm10 = (chartmm10[nm10 // 2 - 1] + chartmm10[nm10 // 2]) / 2
    else:
        medianm10 = chartmm10[nm10 // 2]
    print("median 10:", medianm10)
    chartmm11 = sorted(chartsm11)
    print(chartmm11)
    chartmm11 = list(filter(lambda x: x != 0, chartmm11))
    nm11 = len(chartmm3)
    if nm11 % 2 == 0:
        medianm11 = (chartmm11[nm11 // 2 - 1] + chartmm11[nm11 // 2]) / 2
    else:
        medianm11 = chartmm11[nm11 // 2]
    print("median11:", medianm11)
    chartmm12 = sorted(chartsm12)
    print(chartmm12)
    chartmm12 = list(filter(lambda x: x != 0, chartmm12))
    print(chartmm12)
    nm12 = len(chartmm12)
    if nm12 % 2 == 0:
        medianm12 = (chartmm12[nm12 // 2 - 1] + chartmm12[nm12 // 2]) / 2
    else:
        medianm12 = chartmm12[nm12 // 2]
    print("median12:", medianm12)

    cha = df['in_spotify_charts']
    df['key'] = df['key'].fillna('C')
    print(df['key'][12])
    charts1k = []
    charts2k = []
    charts3k = []
    charts4k = []
    charts5k = []
    charts6k = []
    charts7k = []
    charts8k = []
    charts9k = []
    charts10k = []
    charts11k = []
    charts12k = []
    charts13k = []
    charts14k = []
    itk = 0
    dfe = []
    alp = df['key']
    for i in alp:
        if i == 'A':
            charts1k.append(cha[itk])
            itk += 1
        elif i == 'A#':
            charts2k.append(cha[itk])
            itk += 1
        elif i == 'B':
            charts3k.append(cha[itk])
            itk += 1
        elif i == 'C':
            charts4k.append(cha[itk])
            itk += 1
        elif i == 'C#':
            charts6k.append(cha[itk])
            itk += 1
        elif i == 'D':
            charts7k.append(cha[itk])
            itk += 1
        elif i == 'D#':
            charts8k.append(cha[itk])
            itk += 1
        elif i == 'E':
            charts10k.append(cha[itk])
            itk += 1
        elif i == 'F':
            charts11k.append(cha[itk])
            itk += 1
        elif i == 'F#':
            charts12k.append(cha[itk])
            itk += 1
        elif i == 'G':
            charts13k.append(cha[itk])
            itk += 1
        elif i == 'G#':
            charts14k.append(cha[itk])
            itk += 1
        else:
            None
    print(itk)
    print(charts1k)
    chartkm1 = sorted(charts1k)
    chartkm1 = list(filter(lambda x: x != 0, chartkm1))
    print(chartkm1)
    nk = len(chartkm1)
    if nk % 2 == 0:
        mediank = (chartkm1[nk // 2 - 1] + chartkm1[nk // 2]) / 2
    else:
        mediank = chartkm1[nk // 2]
    print("median:", mediank)
    chartkm2 = sorted(charts2k)
    chartkm2 = list(filter(lambda x: x != 0, chartkm2))
    print(chartkm2)
    nk2 = len(chartkm2)
    if nk2 % 2 == 0:
        mediank2 = (chartkm2[nk2 // 2 - 1] + chartkm2[nk2 // 2]) / 2
    else:
        mediank2 = chartkm2[nk2 // 2]
    print("median 2:", mediank2)
    chartkm3 = sorted(charts3k)
    chartkm3 = list(filter(lambda x: x != 0, chartkm3))
    print(chartkm3)
    nk3 = len(chartkm3)
    if nk3 % 2 == 0:
        mediank3 = (chartkm3[nk3 // 2 - 1] + chartkm3[nk3 // 2]) / 2
    else:
        mediank3 = chartkm3[nk3 // 2]
    print("median3:", mediank3)
    chartkm4 = sorted(charts4k)
    chartkm4 = list(filter(lambda x: x != 0, chartkm4))
    print(chartkm4)
    nk4 = len(chartkm4)
    if nk4 % 2 == 0:
        mediank4 = (chartkm4[nk4 // 2 - 1] + chartkm4[nk4 // 2]) / 2
    else:
        mediank4 = chartkm4[nk4 // 2]
    print("median4:", mediank4)
    chartkm6 = sorted(charts6k)
    chartkm6 = list(filter(lambda x: x != 0, chartkm6))
    print(chartkm6)
    nk6 = len(chartkm6)
    if nk6 % 2 == 0:
        mediank6 = (chartkm6[nk6 // 2 - 1] + chartkm6[nk6 // 2]) / 2
    else:
        mediank6 = chartkm6[nk6 // 2]
    print("median6:", mediank6)
    chartkm7 = sorted(charts7k)
    chartkm7 = list(filter(lambda x: x != 0, chartkm7))
    print(chartkm7)
    nk7 = len(chartkm7)
    if nk7 % 2 == 0:
        mediank7 = (chartkm7[nk7 // 2 - 1] + chartkm7[nk7 // 2]) / 2
    else:
        mediank7 = chartkm7[nk7 // 2]
    print("median7:", mediank7)
    chartkm8 = sorted(charts8k)
    chartkm8 = list(filter(lambda x: x != 0, chartkm8))
    print(chartkm8)
    nk8 = len(chartkm8)
    if nk8 % 2 == 0:
        mediank8 = (chartkm8[nk8 // 2 - 1] + chartkm8[nk8 // 2]) / 2
    else:
        mediank8 = chartkm8[nk8 // 2]
    print("median8:", mediank8)
    chartkm9 = sorted(charts10k)
    chartkm9 = list(filter(lambda x: x != 0, chartkm9))
    print(chartkm9)
    nk9 = len(chartkm9)
    if nk9 % 2 == 0:
        mediank9 = (chartkm9[nk9 // 2 - 1] + chartkm9[nk9 // 2]) / 2
    else:
        mediank9 = chartkm9[nk9 // 2]
    print("median9:", mediank9)
    chartkm11 = sorted(charts11k)
    chartkm11 = list(filter(lambda x: x != 0, chartkm11))
    print(chartkm11)
    nk11 = len(chartkm11)
    if nk11 % 2 == 0:
        mediank11 = (chartkm11[nk11 // 2 - 1] + chartkm11[nk11 // 2]) / 2
    else:
        mediank11 = chartkm11[nk11 // 2]
    print("median11:", mediank11)
    chartkm12 = sorted(charts12k)
    chartkm12 = list(filter(lambda x: x != 0, chartkm12))
    print(chartkm12)
    nk12 = len(chartkm12)
    if nk12 % 2 == 0:
        mediank12 = (chartkm12[nk12 // 2 - 1] + chartkm12[nk12 // 2]) / 2
    else:
        mediank12 = chartkm12[nk12 // 2]
    print("median12:", mediank12)
    chartkm13 = sorted(charts13k)
    chartkm13 = list(filter(lambda x: x != 0, chartkm13))
    print(chartkm13)
    nk13 = len(chartkm13)
    if nk13 % 2 == 0:
        mediank13 = (chartkm13[nk4 // 2 - 1] + chartkm13[nk13 // 2]) / 2
    else:
        mediank13 = chartkm13[nk13 // 2]
    print("median13:", mediank13)
    chartkm14 = sorted(charts14k)
    chartkm14 = list(filter(lambda x: x != 0, chartkm14))
    print(chartkm14)
    nk14 = len(chartkm14)
    if nk14 % 2 == 0:
        mediank14 = (chartkm4[nk14 // 2 - 1] + chartkm14[nk14 // 2]) / 2
    else:
        mediank14 = chartkm14[nk14 // 2]
    print("median14:", mediank14)
    plt.scatter(df['key'], df['in_spotify_charts'])
    plt.title('scatterplot of key vs spotify charts')
    plt.xlabel('key')
    plt.ylabel('spotify charts')
    plt.show()
    df['in_shazam_charts'] = pd.to_numeric(df['in_shazam_charts'], errors='coerce')
    df['in_shazam_charts'].fillna(0)
    shazam_med = df['in_shazam_charts'].median(numeric_only=True)
    df['in_shazam_charts'] = df['in_shazam_charts'].replace(0, shazam_med)
    print(df['in_shazam_charts'][14])



app()

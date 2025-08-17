import numpy as np
import matplotlib.pyplot as plt
import colorsys

def complex_color_plot(T_func, k=5, d=0.1):
    """
    복소함수 T_func를 색상 그래프로 표시
    k: 복소평면 범위 [-k, k]
    d: 단위 눈금 (격자 간격)
    """
    # 복소평면 범위 설정
    x = np.arange(-k, k + d, d)
    y = np.arange(-k, k + d, d)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # 함수 계산
    T = T_func(Z)

    # HSV 계산
    hue = np.angle(T) / (2*np.pi) + 0.5          # 0~1 범위
    brightness = 1 - np.exp(-np.abs(T)/5)        # 크기에 따른 명도
    saturation = np.ones_like(hue)

    # HSV → RGB 변환
    HSV_to_RGB = np.vectorize(colorsys.hsv_to_rgb)
    R, G, B = HSV_to_RGB(hue, saturation, brightness)
    RGB = np.dstack((R, G, B))

    # 그래프 표시
    plt.figure(figsize=(8,8))
    plt.imshow(RGB, extent=[-k,k,-k,k], origin='lower')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.title('plot of T(x) = x(1 + e^{iπx}) + 2(1 - e^{iπx})(3x + 1)/4 = `(n%2)?3n+1):(n/2)`')
    plt.show()

# 예시: 주어진 함수
def T(Z):
    return Z * (1 + np.exp(1j * np.pi * Z)) + 2 * (1 - np.exp(1j * np.pi * Z)) * (3*Z + 1)/4

# 실행
complex_color_plot(T, k=10, d=0.01)
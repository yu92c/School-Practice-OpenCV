# inverse mapping 強調的是「座標轉換的反函數」。
# 幾何轉換函數的反函數。
# T(x, y) → (x', y') --> T⁻¹(x', y') → (x, y)

# | 項目       | inverse mapping 程式（手寫）    | OpenCV 旋轉（內建）         |
#| -----------| ----------------------------- |-------------------------- |
#| 旋轉座標原理 | 一樣，都用的是旋轉矩陣            | 同樣的矩陣                  |
#| 使用方式    | 手動計算、自己轉座標、自己取值      | 呼叫現成函數、自動完成        |
#| 本質上是    | 自己寫的 warpAffine 過程         |  OpenCV 包裝好的 warpAffine |
#| 插值        | 最近鄰（你寫的）                 | 預設是 bilinear（平滑）      |

# 你手寫的 inverse mapping，其實就是 OpenCV warpAffine() 的底層邏輯，
# 只是你用手動方式實作出來，沒有插值、沒有加速，但概念完全相同！

# 「單純的座標轉換反函數（inverse mapping）範例」:
import math

def inverse_rotation(x_prime, y_prime, angle_deg):
    angle_rad = math.radians(angle_deg)

    # 反轉旋轉公式（注意正負號）
    x =  math.cos(angle_rad) * x_prime + math.sin(angle_rad) * y_prime
    y = -math.sin(angle_rad) * x_prime + math.cos(angle_rad) * y_prime

    return x, y

# 範例：假設畫面上的某點是旋轉後的 (30, 50)，想知道它來自原圖哪個點
x_prime, y_prime = 30, 50
angle = 45

x, y = inverse_rotation(x_prime, y_prime, angle)

print(f"Rotated point ({x_prime}, {y_prime}) was originally at ({x:.2f}, {y:.2f})")

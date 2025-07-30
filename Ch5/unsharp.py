import numpy as np
import cv2

# Unsharp Masking 是透過「模糊→產生細節遮罩→加回強化」的邏輯讓圖像變得更銳利。
def unsharp_masking_color(f, k=1.0):
    # 轉為 float32 做運算避免溢位
    f_float = f.astype(np.float32)

    # 使用高斯模糊獲得平滑圖像
    f_avg = cv2.GaussianBlur(f_float, (15, 15), 0)
 
    # 計算細節（原圖 - 模糊圖），並依 k 倍強化
    g_mask = f_float - f_avg
    g = np.clip(f_float + k * g_mask, 0, 255)

    # 回傳 uint8 以供顯示
    return g.astype(np.uint8)

def main():
    img1 = cv2.imread('pic/statue.png', -1)  # 自動判斷是否為灰階/彩色
    if img1 is None:
        print("❌ 找不到圖片檔案，請確認路徑是否正確。")
        return

    img2 = unsharp_masking_color(img1, k=10.0)  # k 值控制細節強化程度

    cv2.imshow("Original Image", img1)
    cv2.imshow("Unsharp Masking Result", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()

'''
Unsharp Masking 原理（步驟):
平滑原圖
用高斯模糊（cv2.GaussianBlur）來產生一個模糊版本 f_avg。

取得細節（遮罩）
用原圖減去模糊圖 →
細節 = 原圖 - 模糊圖
這樣會留下高頻細節（邊緣、雜訊等）。

強化細節後加入回原圖
結果 = 原圖 + k × 細節
越高的 k 值（增強倍率）越銳利。

'''
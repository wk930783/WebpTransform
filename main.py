import subprocess
import tkinter as tk
from tkinter import filedialog
import os

def convert_to_webp(image_filenames):
    for image_filename in image_filenames:
        output_directory = "/".join(image_filename.split("/")[:-1])
        base_name = os.path.splitext(image_filename.split("/")[-1])[0]
        cmd = f'cwebp -q 75 "{image_filename}" -o "{output_directory}/{base_name}.webp"'
        subprocess.run(cmd, shell=True)

def select_images():
    image_filenames = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if image_filenames:
        convert_to_webp(image_filenames)
        result_label.config(text="轉換完成！")

# 創建視窗
root = tk.Tk()
root.title("多圖片轉換工具")

# 創建按鈕
convert_button = tk.Button(root, text="選擇圖片並轉換", command=select_images)
convert_button.pack(pady=20)

# 顯示轉換結果的標籤
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

# 啟動視窗迴圈
root.mainloop()

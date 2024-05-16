"""
////////////////////////////////////////////////////////////////////////////////
// Company: CQU
// Engineer: 王禹轩、宋纯豪、王财成、彭万
//
// Create Date: 
// Design Name: circular-function-calculator
// Module Name: TCGUI
// Target Device: N/A (Simulation)
// Tool versions: Python 3.x
// Description:                               
//              对第四组基于Matlab的circular-function-calculator的GUI实现
// Dependencies:                              
//              <Dependencies here>
// Revision: v1.0   
// <Revision here>
// Additional Comments:
// <Additional Comments here>
////////////////////////////////////////////////////////////////////////////////
"""
import matlab.engine
import tkinter as tk

# 启动 MATLAB 引擎
eng = matlab.engine.start_matlab()
# 调用MATLAB部分由宋纯豪同学实现
# 调用 MATLAB 函数 my_arcsin
def calculate_arcsin():
    try:
        in_val = float(input_entry.get())
        nth = int(nth_entry.get())
        result = eng.my_arcsin(in_val, nth)
        result_label.config(text="Result (arcsin): " + str(result))
    except ValueError:
        result_label.config(text="Invalid input")

# 调用 MATLAB 函数 my_cos
def calculate_cos():
    try:
        in_rad = float(rad_entry.get())
        nth = int(nth_cos_entry.get())
        result = eng.my_cos(in_rad, nth)
        result_cos_label.config(text="Result (cos): " + str(result))
    except ValueError:
        result_cos_label.config(text="Invalid input")

# 调用 MATLAB 函数 my_sin
def calculate_sin():
    try:
        in_rad = float(rad_sin_entry.get())
        nth = int(nth_sin_entry.get())
        result = eng.my_sin(in_rad, nth)
        result_sin_label.config(text="Result (sin): " + str(result))
    except ValueError:
        result_sin_label.config(text="Invalid input")

# 调用 MATLAB 函数 my_arctan
def calculate_arctan():
    try:
        in_val = float(val_arctan_entry.get())
        nth = int(nth_arctan_entry.get())
        result = eng.my_arctan(in_val, nth)
        result_arctan_label.config(text="Result (arctan): " + str(result))
    except ValueError:
        result_arctan_label.config(text="Invalid input")

# GUI界面部分由王禹轩 王财成 彭万同学实现

# 创建 GUI 界面（王禹轩）
root = tk.Tk()
root.title("Trigonometric Function Calculator")
# 计算 arcsin 的部分（王禹轩）
arcsin_frame = tk.Frame(root)
arcsin_frame.pack()

input_label = tk.Label(arcsin_frame, text="Enter input value for arcsin:")
input_label.pack(side=tk.LEFT)
input_entry = tk.Entry(arcsin_frame)
input_entry.pack(side=tk.LEFT)

nth_label = tk.Label(arcsin_frame, text="Enter number of terms:")
nth_label.pack(side=tk.LEFT)
nth_entry = tk.Entry(arcsin_frame)
nth_entry.pack(side=tk.LEFT)

calculate_button_arcsin = tk.Button(root, text="Calculate arcsin", command=calculate_arcsin)
calculate_button_arcsin.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# 计算 cos 的部分（王财成）
cos_frame = tk.Frame(root)
cos_frame.pack()

rad_label = tk.Label(cos_frame, text="Enter angle in radians for cos:")
rad_label.pack(side=tk.LEFT)
rad_entry = tk.Entry(cos_frame)
rad_entry.pack(side=tk.LEFT)

nth_cos_label = tk.Label(cos_frame, text="Enter number of terms:")
nth_cos_label.pack(side=tk.LEFT)
nth_cos_entry = tk.Entry(cos_frame)
nth_cos_entry.pack(side=tk.LEFT)

calculate_button_cos = tk.Button(root, text="Calculate cos", command=calculate_cos)
calculate_button_cos.pack()

result_cos_label = tk.Label(root, text="")
result_cos_label.pack()

# 计算 sin 的部分（王财成）

sin_frame = tk.Frame(root)
sin_frame.pack()

rad_sin_label = tk.Label(sin_frame, text="Enter angle in radians for sin:")
rad_sin_label.pack(side=tk.LEFT)
rad_sin_entry = tk.Entry(sin_frame)
rad_sin_entry.pack(side=tk.LEFT)

nth_sin_label = tk.Label(sin_frame, text="Enter number of terms:")
nth_sin_label.pack(side=tk.LEFT)
nth_sin_entry = tk.Entry(sin_frame)
nth_sin_entry.pack(side=tk.LEFT)

calculate_button_sin = tk.Button(root, text="Calculate sin", command=calculate_sin)
calculate_button_sin.pack()

result_sin_label = tk.Label(root, text="")
result_sin_label.pack()
# 计算 arctan 的部分（彭万）

# Create a frame containing widgets
arctan_frame = tk.Frame(root)
arctan_frame.pack()

# Label and entry for input value
val_arctan_label = tk.Label(arctan_frame, text="Enter input value for arctan:")
val_arctan_label.pack(side=tk.LEFT)
val_arctan_entry = tk.Entry(arctan_frame)
val_arctan_entry.pack(side=tk.LEFT)

# Label and entry for number of terms
nth_arctan_label = tk.Label(arctan_frame, text="Enter number of terms:")
nth_arctan_label.pack(side=tk.LEFT)
nth_arctan_entry = tk.Entry(arctan_frame)
nth_arctan_entry.pack(side=tk.LEFT)

# Calculate button
calculate_button_arctan = tk.Button(root, text="Calculate arctan", command=calculate_arctan)
calculate_button_arctan.pack()


# Result label
result_arctan_label = tk.Label(root, text="")
result_arctan_label.pack()

root.mainloop()

# 关闭 MATLAB 引擎
eng.quit()

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


# 计算 sin 的部分（王财成）


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

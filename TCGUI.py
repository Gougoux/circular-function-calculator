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
# 计算 arcsin 的部分（王禹轩）


# 计算 cos 的部分（王财成）


# 计算 sin 的部分（王财成）


# 计算 arctan 的部分（彭万）

# 关闭 MATLAB 引擎
eng.quit()

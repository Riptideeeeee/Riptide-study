import tkinter as tk
from tkinter import ttk, messagebox
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sympy as sp

class FunctionPlotter:
    def __init__(self, root):
        self.root = root
        self.root.title("高中函数绘图与计算器")
        self.root.geometry("1200x750")
        self.root.resizable(True, True)
        
        # 符号变量
        self.x = sp.Symbol('x')
        self.func_expr = None  # sympy表达式
        
        # 创建界面
        self.create_widgets()
        
        # 默认函数
        self.func_entry.insert(0, "x**2")
        self.plot_function()
    
    def create_widgets(self):
        """创建所有界面组件"""
        # 主框架
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 左侧控制面板
        left_frame = ttk.Frame(main_frame, width=350)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left_frame.pack_propagate(False)
        
        # 右侧绘图面板
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # ===== 左侧控制面板内容 =====
        # 标题
        title_label = ttk.Label(left_frame, text="🎯 函数计算器", font=('Arial', 16, 'bold'))
        title_label.pack(pady=(0, 15))
        
        # 函数输入
        func_frame = ttk.LabelFrame(left_frame, text="📐 函数表达式", padding=10)
        func_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(func_frame, text="f(x) =", font=('Arial', 12)).pack(anchor=tk.W)
        self.func_entry = ttk.Entry(func_frame, font=('Courier', 14))
        self.func_entry.pack(fill=tk.X, pady=(5, 10))
        
        # 常用函数快捷按钮
        quick_frame = ttk.Frame(func_frame)
        quick_frame.pack(fill=tk.X)
        funcs = [('x²', 'x**2'), ('x³', 'x**3'), ('√x', 'sqrt(x)'), ('sin(x)', 'sin(x)'),
                 ('cos(x)', 'cos(x)'), ('tan(x)', 'tan(x)'), ('ln(x)', 'log(x)'), ('eˣ', 'exp(x)')]
        for i, (label, expr) in enumerate(funcs):
            btn = ttk.Button(quick_frame, text=label, command=lambda e=expr: self.set_func(e))
            btn.grid(row=i//4, column=i%4, padx=2, pady=2, sticky='ew')
        quick_frame.grid_columnconfigure(0, weight=1)
        quick_frame.grid_columnconfigure(1, weight=1)
        quick_frame.grid_columnconfigure(2, weight=1)
        quick_frame.grid_columnconfigure(3, weight=1)
        
        # 绘图按钮
        plot_btn = ttk.Button(left_frame, text="🔄 绘制图像", command=self.plot_function)
        plot_btn.pack(fill=tk.X, pady=10)
        
        # 参数设置
        param_frame = ttk.LabelFrame(left_frame, text="⚙️ 参数设置", padding=10)
        param_frame.pack(fill=tk.X, pady=(0, 10))
        
        # x范围
        range_frame = ttk.Frame(param_frame)
        range_frame.pack(fill=tk.X, pady=5)
        ttk.Label(range_frame, text="x范围:").pack(side=tk.LEFT)
        self.xmin_entry = ttk.Entry(range_frame, width=8)
        self.xmin_entry.pack(side=tk.LEFT, padx=5)
        self.xmin_entry.insert(0, "-10")
        ttk.Label(range_frame, text="~").pack(side=tk.LEFT)
        self.xmax_entry = ttk.Entry(range_frame, width=8)
        self.xmax_entry.pack(side=tk.LEFT, padx=5)
        self.xmax_entry.insert(0, "10")
        
        # 计算功能
        calc_frame = ttk.LabelFrame(left_frame, text="🧮 计算功能", padding=10)
        calc_frame.pack(fill=tk.X, pady=(0, 10))
        
        # 函数值计算
        val_frame = ttk.Frame(calc_frame)
        val_frame.pack(fill=tk.X, pady=5)
        ttk.Label(val_frame, text="f(").pack(side=tk.LEFT)
        self.val_entry = ttk.Entry(val_frame, width=10)
        self.val_entry.pack(side=tk.LEFT, padx=5)
        ttk.Label(val_frame, text=") =").pack(side=tk.LEFT)
        self.val_result = ttk.Label(val_frame, text="", font=('Arial', 12, 'bold'))
        self.val_result.pack(side=tk.LEFT, padx=5)
        ttk.Button(val_frame, text="计算", command=self.calc_value).pack(side=tk.LEFT, padx=5)
        
        # 特殊点计算
        special_frame = ttk.Frame(calc_frame)
        special_frame.pack(fill=tk.X, pady=5)
        ttk.Button(special_frame, text="🎯 求零点", command=self.find_zeros).pack(side=tk.LEFT, padx=2)
        ttk.Button(special_frame, text="📈 求极值", command=self.find_extrema).pack(side=tk.LEFT, padx=2)
        ttk.Button(special_frame, text="📊 求交点", command=self.find_intersection).pack(side=tk.LEFT, padx=2)
        
        # 结果显示
        result_frame = ttk.LabelFrame(left_frame, text="📋 结果", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True)
        
        self.result_text = tk.Text(result_frame, height=10, wrap=tk.WORD, font=('Courier', 10))
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(self.result_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)
        
        # ===== 右侧绘图面板 =====
        # matplotlib 图形
        self.fig = Figure(figsize=(7, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # 底部操作栏
        bottom_frame = ttk.Frame(right_frame)
        bottom_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(bottom_frame, text="💾 保存图像", command=self.save_plot).pack(side=tk.LEFT, padx=5)
        ttk.Button(bottom_frame, text="🔄 重置视图", command=self.reset_view).pack(side=tk.LEFT, padx=5)
        ttk.Button(bottom_frame, text="📐 显示网格", command=self.toggle_grid).pack(side=tk.LEFT, padx=5)
        
        self.grid_var = tk.BooleanVar(value=True)
        
    def set_func(self, expr):
        """设置函数表达式"""
        self.func_entry.delete(0, tk.END)
        self.func_entry.insert(0, expr)
        self.plot_function()
    
    def get_function(self):
        """获取并解析函数表达式"""
        expr_str = self.func_entry.get().strip()
        if not expr_str:
            messagebox.showerror("错误", "请输入函数表达式")
            return None
        
        try:
            # 替换数学函数为sympy格式
            expr_str = expr_str.replace('^', '**')
            expr_str = expr_str.replace('sqrt', 'sp.sqrt')
            expr_str = expr_str.replace('sin', 'sp.sin')
            expr_str = expr_str.replace('cos', 'sp.cos')
            expr_str = expr_str.replace('tan', 'sp.tan')
            expr_str = expr_str.replace('log', 'sp.log')
            expr_str = expr_str.replace('exp', 'sp.exp')
            expr_str = expr_str.replace('pi', 'sp.pi')
            expr_str = expr_str.replace('e', 'sp.E')
            
            # 安全地解析
            self.func_expr = sp.sympify(expr_str)
            return self.func_expr
        except Exception as e:
            messagebox.showerror("错误", f"函数解析失败: {str(e)}")
            return None
    
    def plot_function(self):
        """绘制函数图像"""
        func = self.get_function()
        if func is None:
            return
        
        try:
            # 获取x范围
            xmin = float(self.xmin_entry.get())
            xmax = float(self.xmax_entry.get())
            
            if xmin >= xmax:
                messagebox.showerror("错误", "x范围无效: 最小值必须小于最大值")
                return
            
            # 生成x值
            x_vals = np.linspace(xmin, xmax, 1000)
            
            # 计算y值
            y_vals = []
            for x_val in x_vals:
                try:
                    y_val = float(func.subs(self.x, x_val))
                    # 检查是否有意义
                    if math.isnan(y_val) or math.isinf(y_val):
                        y_vals.append(np.nan)
                    else:
                        y_vals.append(y_val)
                except:
                    y_vals.append(np.nan)
            
            y_vals = np.array(y_vals)
            
            # 清空画布
            self.ax.clear()
            
            # 绘制函数
            self.ax.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'f(x) = {self.func_entry.get()}')
            
            # 绘制坐标轴
            self.ax.axhline(y=0, color='black', linewidth=0.5)
            self.ax.axvline(x=0, color='black', linewidth=0.5)
            
            # 设置网格
            if self.grid_var.get():
                self.ax.grid(True, alpha=0.3)
            
            # 设置标签
            self.ax.set_xlabel('x', fontsize=12)
            self.ax.set_ylabel('y', fontsize=12)
            self.ax.set_title('函数图像', fontsize=14, fontweight='bold')
            self.ax.legend()
            
            # 自动调整y轴范围
            y_finite = y_vals[np.isfinite(y_vals)]
            if len(y_finite) > 0:
                y_min, y_max = np.nanmin(y_finite), np.nanmax(y_finite)
                y_range = y_max - y_min
                if y_range > 0:
                    self.ax.set_ylim(y_min - 0.1*y_range, y_max + 0.1*y_range)
            
            self.ax.set_xlim(xmin, xmax)
            
            # 刷新画布
            self.canvas.draw()
            
            # 清空结果
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"✅ 函数 f(x) = {self.func_entry.get()} 绘制成功\n")
            self.result_text.insert(tk.END, f"📊 x范围: [{xmin}, {xmax}]\n")
            
        except Exception as e:
            messagebox.showerror("错误", f"绘图失败: {str(e)}")
    
    def calc_value(self):
        """计算函数值"""
        func = self.get_function()
        if func is None:
            return
        
        try:
            x_val = float(self.val_entry.get())
            y_val = float(func.subs(self.x, x_val))
            
            if math.isnan(y_val) or math.isinf(y_val):
                self.val_result.config(text="无意义")
            else:
                self.val_result.config(text=f"{y_val:.6f}")
                
            # 添加到结果
            self.result_text.insert(tk.END, f"📌 f({x_val}) = {y_val:.6f}\n")
            self.result_text.see(tk.END)
            
        except Exception as e:
            messagebox.showerror("错误", f"计算失败: {str(e)}")
    
    def find_zeros(self):
        """求零点"""
        func = self.get_function()
        if func is None:
            return
        
        try:
            xmin = float(self.xmin_entry.get())
            xmax = float(self.xmax_entry.get())
            
            # 使用sympy求解
            solutions = sp.solve(func, self.x)
            
            # 过滤实数解且在范围内的
            zeros = []
            for sol in solutions:
                if sol.is_real:
                    sol_val = float(sol)
                    if xmin <= sol_val <= xmax:
                        zeros.append(sol_val)
            
            if zeros:
                self.result_text.insert(tk.END, f"🎯 零点 (在 [{xmin}, {xmax}] 范围内):\n")
                for z in zeros:
                    self.result_text.insert(tk.END, f"   x = {z:.6f}\n")
                
                # 在图上标记零点
                for z in zeros:
                    self.ax.plot(z, 0, 'ro', markersize=8)
                    self.ax.axvline(x=z, color='red', linestyle='--', alpha=0.5)
                self.canvas.draw()
            else:
                self.result_text.insert(tk.END, "❌ 在指定范围内未找到零点\n")
            
            self.result_text.see(tk.END)
            
        except Exception as e:
            messagebox.showerror("错误", f"求零点失败: {str(e)}")
    
    def find_extrema(self):
        """求极值点"""
        func = self.get_function()
        if func is None:
            return
        
        try:
            xmin = float(self.xmin_entry.get())
            xmax = float(self.xmax_entry.get())
            
            # 求导数
            derivative = sp.diff(func, self.x)
            
            # 解导数方程
            critical_points = sp.solve(derivative, self.x)
            
            extrema = []
            for point in critical_points:
                if point.is_real:
                    point_val = float(point)
                    if xmin <= point_val <= xmax:
                        # 计算二阶导数判断极值类型
                        second_deriv = sp.diff(derivative, self.x)
                        try:
                            second_val = float(second_deriv.subs(self.x, point))
                            y_val = float(func.subs(self.x, point))
                            if second_val > 0:
                                extrema.append((point_val, y_val, "极小值"))
                            elif second_val < 0:
                                extrema.append((point_val, y_val, "极大值"))
                            else:
                                extrema.append((point_val, y_val, "鞍点"))
                        except:
                            extrema.append((point_val, float(func.subs(self.x, point)), "极值点"))
            
            if extrema:
                self.result_text.insert(tk.END, f"📈 极值点 (在 [{xmin}, {xmax}] 范围内):\n")
                for x_val, y_val, typ in extrema:
                    self.result_text.insert(tk.END, f"   {typ}: ({x_val:.6f}, {y_val:.6f})\n")
                    # 在图上标记
                    self.ax.plot(x_val, y_val, 'g*', markersize=12)
                self.canvas.draw()
            else:
                self.result_text.insert(tk.END, "❌ 在指定范围内未找到极值点\n")
            
            self.result_text.see(tk.END)
            
        except Exception as e:
            messagebox.showerror("错误", f"求极值失败: {str(e)}")
    
    def find_intersection(self):
        """求与x轴交点（同上，保留作为独立功能）"""
        self.find_zeros()
    
    def save_plot(self):
        """保存图像"""
        from tkinter import filedialog
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG 图片", "*.png"), ("JPG 图片", "*.jpg"), ("PDF 文件", "*.pdf")]
        )
        if filename:
            self.fig.savefig(filename, dpi=300, bbox_inches='tight')
            messagebox.showinfo("保存成功", f"图像已保存到:\n{filename}")
    
    def reset_view(self):
        """重置视图"""
        self.plot_function()
    
    def toggle_grid(self):
        """切换网格显示"""
        self.grid_var.set(not self.grid_var.get())
        self.plot_function()

if __name__ == "__main__":
    root = tk.Tk()
    app = FunctionPlotter(root)
    root.mainloop()
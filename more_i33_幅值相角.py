import pandapower as pp
import pandas as pd
import numpy as np
import os
import pandapower.networks as pn
import random
from init_data_i33 import loads,lines
# 定义 CSV 文件名
csv_file = 'output_data_degree.csv'
with open(csv_file, 'w') as f:
    f.write('bus,U,degree,p,q\n')  # 写入表头
with open('loads_train.csv', 'w') as f:
    f.write('bus,p,q\n')  # 写入表头
# create empty net
#迭代次数
#epochs = 2
simples=100
#print(f'load长度={len(loads)}')
#print(f'line长度={len(lines)}')
def generate_random_sum(n, target_sum, min_val, max_val):
    # 生成 n 个随机数
    random_values = [random.uniform(min_val, max_val) for _ in range(n)]
    # 归一化并乘以目标总和
    total = sum(random_values)
    normalized_values = [value / total * target_sum for value in random_values]
    return normalized_values
#创建网络
net = pp.create_empty_network()
net=pp.create_empty_network()
for i in range (33):
    pp.create_bus(net, name='bus%s' % i, vn_kv=10, type='n')
bus8= net.bus.index[8]
bus14= net.bus.index[14]
bus11= net.bus.index[11]
bus21= net.bus.index[21]
bus7= net.bus.index[7]
bus20= net.bus.index[20]
bus24= net.bus.index[24]
bus28= net.bus.index[28]
bus17= net.bus.index[17]
bus32= net.bus.index[32]
bus0= net.bus.index[0]
sw1 = pp.create_switch(net, bus8, bus14, et="b", type="CB", closed=True)
sw2 = pp.create_switch(net, bus11, bus21, et="b", type="CB", closed=True)
sw3 = pp.create_switch(net, bus7, bus20, et="b", type="CB", closed=True)
sw4 = pp.create_switch(net, bus24, bus28, et="b", type="CB", closed=True)
sw5 = pp.create_switch(net, bus17, bus32, et="b", type="CB", closed=True)
pp.create_ext_grid(net, bus0, vm_pu=1.02, va_degree=0,max_p_mw=5.08426, max_q_mvar=2.54732)
#循环创建随机
for epoch in range(simples):
    new_lines = []
    for line in lines:
        # 生成随机值
        random_value_3 = random.uniform(0.08, 1.1)
        random_value_4 = random.uniform(0.05, 1.0)

        # 创建新的元组，替换第3列和第4列
        new_line = (line[0], line[1], random_value_3, random_value_4)
        new_lines.append(new_line)
    new_loads = []
    # 预生成 random_value_3 和 random_value_4
    num_loads = len(loads)-1
    random_values_p = generate_random_sum(num_loads, 3.755, 0.08, 1.1)
    random_values_q = generate_random_sum(num_loads, 2.5, 0.05, 1.0)
    for i,load in enumerate(loads):
        if i == 0:
            # 第一行不替换
            new_load = (load[0], 3.755, 2.5)
            new_loads.append(new_load)
        else:
            # 从第二行开始替换第3列和第4列
            new_load = (load[0], random_values_p[i-1], random_values_q[i-1])
            new_loads.append(new_load)
    loads_new = pd.DataFrame(new_loads, columns=['bus', 'p_mw', 'q_mvar'])
    #loads_new.to_csv('loads_train.csv', mode='a', header=False, index=False)
    # 创建线路
    for line in new_lines:
        from_bus, to_bus, r, x = line
        pp.create_line_from_parameters(net, from_bus=from_bus, to_bus=to_bus, length_km=1, r_ohm_per_km=r,
                                       x_ohm_per_km=x, c_nf_per_km=0.0, g_ohm_per_km=0.0, max_i_ka=0.4)
    for load in new_loads:
        bus_index, p_mw, q_mvar = load
        pp.create_load(net, bus=bus_index, p_mw=p_mw, q_mvar=q_mvar, sn_mva=10)
    pp.runpp(net)
    #print(net.res_bus)
    #print(f"epoch:{epoch}")
    #print("--------------------"*2)
    # 提取 res_bus
    res_bus = net.res_bus

    # 计算实部和虚部
    vm = res_bus['vm_pu'].values  # 电压幅值
    va = res_bus['va_degree'].values  # 电压相角

    U=vm*12.66

    # 创建新的 DataFrame res_bus2
    res_bus2 = pd.DataFrame({
        'bus': res_bus.index,
        'U_part': U,
        'imaginary_part': va,
        'p_mw': res_bus['p_mw'],
        'q_mvar': res_bus['q_mvar']
    })

    # 打印新的 res_bus2
    #print(f"a+bj=\n{res_bus2}")
    res_bus2.to_csv(csv_file, mode='a', header=False, index=False)
    print("ie33生成train数据：",epoch)
print("ie33生成train数据完成")
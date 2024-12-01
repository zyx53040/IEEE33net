#%%
import pandapower as pp
import pandas as pd
import numpy as np
import os
# create empty net
net = pp.create_empty_network()
#%%
net=pp.create_empty_network()
#Bus1=pp.create_bus(net, name='Busbar1', vn_kv=10, type='b')
#Bus2=pp.create_bus(net, name='Busbar2', vn_kv=10, type='b')
#Bus3=pp.create_bus(net, name='Busbar5', vn_kv=10, type='b')
for i in range (33):
    pp.create_bus(net, name='bus%s' % i, vn_kv=10, type='n')
        

        
#%%
#net.bus
#%%
# 获取 bus8 的信息
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
# 打印 bus8 的信息

#%%
#switch
sw1 = pp.create_switch(net, bus8, bus14, et="b", type="CB", closed=True)
sw2 = pp.create_switch(net, bus11, bus21, et="b", type="CB", closed=True)
sw3 = pp.create_switch(net, bus7, bus20, et="b", type="CB", closed=True)
sw4 = pp.create_switch(net, bus24, bus28, et="b", type="CB", closed=True)
sw5 = pp.create_switch(net, bus17, bus32, et="b", type="CB", closed=True)
#%%
#net.load
#%%
#节点负载信息
loads = [
    (1, 0.1, 0.06),   # 节点1
    (2, 0.09, 0.04),  # 节点2
    (3, 0.12, 0.08),  # 节点3
    (4, 0.06, 0.03),  # 节点4
    (5, 0.06, 0.02),  # 节点5
    (6, 0.2, 0.1),    # 节点6
    (7, 0.2, 0.1),    # 节点7
    (8, 0.06, 0.02),   # 节点8
    (9, 0.06, 0.02),   # 节点9
    (10, 0.045, 0.03), # 节点10
    (11, 0.06, 0.035), # 节点11
    (12, 0.06, 0.035), # 节点12
    (13, 0.12, 0.08),  # 节点13
    (14, 0.1, 0.1),    # 节点14
    (15, 0.06, 0.02),   # 节点15
    (16, 0.06, 0.02),   # 节点16
    (17, 0.09, 0.04),   # 节点17
    (18, 0.09, 0.04),   # 节点18
    (19, 0.09, 0.04),   # 节点19
    (20, 0.09, 0.04),   # 节点20
    (21, 0.09, 0.04),   # 节点21
    (22, 0.09, 0.05),   # 节点22
    (23, 0.42, 0.2),    # 节点23
    (24, 0.42, 0.2),    # 节点24
    (25, 0.06, 0.025),   # 节点25
    (26, 0.06, 0.025),   # 节点26
    (27, 0.06, 0.02),    # 节点27
    (28, 0.12, 0.07),    # 节点28
    (29, 0.2, 0.6),      # 节点29
    (30, 0.15, 0.2),     # 节点30
    (31, 0.21, 0.1),     # 节点31
    (32, 0.06, 0.02),    # 节点32
]
m=len(loads)
#节点间支路阻抗信息
lines = [
    (0, 1, 0.0922, 0.047),  # 从节点0到节点1
    (1, 2, 0.4930, 0.2511),  # 从节点1到节点2
    (2, 3, 0.3660, 0.1864),  # 从节点2到节点3
    (3, 4, 0.3811, 0.1941),  # 从节点3到节点4
    (4, 5, 0.8190, 0.7070),  # 从节点4到节点5
    (5, 6, 0.1872, 0.6188),  # 从节点5到节点6
    (6, 7, 0.7114, 0.2351),  # 从节点6到节点7
    (7, 8, 1.0300, 0.7400),  # 从节点7到节点8
    (8, 9, 1.0440, 0.7400),  # 从节点8到节点9
    (9, 10, 0.1966, 0.0650), # 从节点9到节点10
    (10, 11, 0.3744, 0.1238),# 从节点10到节点11
    (11, 12, 1.4680, 1.1550),# 从节点11到节点12
    (12, 13, 0.5416, 0.7129),# 从节点12到节点13
    (13, 14, 0.5910, 0.5260),# 从节点13到节点14
    (14, 15, 0.7463, 0.5450),# 从节点14到节点15
    (15, 16, 1.2890, 1.7210),# 从节点15到节点16
    (16, 17, 0.3720, 0.5740),# 从节点16到节点17
    (17, 18, 0.1640, 0.1565),# 从节点17到节点18
    (18, 19, 1.5042, 1.3554),# 从节点18到节点19
    (19, 20, 0.4095, 0.4784),# 从节点19到节点20
    (20, 21, 0.7089, 0.9373),# 从节点20到节点21
    (21, 22, 0.4512, 0.3083),# 从节点21到节点22
    (22, 23, 0.8980, 0.7091),# 从节点22到节点23
    (23, 24, 0.8960, 0.7011),# 从节点23到节点24
    (24, 25, 0.2030, 0.1034),# 从节点24到节点25
    (25, 26, 0.2842, 0.1447),# 从节点25到节点26
    (26, 27, 1.0590, 0.9337),# 从节点26到节点27
    (27, 28, 0.8042, 0.7006),# 从节点27到节点28
    (28, 29, 0.5075, 0.2585),# 从节点28到节点29
    (29, 30, 0.9744, 0.9630),# 从节点29到节点30
    (30, 31, 0.3105, 0.3619),# 从节点30到节点31
    (31, 32, 0.3410, 0.5362),# 从节点31到节点32
    (7,20,2,2),# 从节点7到节点20
    (8,14,2,2),# 从节点8到节点14
    (11,21,2,2),# 从节点11到节点21
    (17,32,0.5,0.5),# 从节点17到节点32
    (24,28,0.5,0.5),# 从节点24到节点28
]


#%%
# 创建线路
for line in lines:
    from_bus, to_bus, r, x = line
    pp.create_line_from_parameters(net, from_bus=from_bus, to_bus=to_bus, length_km=1, r_ohm_per_km=r, x_ohm_per_km=x,c_nf_per_km=0.0,g_ohm_per_km=0.0,max_i_ka=0.4)
#%%
#net.line
#%%
#创建阻抗
for load in loads:
    bus_index, p_mw, q_mvar = load
    pp.create_load(net, bus=bus_index, p_mw=p_mw, q_mvar=q_mvar,sn_mva=10)
#%%
#net.load
#%%
#pp.create_gen(net, bus0, p_mw=5.08426, max_q_mvar=2.54732, min_q_mvar=-3, vm_pu=1.266, name="generator") 
#net.bus
#%%
#pp.create_ext_grid(net, bus0, vm_pu=1.02, va_degree=0,max_p_mw=5.08426, max_q_mvar=2.54732) 
pp.create_ext_grid(net, bus0, vm_pu=1.02, va_degree=0,max_p_mw=4.260959, max_q_mvar=2.644403)
#%%

#%%
pp.runpp(net)
#%%
#net.ext_grid
#%%
print(f"res_bus=\n{net.res_bus}")
#%%
# 从结果中提取母线电压幅值（标幺值）
vm_pu = net.res_bus['vm_pu']
va_degree = net.res_bus['va_degree']
# 打印或处理vm_pu数据

#%%
print('net.res_line\n', net.res_line)
#%% md
# 1. **p_from (MVA)**: 从母线“from”流向母线“to”的有功功率（正值表示流出，负值表示流入）。
# 2. **q_from (MVar)**: 从母线“from”流向母线“to”的无功功率（正值表示感性无功流出或容性无功流入，负值相反）。
# 3. **p_to (MVA)**: 等同于从母线“to”看进去的有功功率接收量（与`p_from`数值相同但符号相反，如果忽略线路损耗的话）。
# 4. **q_to (MVar)**: 等同于从母线“to”看进去的无功功率接收量（与`q_from`数值相同但符号相反，如果忽略线路损耗和充电功率的话）。
# 5. **pl_mw**: 线路上的有功损耗（MW），即由于电阻发热等原因在线路上损失的有功功率。
# 6. **ql_mvar**: 线路上的无功损耗（MVar），主要由线路的感抗引起，也可能包括电容效应导致的无功补偿。
# 7. **vm_from_pu**: 发电端（from bus）电压幅值的标幺值。
# 8. **va_from_degree**: 发电端（from bus）电压相角，单位为度。
# 9. **vm_to_pu**: 受电端（to bus）电压幅值的标幺值。
# 10. **va_to_degree**: 受电端（to bus）电压相角，单位为度。
# 11. **loading_percent**: 线路的负载率百分比，基于线路的额定容量计算得出，是评估线路过载情况的一个重要指标。
#%%
#net.res_load
#%%
'''import networkx as nx
import matplotlib.pyplot as plt

# 假设 net 是一个包含 bus 和 line 数据的字典
buses = net["bus"]
lines = net["line"]

G = nx.Graph()

# 添加总线节点
for _, bus in buses.iterrows():
    G.add_node(bus['name'], type='bus', vn_kv=bus['vn_kv'])

# 添加线路边
for _, line in lines.iterrows():
    G.add_edge(line['from_bus'], line['to_bus'], type='line')

pos = nx.spring_layout(G)  # 计算节点的位置

# 创建图形和轴
fig, ax = plt.subplots()

# 画节点
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', ax=ax)

# 画边
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, alpha=0.5, ax=ax)

# 画节点标签
labels = {n: f"{n} {G.nodes[n].get('vn_kv', 'N/A')}kV" for n in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_family="sans-serif", ax=ax)

# 显示图形
plt.title("PandaPower Network Topology")
plt.show()
'''
                                                                                        
'''
import networkx as nx
import matplotlib.pyplot as plt
import pandapower.plotting as plot
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制电网
plot.simple_plot(net, ax=ax)

# 设置标题和显示图形
plt.title("Pandapower Network Visualization with Custom Coordinates")
plt.show()
'''

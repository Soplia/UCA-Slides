<h3 style = "text-align:center"> Hata Model </h3>

移动通信中，由于移动台在不停的运动，电波传播的实际情况是复杂多变的。为此，人们通过大量的实地测量和分析，总结归纳了多种经验模型。通常在一定情况下，使用这些模型对移动通信电波传播特性进行估算，都能获得比较准确的预测结果。

能否准确预测基站信号的覆盖情况是移动通信网络规划的优劣所在，提高预测准确度的关键在于选择最能接近实测值的预测模型。

预测模型的目标是预测特定点或特定区域(小区)的信号强度，但在方法复杂性和精确性方面差异很大，因此针对不同地形特点，要选择最适合于本地的预测模型。

城区、郊区、开阔地和空间自由传播

在无线通信系统中，电波通常在非规则非单一的环境中传播。在估计信道损耗时，需要考虑传播路径上的地形地貌，也要考虑到建筑物、树木、电线杆等阻挡物[1]。不同的室外传播环境模型适用于不同的环境，





Okumura/Hata模型是以准平滑地形的市区作基准，其余各区的影响均以校正因子的形式出现。

随着距离的增大，接收信号强度逐渐减小，然而衰减的速率是不同的：空间自由传播的情况下衰减速率最小，其次是开阔地和郊区，城区的衰减速率最大

接收信号强度与距离的非线形关系



池塘中的波纹：能量从源点向四周传播，并逐渐减弱

电磁波的传播（当辐射源是各向同性的理想点源时）：

–在三维空间以球面波的形式传播

–传播介质不同，空气、障碍物、反射物



$$Lm = Lu - 2[log(f / 28)]^2 - 5.4$$



$$Lm = Lu -4.78(logf)^2 + 18.33logf - 40.98​$$





\ Model folding
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
 
Subject To
 f0_0: - w[0] + y0[0] = 0
 f0_1: - w[2] + 6 y0[0] + 9 y0[1] = 0
 f0_2: - w[3] + 6 y0[0] + 4.5 y0[1] = 0
 nf0_0: - w[1] + 12 y0[0] <= -1e-05
 f1_0: - w[0] + y1[0] = 0
 f1_1: - w[1] + 12 y1[0] = 0
 f1_2: - w[3] + 6 y1[0] + 4.5 y1[1] = 0
 nf1_0: - w[2] + 6 y1[0] + 9 y1[1] <= -1e-05
 f2_0: - w[1] + 12 y2[0] = 0
 f2_1: - w[2] + 6 y2[0] + 9 y2[1] = 0
 f2_2: - w[3] + 6 y2[0] + 4.5 y2[1] = 0
 nf2_0: - w[0] + y2[0] <= -1e-05
Bounds
 y0[0] free
 y0[1] free
 y1[0] free
 y1[1] free
 y2[0] free
 y2[1] free
End

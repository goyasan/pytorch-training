import numpy as np

data = np.array([
    [ [65, 70], [56, 80], [78, 68], [90, 85], [60, 75] ],
    [ [70, 75], [54, 88], [82, 64], [88, 83], [58, 78] ],
    [ [67, 72], [52, 82], [80, 66], [86, 80], [59, 74] ]
])

print("データの形状：", data.shape)
print("各クラスの平均点：", data.mean(axis=1))
print("各クラスの番号３番の学生での二科目目の最高点：", data[:,2,1].max())
print("各科目の最高得点と最低得点の差：",[data[:,:,0].max() - data[:,:,0].min() ,data[:,:,1].max() - data[:,:,1].min()])
print("各科目で一教科目が８０点以上の人数：", np.where(data[:,:,0] >= 80, 1, 0).sum())
print("二科目の合計得点が１３５点以上の人数：", np.sum(np.sum(data, axis=2) > 135))
print("全生徒の一科目目と二科目目の点数の相関係数", np.sum((data[:,:,0] - data[:,:,0].mean()) * (data[:,:,1] - data[:,:,1].mean())) / (np.sum(np.sqrt(((data[:,:,0] - data[:,:,0].mean()))**2)) * np.sum(np.sqrt(((data[:,:,1] - data[:,:,1].mean()))**2))))

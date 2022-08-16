# GitHub Practice
### 本練習以特徵提取程式碼開發為例，演練Git實務。
學員將練習應用GitHub合作撰寫特徵提取程式碼，目標為成功自example_rawdata.csv提取10個時域特徵值，並以一個List按照下列特徵順序輸出。

## 10個時域特順序與數學公式
1. Root mean square: 
$$x_{rms}=\sqrt{\frac{1}{N}\sum_{j=1}^{N}\left(x_j\right)^2}$$
2. Mean:
$$x_m=\bar{x}=\frac{1}{N}\sum_{j=1}^{N}x_j$$
3. Standard deviation
$$x_{std}=\sigma=\sqrt{\frac{1}{N-1}\sum_{j=1}^{N}\left(x_j-\bar{x}\right)^2}$$
4. Peak to Peak:
$$x_{p2p}=\left|\max{x}-\min{x}\right|$$
5. Kurtosis:
$$x_{ku}=\frac{\frac{1}{N}\sum_{i=1}^{N}\left(x_i-\bar{x}\right)^4}{\left[\frac{1}{N}\sum_{i=1}^{N}\left(x_i-\bar{x}\right)^2\right]^2}$$
6. Skewness:
$$x_{sk}=\frac{\frac{1}{N}\sum_{i=1}^{N}\left(x_i-\bar{x}\right)^3}{\left[\frac{1}{N}\sum_{i=1}^{N}\left(x_i-\bar{x}\right)^2\right]^\frac{3}{2}}$$
7. Crest indicator:
$$x_{ci}=\frac{max\left|{x}\right|}{\sqrt{\left(1/N\right)\sum_{j=1}^{N}\left(x_j\right)^2}}$$
8. Clearance indicator:
$$x_{cli}=\frac{max\left|{x}\right|}{\left(\left(1/N\right)\sum_{j=1}^{N}\sqrt{\left|x_j\right|}\right)^2}$$
9. Shape indicator:
$$x_{si}=\frac{\sqrt{\left(1/N\right)\sum_{j=1}^{N}\left(x_j\right)^2}}{\left(1/N\right)\sum_{j=1}^{N}\left|x_j\right|}$$
10. Impulse indicator:
$$x_{mi}=\frac{max\left|{x}\right|}{\left(1/N\right)\sum_{j=1}^{N}\left|x_j\right|}$$

## 演練Git功能包含
1. 創立分支 Creating a branch
2. 提交程式碼變更 Making and committing changes
3. 建立拉取請求 Opening a pull request
4. 合併拉取請求 Merging your pull request
5. 建立議題 Opening a Issue

# weibo_data
* Weibo data prediction
* Create date: 20180113
* Author: HZT

---
---
# 数据清洗
washing.py
* 训练集中有的行不是用逗号分开的，是用\t分开的，所以要把\t替换成逗号
* 有的行不是有效行，是混乱的信息，这些行的fcs，ccs，lcs都是NaN，要剔除掉

---
---
# 预处理
preprocessor.py

## 得到用户特征值
`luid,count,max_fcs,min_fcs,avg_fcs,max_ccs,min_ccs,avg_ccs,max_lcs,min_lcs,avg_lcs,max_sum,min_sum,avg_sum,above_avg_rate（未研究）`
* 要先对数据集有个大概的认识
* 有多少条数据
* 用户有多少人
* 各项数据的极值是多少，分布大概如何
* 训练集的sum分布如何
* content要怎么从中选取关键词
* 时间拆分成星期和时间段两个特征

## 得到内容特征

## 得到时间特征

---
---
# 预测
* 如果测试集中的用户在washed_userfeature.txt中出现了，就认为其互动数不为0，进行以下操作
    1. 一个用户的`avg_fcs`,`avg_ccs`,``avg_lcs`小于1，那么就取其最大值作为预测值
    2. 若大于1，则取其平均值作为预测值。
* 如果测试集中的用户在washed_userfeature.txt中没有对应，就认为其互动数为0

---
---
# 问题探究
* 发送量很大的用户互动数为0，探究其内容特征
* 得到了用户特征、内容特征、时间特征之后，如果把这些特征联合起来得到最后的结果？（使用什么算法？？？）
* 能不能把时间和内容之间建立联系，找出那段时间的话题是什么

---
---
# 参考资料
* http://blog.csdn.net/xieyan0811/article/details/78750611
* http://blog.csdn.net/jingyi130705008/article/details/78257350
* http://blog.csdn.net/fjssharpsword/article/details/78412803?locationNum=7&fps=1
* http://lemondy.github.io/2015/12/01/sina_weibo_big_data_competition/
# Neural Subgraph Matching
# Basic Information:

- Title: Neural Subgraph Matching (神经子图匹配)
- Authors: Rex Ying, Zhaoyu Lou, Jiaxuan You, Chengtao Wen, Arquimedes Canedo, Jure Leskovec
- Affiliation: Department of Computer Science, Stanford University (斯坦福大学计算机科学系)
- Keywords: subgraph matching, graph neural network, embeddings, voting mechanism
- URLs: [Paper](https://arxiv.org/abs/2007.03092), [GitHub](https://github.com/stanford-futuredata/NeuroMatch)

Note: The affiliation provided above only applies to the first three authors of the paper. The remaining authors are affiliated with Siemens Corporate Technology.

# Summary:

- a. Research background of this article:
  - 本文关于拓扑子图的匹配问题，传统方法如组合匹配和整数规划难以处理target和query graph规模较大的匹配问题。
- b. Past methods, their problems, and motivation:
  - 传统方法如组合匹配和整数规划难以处理target和query graph规模较大的匹配问题，必须寻求一种能够处理较大规模匹配问题的新方法。
- c. Research methodology proposed in this paper:
  - 本文提出了一种新的拓扑子图匹配方法NeuroMatch。NeuroMatch将图分解为小的子图并使用图神经网络（GNN）对其进行嵌入以捕获几何约束。而后在嵌入空间中进行子图匹配。
- d. Task and performance achieved by the methods in this paper:
  - NeuroMatch的性能通过与state-of-the-art的组合方法进行比较，实验结果表明它的效率更高，并且比现有的近似子图匹配方法更准确18%。

# Background:

- a. Subject and characteristics:
  - 本文研究的主题是关于拓扑子图匹配问题。
- b. Historical development:
  - 传统方法诸如组合匹配和整数规划等难以处理target和query graph规模较大的匹配问题。
- c. Past methods:
  - 过去的方法包括组合匹配和整数规划等。
- d. Past research shortcomings:
  - 传统算法难以处理规模较大的拓扑子图匹配问题。
- e. Current issues to address:
  - 如何处理规模较大的拓扑子图匹配问题。

# Methods:

- a. Theoretical basis of the study:
  - 本文的理论基础是图神经网络（GNN），GNN学习节点和子图的嵌入表示，以预测拓扑同构。
- b. Technical route of the article (step by step):
  - NeuroMatch分两个阶段，首先通过GNN学习节点和子图的嵌入表示，然后使用子图预测函数，在嵌入空间中预测是否存在拓扑同构性。
  - 在预测结果中，NeuroMatch还对匹配节点进行投票机制以提高匹配的准确性。
  - 采用课程学习方法进行模型训练，并通过随机采样大型目标图的子图来生成训练数据。
  - 性能评估采用基准数据集，结果表明NeuroMatch表现出优秀的性能，远高于传统方法。

# Conclusion:

- a. Significance of the work:
  - 本文提出的NeuroMatch算法可以有效地解决拓扑子图匹配问题，在求解效率和准确性方面表现出色。
- b. Innovation, performance, and workload:
  - 与传统算法相比，NeuroMatch使用GNN进行图嵌入，可以使子图关系被保留，并加入有效的归纳偏差，这样就可以大大简化查询过程。
  - 实验结果表明，NeuroMatch在求解效率和准确性上都优于传统算法。
- c. Research conclusions (list points):
  - 本文提出了一种基于图神经网络的新型拓扑子图匹配算法NeuroMatch。
  - NeuroMatch使用图嵌入技术来捕获几何约束，以有效地解决规模较大的拓扑子图匹配问题。
  - 实验结果表明，NeuroMatch在求解效率和准确性方面均优于传统算法。
  - NeuroMatch的研究成果受到多家机构和组织的支持，包括DARPA、ARO、NSF、Stanford数据科学倡议、吴才神经科学研究所、陈·扎克伯格生物中心等。
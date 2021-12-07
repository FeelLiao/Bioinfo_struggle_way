# WGS 数据分析

## 1. 原始测序数据质控

### 1.1 数据质控的意义

以illumina为首的NGS测序基本都是运用边合成边测序的技术，合成过程中随着合成链的增长，DNA聚合酶的效率会下降，特异性也会变差，因此越到后面碱基合成的错误率就会越高，这也是为什么NGS测序读长普遍偏短的原因。另外，有时候测序仪在刚开始进行合成反应的时候由于反应还不够稳定，同样会带来质量值的波动，不过这种波动一般都在高质量区。

测序数据的好坏会影响到下游的数据分析，但不同测序平台的测序错误率是存在差别的，因此，在分析测序数据之前应该先搞清楚两个地方：

- 原始数据产生的平台，它的错误分布率怎么样，是否具有一定的偏向和局限，是否显著受GC含量的影响等。
- 评估它们可能影响哪些方面的分析。

如何去认识一个原始的测序数据（fastq data）呢？一般可以从一下几个方面入手：

- read各个位置的碱基质量值分布
- 碱基总体质量值分布
- **read各个位置上的碱基分布比例，分析碱基的分离程度**
- **GC含量**
- **read各位置的N含量**
- read是否还包含测序接头序列
- read重复率，由实验扩增过程引起

现在有很多工具可以高效的完成测序数据的质量控制，比较常用的是[FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)，Linux可以直接通过anaconda安装。

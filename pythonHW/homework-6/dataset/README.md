# Dataset folder

**Author**: Yintao, XU, **Date**: 2020/02/17

This folder should include all necessary datasets, downloaded from `gazelib.utils.download_csv_mpIIdataset` and `gazelib.utils.download_demo_Img`.

**Note:** **In most cases, you should not download it manually. Cells in Jupyter notebook will help you download datasets by scripts!**

## Description

This folder should include two csv files for **MPIIGaze dataset** and one demo image.

```
├── demo.jpeg
├── test.csv
└── train.csv
```

- `train.csv`: training set of MPIIGaze. [[Manually download link](http://data.liubai01.cn:81/f/768e16137c1e4fb1b1c6/)]
- `test.csv`: test set of MPIIGaze.[[Manually download link](http://data.liubai01.cn:81/f/0d94a125c8c24f059254/)]
- `demo.jpeg`: a demo image for visualization. [[Manually download link](http://data.liubai01.cn:81/f/5c59f03d303740cfa3ce/)]

## Reference

```Bibtex
@inproceedings{zhang15_cvpr,
Author = {Xucong Zhang and Yusuke Sugano and Mario Fritz and Bulling, Andreas},
Title = {Appearance-based Gaze Estimation in the Wild},
Booktitle = {Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
Year = {2015},
Month = {June}
Pages = {4511-4520}
}
```
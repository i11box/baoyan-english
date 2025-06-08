# BAOYAN English
记录了一些可能会被问到的口试问题，并用文本转语音技术模拟问题

## 项目结构

```
.
├── data/                   # 数据目录
│   ├── problems.txt       # 问题文本文件，包含所有问题
│   └── wavs/              # 音频文件目录，存储所有问题的录音文件
└── main.py                # 主程序入口
```

- `data/problems.txt`  
  纯文本文件，每行包含一个问题
- `data/wavs/`  
  音频文件目录，存放所有问题的录音文件
- `main.py`  
  程序主入口

## 启动项目
```sh
git clone https://github.com/your-repo/your-repo.git
cd your-repo
conda create -n baoyan python=3.12
conda activate baoyan
pip install pydub # 需要先安装ffmpeg
python main.py
```

- 按下回车播放音频
- 按下r加回车重新播放
- 按下q加回车退出

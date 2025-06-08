# BAOYAN English
记录了一些可能会被问到的口试问题，并用文本转语音技术模拟问题

## 项目结构
- data
  - problems.txt: 存放问题的文本文件
  - wavs: 存放问题的音频文件
- main.py: 主程序

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

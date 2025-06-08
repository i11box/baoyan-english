# audio_player.py
import os
import random
from pydub import AudioSegment
from pydub.playback import play
import sys

def get_audio_files(directory):
    """获取目录下所有的wav文件"""
    if not os.path.exists(directory):
        print(f"错误：目录 {directory} 不存在")
        return []
    
    audio_files = [os.path.join(directory, f) for f in os.listdir(directory) 
                  if f.lower().endswith('.wav')]
    
    if not audio_files:
        print(f"错误：在 {directory} 中没有找到wav文件")
        return []
    
    return audio_files

def play_random_audio(audio_files, played_indices, repeated_index = -1):
    """随机播放一个未播放过的音频"""
    if len(played_indices) >= len(audio_files):
        print("所有音频已播放完毕！")
        return False
    
    # 获取未播放的音频索引
    if repeated_index == -1:
        available_indices = [i for i in range(len(audio_files)) if i not in played_indices]
        chosen_index = random.choice(available_indices)
    else:
        chosen_index = repeated_index
    audio_file = audio_files[chosen_index]
    
    try:
        print(f"正在播放: {os.path.basename(audio_file)}")
        audio = AudioSegment.from_file(audio_file)
        play(audio)
        played_indices.add(chosen_index)
        return True, chosen_index
    except Exception as e:
        print(f"播放 {audio_file} 时出错: {e}")
        return False, -1

def main():
    # 设置音频目录
    audio_dir = os.path.join('data', 'wavs')
    
    # 获取所有音频文件
    audio_files = get_audio_files(audio_dir)
    if not audio_files:
        return
    
    # 打乱音频文件顺序
    random.shuffle(audio_files)
    played_indices = set()  # 记录已播放音频的索引
    
    print(f"找到 {len(audio_files)} 个音频文件")
    print("按回车键播放随机音频，输入 'q' 退出...")
    
    last_index = -1
    while True:
        user_input = input()
        if user_input.lower() == 'q':
            print("退出播放器")
            break
        if user_input.lower() == 'r':
            if last_index == -1:
                print("尚未播放音频，或上个音频播放出错")
                continue
            play_random_audio(audio_files, played_indices, repeated_index=last_index)
            print("重新播放")
            
        flag, last_index = play_random_audio(audio_files, played_indices)
        if not flag:
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"发生错误: {e}")
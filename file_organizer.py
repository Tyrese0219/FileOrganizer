import os
import shutil

# 文件类型分类规则
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".flac"],
}

def organize_files(directory):
    """整理指定文件夹内的文件"""
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # 跳过子文件夹和隐藏文件
        if os.path.isdir(filepath) or filename.startswith("."):
            continue
        
        # 获取文件扩展名
        _, ext = os.path.splitext(filename)
        ext = ext.lower()  # 统一转小写
        
        # 查找匹配的类别
        moved = False
        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                # 创建目标文件夹（如果不存在）
                target_dir = os.path.join(directory, category)
                os.makedirs(target_dir, exist_ok=True)
                
                # 移动文件
                shutil.move(filepath, os.path.join(target_dir, filename))
                print(f"Moved: {filename} -> {category}/")
                moved = True
                break
        
        # 未匹配的文件放入 "Other" 文件夹
        if not moved:
            target_dir = os.path.join(directory, "Other")
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(filepath, os.path.join(target_dir, filename))
            print(f"Moved: {filename} -> Other/")

if __name__ == "__main__":
    target_directory = input("Enter the directory path to organize: ").strip()
    if os.path.isdir(target_directory):
        organize_files(target_directory)
        print("File organization completed!")
    else:
        print("Error: Invalid directory path.")

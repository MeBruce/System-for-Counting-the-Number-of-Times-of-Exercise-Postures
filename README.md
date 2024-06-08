# System for Counting the Number of Times of Exercise Postures
![Screenshot 2024-04-25 155004](https://github.com/MeBruce/The-System-Helps-Count-the-Number-of-Exercise-Postures/assets/86824250/3e9df8c4-1a9a-4a7d-bfb2-557a01386e0b)

This project is created as a thesis for the completion of a Bachelor's degree in the Faculty of Engineering, Department of Computer Engineering.

# Step to use project

  1.pip install -r requirement.txt

For CUDA
  
  2.pip install torch==2.2.2+cu121 torchvision==0.17.2+cu121 torchaudio===2.2.2+cu121 -f https://download.pytorch.org/whl/torch_stable.html

  3.Donwload Model weight จาก link:https://atrmutrac-my.sharepoint.com/:f:/g/personal/1631010541133_outlook_rmutr_ac_th/Eh57BzwBmqZCt9riHW6n8icB897wrbeoGVheEAf3nv2cOQ?e=SJb4EW 
  แล้วนำไปใส่ใน folder model
  
  4.run test_use_cuda.py เพื่อ check ว่า device ของคุณลองรับ CUDA หรือยัง
  
  5.run home.py

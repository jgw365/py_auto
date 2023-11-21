# 使用前安装python包 ： pip3 install pyautogui
# 使用前安装terminator：sudo apt-get install terminator
# 使用时尽量不要动鼠标和键盘
# 刚体名字要对上 要改为英文输入法；
import pyautogui
import time
# 使用前需要更改
addr_auto_takeoff = "~/Desktop/auto_takeoff"
tty_name = 'ttyUSB0'
password = ' '
print("warning: \n1 english input\n2 body name\n3 terminator installed \n4 dont't move mouse and keyboard \n5 mocap is coming\n")
input('takeoff_address:'+addr_auto_takeoff)
input('tty_name:'+tty_name)
input('computer_password:'+password)

#保护措施，避免失控
pyautogui.FAILSAFE = True
#为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
pyautogui.PAUSE = 0.5
# 开始
pyautogui.hotkey('win','d')
# 打开终端
pyautogui.hotkey('ctrl','alt', 't')
# 开client 接受动捕数据 
# 使用前确保vrpn client 已经安装；动捕已经in 
pyautogui.write('roslaunch vrpn_client_ros sample.launch server:=10.1.1.198')
pyautogui.press('enter')

# 开启odometry
pyautogui.hotkey('ctrl','shift', 'e')


pyautogui.write('cd '+addr_auto_takeoff+'/VICON/')
pyautogui.press('enter')

pyautogui.write('catkin_make')
pyautogui.press('enter')
time.sleep(10)

pyautogui.write('source devel/setup.bash')
pyautogui.press('enter')
time.sleep(1)
# 刚体名字在这里可以更改
pyautogui.write('roslaunch odom_converter converter.launch')
pyautogui.press('enter')

# 开启mavros 
pyautogui.hotkey('ctrl','alt', 't')
pyautogui.write('sudo chmod 777 /dev/'+tty_name)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write(password)
pyautogui.press('enter')
pyautogui.write('roslaunch mavros px4.launch')
pyautogui.press('enter')
# 开启ekf 

pyautogui.hotkey('ctrl','shift', 'e')
pyautogui.write('cd '+addr_auto_takeoff+'/ekf/')
pyautogui.press('enter')
pyautogui.write('catkin_make')
pyautogui.press('enter')
time.sleep(10)

pyautogui.write('source devel/setup.bash')
pyautogui.press('enter')
time.sleep(1)

pyautogui.write('roslaunch ekf nokov.launch')
pyautogui.press('enter')

# 开启px4ctrl
pyautogui.hotkey('ctrl','shift', 'o')
pyautogui.write('cd '+addr_auto_takeoff+'/px4ctrl/')
pyautogui.press('enter')
pyautogui.write('catkin_make')
pyautogui.press('enter')
time.sleep(10)
pyautogui.write('source devel/setup.bash')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('roslaunch px4ctrl run_ctrl.launch')
pyautogui.press('enter')

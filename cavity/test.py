from pathlib import Path
import win32gui
import pyautogui as auto
import pygetwindow as gw


auto.FAILSAFE = False
#auto.mouseInfo()

p = Path(r"C:\Program Files\WindowsApps\king.com.CandyCrushSaga_1.2810.2.0_x64__kgqvnymyfvs32")


cc_win = gw.getWindowsWithTitle("Candy Crush Saga")[0]
cc_win.resizeTo(0, 0)  # 487, 674 might be max
cc_win.moveTo(0, 0)
print(cc_win.size)

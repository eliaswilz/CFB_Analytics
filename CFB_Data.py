import os, webbrowser, pyautogui, time, openpyxl
testList = ["acc"]
conf= ["acc","american","big-12","big-ten","cusa","independent","mac","mwc","pac-12","sec","sun-belt"]
confDict ={"acc":14, "american":12,"big-12":10,"big-ten":14,"cusa":14,"independent":4,"mac":12,"mwc":12,"pac-12":12,"sec":14,"sun-belt":12}
os.makedirs('cfb_data', exist_ok=True)
total = len(conf)
count = 0
resolution = str(pyautogui.size())
screenX = str(pyautogui.size())[1:5]
screenY = str(pyautogui.size())[7:10]

if screenX == "2560" and screenY == "108":
    for item in testList:
        scroll = confDict.get(item)
        webbrowser.open('https://www.sports-reference.com/cfb/conferences/'+item+'/2017.html')
        time.sleep(2.5)
        url = 'https://www.sports-reference.com/cfb/conferences/'+item+'/2017.html'
        print("Downloading "+item)
        pyautogui.moveTo(1457, 710, duration=0.2)
        time.sleep(.1)
        pyautogui.moveTo(1457, 802, duration=0.2)
        time.sleep(.1)
        pyautogui.click()
        pyautogui.scroll(int((scroll)/2)*-1)
        time.sleep(.1)
        pyautogui.moveTo(1287, 532, duration=0.2)
        pyautogui.dragTo(2000,800, duration=0.5)
        pyautogui.hotkey('command', 'c')
        pyautogui.moveTo(1645, 1045, duration=0.2)
        pyautogui.click()
        time.sleep(4)
        pyautogui.moveTo(51, 214, duration=0.2)
        pyautogui.click()
        pyautogui.hotkey('command', 'v')
        
        
        
        

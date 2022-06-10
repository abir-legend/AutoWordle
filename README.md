# AutoWordle

![](https://img.shields.io/github/stars/abir-legend/AutoWordle.svg) 
![](https://img.shields.io/github/forks/abir-legend/AutoWordle.svg) 
![](https://img.shields.io/github/tag/abir-legend/AutoWordle.svg) 
![](https://img.shields.io/github/release/abir-legend/AutoWordle.svg) 
![](https://img.shields.io/github/issues/abir-legend/AutoWordle.svg) 

**Things needed to run**
- [Python](https://www.python.org/ "get python from here")
- [pyautogui](https://pypi.org/project/PyAutoGUI/ "get pyautogui from here")

or just
  > pip install PyAutoGUI

**Adjustments For Screen optimisation**
since it uses pyautogui to read pixel color it might not work with displays that are not 1366x768 so to fix that take a full screen screenshot with <table><tr><td>windows key + shift + s</td></tr></table>
then use paint to fetch 
- x cords for each item in first row and
- y cords for each element in first column

take notes for the values and replace them in 
<details>
  <summary>
   WordleGod.py
  </summary>
    A bit misleading name since it can still fail 6% of the time
</details>


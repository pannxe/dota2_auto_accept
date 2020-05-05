import pyautogui as pag
import time

CHECK_INTERVAL = 1

CLICK_INTERVAL = 0.3
NUM_OF_CLICKS = 5

CONFIDENCE = 0.7
GRAYSCALE = True

def main():
    print("Dota 2 Auto Accept 1.0.0\nWritten by pannxe.\n")

    found = False
    print("Looking for accept-button-like object(s)...")
    while True:
        coors = pag.locateCenterOnScreen(
            "img/accept-en.png", grayscale=GRAYSCALE, confidence=CONFIDENCE
        )
        if coors == None:
            if found :
                pag.alert("Auto-accepted :D\nClick OK to continue.")
                print("Continue looking for accept-button-like object(s)...")
                found = False
            time.sleep(CHECK_INTERVAL)
        else:
            if found :
                print("Accept-button-like object does not seem to disappear.")
            found = True
            print("Found an accept-button-like object at\t{},\t{}".format(coors.x, coors.y))
            pag.click(
                x=coors.x,
                y=coors.y,
                interval=CHECK_INTERVAL,
                clicks=NUM_OF_CLICKS,
                button="left",
            )
            print("\t--> clicked.")

if __name__ == "__main__":
    main()

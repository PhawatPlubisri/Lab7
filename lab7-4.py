import RPi.GPIO as GPIO
import drivers
from time import sleep
display = drivers.Lcd()
display.lcd_clear()
SW1 = 27
SW2 = 17
lcd_position = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)
try:
 while True:
    if GPIO.event_detected(SW1):
      lcd_position += 1
      if lcd_position == 1:
        display.lcd_display_string("Jirajaet", 1)
        display.lcd_display_string("116510400643-2", 2)
        print(f"1")
      elif lcd_position == 2:
        display.lcd_display_string("Phawat  ", 1)
        display.lcd_display_string("116510400645-7", 2)
        print(f"2")
      elif lcd_position == 3:
        display.lcd_display_string("Siwawong", 1)
        display.lcd_display_string("116510400648-1", 2)
        print(f"3")
        lcd_position = 0
    elif GPIO.event_detected(SW2):
        display.lcd_clear()
        print(f"Bye!!")
except KeyboardInterrupt:
 GPIO.remove_event_detect(SW1)
 GPIO.remove_event_detect(SW2)
 GPIO.cleanup()
 print("\nBye...")

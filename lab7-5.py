import RPi.GPIO as GPIO
import drivers
from time import sleep
display = drivers.Lcd()
display.lcd_clear()
SW1 = 27
SW2 = 17
i = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)
my_array = ["LAB 7           ",\
     " LAB 7          ",\
     "  LAB 7         ",\
     "   LAB 7        ",\
     "    LAB 7       ",\
     "     LAB 7      ",\
     "      LAB 7     ",\
     "       LAB 7    ",\
     "        LAB 7   ",\
     "         LAB 7  ",\
     "          LAB 7 ",\
     "           LAB 7",\
]
try:
 while True:
    if GPIO.event_detected(SW1):
      i += 1
      if i <= 11:
        display.lcd_display_string(my_array[i], 1)
        print(i)
      else:
        i = 11
        display.lcd_display_string(my_array[i], 1)
        print(i)
    elif GPIO.event_detected(SW2):
      i -= 1
      if i >= 0:
        display.lcd_display_string(my_array[i], 1)
        print(i)
      else:
        i = 0
        display.lcd_display_string(my_array[i], 1)
        print(i)
except KeyboardInterrupt:
 GPIO.remove_event_detect(SW1)
 GPIO.remove_event_detect(SW2)
 GPIO.cleanup()
 print("\nBye...")

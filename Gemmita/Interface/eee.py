import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
import time
import psutil
    
def display_usage(cpu_usage,mem_usage,bars=50):
    cpu_use = (cpu_usage) 
    mem_use = (mem_usage/100.0)     
    print(cpu_use) 
    print(mem_use)

while True:
    display_usage(psutil.cpu_percent(),psutil.virtual_memory().percent,30)
    time.sleep(1.2)
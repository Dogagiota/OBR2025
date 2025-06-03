#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Criar objetos aqui.

ev3 = EV3Brick()
motor_d = Motor(Port.A)
motor_e = Motor(Port.D)
cor_d = ColorSensor(Port.S1)
cor_e = ColorSensor(Port.S4)

d_r, d_g, d_b = cor_d.rgb()
e_r, e_g, e_b = cor_e.rgb()
colore = cor_e.reflection()
colord = cor_d.reflection()
                        # verde 
# vermelho
v_r_min = 5
v_r_max = 15
# verde
v_g_min = 25
v_g_max = 36
# azul
v_b_min = 7 
v_b_max = 17
cor_d.color()
cor_e.color()
# funções
def segue_linha():
    if cor_e.color() == Color.BLACK and cor_d.color() == Color.BLACK:
        if cor_d.reflection() < (cor_e.reflection()-5):
                print(cor_d.reflection(), cor_e.reflection())
                motor_d.dc(20)
                motor_e.dc(-20)
        elif cor_d.reflection() > (cor_e.reflection()+5):
                print(cor_d.reflection(), cor_e.reflection())
                motor_d.dc(-20)
                motor_e.dc(20)
        else:
            motor_d.run_angle(500, -300, wait=False)
            motor_e.run_angle(500, -300, wait=False)
    elif cor_e.color() == Color.BLACK:
        motor_d.dc(-40)
        motor_e.dc(40)
    elif cor_d.color() == Color.BLACK:
        motor_d.dc(40)
        motor_e.dc(-40)
    else:
        motor_d.dc(-40)
        motor_e.dc(-40)

# Escreva o programa aqui.
wait(1000)
while True:
    if cor_d.color() == Color.RED and cor_e.color() == Color.RED:
        exit()
    """else:
    if ((r >= v_r_min and r <= v_r_max) and  cor_e.color() == Color.GREEN) and 
       ():
        motor_d.stop()
        motor_e.stop()
        motor_d.run_angle(500, -3000)
        motor_e.run_angle(500, -3000)
        wait(10000)
        exit()
    if e_r >= v_r_min and e_r <= v_r_max and e_g >= v_g_min and e_r <= v_g_max and e_b >= v_b_min and e_b <= v_b_max:
        motor_d.run_angle(-150, -200)
        motor_e.run_angle(300, -750)
    elif d_r >= v_r_min and d_r <= v_r_max and d_g >= v_g_min and d_r <= v_g_max and d_b >= v_b_min and d_b <= v_b_max :
        motor_d.run_angle(300, -750)
        motor_e.run_angle(-150, -200)
    else:"""
    segue_linha() aooooooooooooooooba
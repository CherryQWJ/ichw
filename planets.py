#!/usr/bin/env/python3

"""Planets.py: Description of how planets go.

__author__ = "QiuWeiJie"
__pkuid__  = "1800011802"
__email__  = "qiuweijie2000@pku.edu.cn"
"""
import turtle        
wn = turtle.Screen()
wn.bgcolor("black")

Sun=turtle.Turtle()
Sun.color("yellow")
Sun.shape("circle")
Sun.goto(0,0)

Mercury= turtle.Turtle()
Mercury.color("blue")
Mercury.shape("circle")
Mercury.penup()
Mercury.goto(0,-50)
Mercury.pendown()

Venus=turtle.Turtle()
Venus.color("green")
Venus.shape("circle")
Venus.penup()
Venus.goto(0,-100)
Venus.pendown()

Earth=turtle.Turtle()
Earth.color("grey")
Earth.shape("circle")
Earth.penup()
Earth.goto(0,-150)
Earth.pendown()

Mars=turtle.Turtle()
Mars.color("red")
Mars.shape("circle")
Mars.penup()
Mars.goto(0,-200)
Mars.pendown()

Jupiter=turtle.Turtle()
Jupiter.color("purple")
Jupiter.shape("circle")
Jupiter.penup()
Jupiter.goto(0,-250)
Jupiter.pendown()

Saturn=turtle.Turtle()
Saturn.color("brown")
Saturn.shape("circle")
Saturn.penup()
Saturn.goto(0,-300)
Saturn.pendown()


for i in range(10000):
    Mercury.circle(50,20)
    Venus.circle(100,15)
    Earth.circle(150,10)
    Mars.circle(200,6)
    Jupiter.circle(250,3)
    Saturn.circle(300,1)

#！/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import random
import math
import matplotlib.pyplot as plt 
from .validate import validate

__all__ = ['ball_in_box']

def ball_in_box(num_of_circle, blockers):
	circles=[]
	#初始化球的坐标和半径
	for tmp in range(num_of_circle):
		circles.append([0,0,0])
	
	#分100*100的点
	axis_x=np.linspace(-1+0.000001,1-0.000001,400)
	axis_y=np.linspace(-1+0.000001,1-0.000001,400)
	maycenters=[(x,y) for x in axis_x
				for y in axis_y]
	
	#print('1111',maycenters[0],maycenters[4])
	for index in range(num_of_circle):
		maxcir=[0,0,0]
		for maycenter in maycenters:
			x=maycenter[0]
			y=maycenter[1]
			cir=[x,y,0]
			cir=getCurrentSpotMaxCir(cir,index,circles,blockers)
			if cir[2]>maxcir[2]:
				maxcir=cir

		circles[index]=maxcir

		index+=1
	
	return circles
def getCurrentSpotMaxCir(circle,index,circles,blockers):
	min_r=0
	if (0==index):
		r1=dirCirAndBlocler(circle,blockers)
		r2=dirCirAndBounder(circle)
		r=min(r1,r2)
		circle[2]=r
		#print(circle[2])
		return circle
	else:
		r1=dirCirAndBlocler(circle,blockers)
		r2=dirCirAndBounder(circle)
		for i in range(index):
			r3=dirtCirAndCir(circles[i],circle)-circles[i][2]
			if min_r==0:
				min_r=r3
			min_r=min(min_r,r3)
		circle[2]=min(r1,r2,min_r)
		#print(circle[2])
		return circle

def dirtCirAndCir(circle1,circle2):
	dir=math.sqrt((circle1[0]-circle2[0])**2+(circle1[1]-circle2[1])**2)
	return dir
	
def dirCirAndBlocler(circle,blockers):
	mindir=0
	for i in range(len(blockers)):
		dir=math.sqrt((circle[0]-blockers[i][0])**2+(circle[1]-blockers[i][1])**2)
		if 0==mindir:
			mindir=dir
		mindir=min(dir,mindir)
	return mindir
	
def dirCirAndBounder(circle):
	r1=circle[0]+1
	r2=1-circle[0]
	r3=1-circle[1]
	r4=circle[1]+1
	return min(r1,r2,r3,r4)
		
def draw(blockers,circles):
	fig=plt.figure()
	ax=fig.gca()
	plt.xlim((-1,1))
	plt.ylim((-1,1))
	for i in blockers:
		plt.scatter(i[0],i[1],color='',marker='.',edgecolor='g',s=20)
	for i in circles:
		if len(i)==1:
			continue
		circle=plt.Circle((i[0],i[1]),i[2],color='r',fill=False)
		ax.add_artist(circle)
	plt.show()	
	
	
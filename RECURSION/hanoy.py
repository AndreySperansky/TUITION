def move(n, left) :
	print('Промежуточное значение для ' + str(n)  +  ' Значение left составляет ' + str(left) )
	if n == 0:
		return
	move(n-1, not left)

	""" После RETURN программа вываливается сюда со значением (n-1)+1, то есть, если было 0 то n будет 1"""

	if left:
		print(str(n) + ' <-- left')
	else:
		print(str(n) + ' --> right')

	""" Здесь программа начинает работать с узла на 1 уровень выше и снова опускается до 0 чтобы после этого
	 подняться на узел еще на 1 уровень выше"""

	move(n-1, not left)


n = int(input('Введите число дисков N: '))
move(n, True)


"""
В итоге программа работает следующим образом
move(4,true)
	move(3,false)
		move(2,true)
			move(1,false)	
				move(0,true) 					break
			(1) 					--> right
		(2)						<-- left
			move(1,false)	
				move(0,true) 					break
			(1) 					--> right
				
	(3)								--> right
		move(2,true)		
			move(1,false)	
				move(0,true) 					break			
			(1) 					--> right
				move(0,true) 		break	
		(2)						<-- left
			move(1,false)	
				move(0,true) 					break
			(1) 					--> right
				
(4)								<-- left
	move(3,false)
		move(2,true)
			move(1,false)	
				move(0,true) 					break
			(1) 					--> right
		(2)						<-- left
			move(1,false)	
				move(0,true) 					break
			(1) 					--> right
				
	(3)								--> right
		move(2,true)		
			move(1,false)	
				move(0,true) 					break			
			(1) 					--> right
				move(0,true) 		break	
		(2)						<-- left
			move(1,false)	
				move(0,true) 					break
			(1) 					--> right

"""

def findx(): 
	for x in range(1, 1000): 
		ls = [int(no) for no in str(x)]
		total = 0
		count = 0

		if len(ls) >= 2: 
			for i in range(2,x): 
				if not(x % i == 0): 
					if (str(x).find('1') == -1) and (str(x).find('7') == -1): 
						while count < len(ls): 
							for i in ls: 
								total += i
								count += 1
							if total <= 10: 		
								no = ls[0] + ls[1]
								if not (no % 2 == 0): 
									if  ls[-2] % 2 == 0: 			
										if ls[-1] == len(ls): 
											print(x)
		else: 
			continue
		
findx()
		

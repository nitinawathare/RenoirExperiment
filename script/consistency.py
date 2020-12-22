

def main():
	advs = [1/10,3/10,1/2]
	# cvalues = [1,2,4,10,25,60,100]
	cvalues = [60]
	pr={}
	ph={}
	pr_conditional_Delta = {}
	l = {}
	for c in range(0,len(cvalues)):
		Delta = pow(10,13)
		p = 1/(cvalues[c]*Delta)

		print(Delta)
		mu = 0.5
		p_Delta = pow((1-mu*p),Delta)
		pr["00"]=pr["10"] = 1- p_Delta
		pr["01"]=pr["11"] = p_Delta
		
		ph["0"] = 1- p_Delta
		ph["1"] = p_Delta

		prSum = 0
		for j in range(1, Delta+1):
			prSum = prSum+pow((1-mu*p),(j-1))*mu*p
		# print(prSum)

		looSum = 0
		for i in range(1, Delta+1):
			looSum = looSum+i*pow((1-mu*p),(i-1))*mu*p/prSum
		# print(looSum)
		l["00"] = looSum
		l["01"] = Delta
		l["11"] = Delta + (1/(mu*p))
		l["10"] = looSum + (1/(mu*p))


		finalSum = 0
		for i in range(0,2):
			for j in range(0,2):
				finalSum = finalSum+pr[str(i)+str(j)]*ph[str(i)]*l[str(i)+str(j)]
				print(l[str(i)+str(j)])
		# print(pow(p_Delta,2)/finalSum, (1-mu)*p*pow(10,5))


if __name__ == "__main__":
	main()

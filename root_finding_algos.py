#!/usr/bin/env python3
def bisect_method(f,a,b,tol): 
#finding root of the function f with the root inside (a,b)
#with given tolerence tol
	if f(a)==0:
		return(f(a))
	if f(b)==0:
		return(f(b))
	if f(a)*f(b)>=0:
		return("Incorrect range")
	else:
		err = abs(b-a)
		while err>tol:
			c = (a+b)/2
			if f(c)==0:
				return (c)
			elif f(a)*f(c)<0:
				b=c
			else:
				a=c
			err=abs(b-a)
	return (a)
		

def newt_raph(f, df, x0, tol):
#Newton Raphson method of finding root of function f
#with derivative df and initial estimate x0 and tolerence tol
	x_arr = []
	if df(x0)==0:
		return
	err = abs(f(x0)/df(x0))
	while err>tol:
		x1 = x0 - err
		x0 = x1
		x_arr.append(x1)
		if df(x0)==0:
			return
		err = abs(f(x0)/df(x0))
	return (x0, x_arr)



def hybrid(f, df, a, b, tol):
#Hybrid of Newton Raphson and Bisection method
#given range(a,b) inside which the root lies
    if abs(f(a))<tol:
    	return(a)
    elif abs(f(b))<tol:
        return(b)
    err = abs(a-b)
    if f(a)*f(b)>0:
        return("incorrect range")
    else:
        
        while err > tol:
            c = (a+b)/2
            if abs(f(c))<tol:
                return(c)

            elif f(c)*f(a)<0:
                b=c
            else:
                a=c
                err = abs(f(c))
            if df(c)==0:
                continue
            else:
                err = abs(f(c)/df(c))
                x0 = c
                while err > tol:
                    
                    x1 = x0 - f(x0)/df(x0)
                    if abs(f(x1))<tol:
                        return (x1)
                    if df(x1)==0 or (abs(2*f(x1)) > ((x1-x0)*df(x1))) or x1>=b or x1<=a:
                        break
                    if np.sign(f(a))==np.sign(f(x1)):
                        a = x1
                    else:
                        b=x1
                    x0 = x1
                    err = abs(f(x1)/df(x1))
        return(x1)



def secant(f, x0, x1, tol):
#secant method of finding root of function f
	err = abs(f(x1))
	while err>tol:
		sec = abs((f(x1)-f(x0))/(x1-x0))
		if sec == 0:
			return
		x2 = x1 - f(x1)/sec
		x0 = x1
		x1 = x2
		err = f(x1)
	return(x1)
	
	

def brute_force(f,a,b):
#brute force method of finding approximate intervals where roots exist
#given the range (a,b)
    x = np.linspace(a,b,1000)
    intervals = np.array([])
    for i in range(1000-1):
        if f(x[i])*f(x[i+1])<0:
            if len(intervals)==0:
                intervals = np.array([x[i],x[i+1]])
            else:
                intervals = np.vstack((intervals,np.array([x[i],x[i+1]])))
    return(intervals)



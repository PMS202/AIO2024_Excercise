import math
import random

# 1. Viết function thực hiện đánh giá classification model bằng F1-Score.

def Calc_F1_Score ( tp, fp, fn):
    # Check data type of tp,fp,fn
    if type(tp) != int or type(fp) != int or type(fn) != int:
        print("tp and fp and fn must be int")
        return
    
    # Check tp,fp,fn > 0
    if tp > 0 or fp > 0 or fn > 0:
        print("tp and fp and fn must be greater than zero")
        return
    precision = tp / ( tp + fp )
    recall = tp / ( tp + fn )
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    print(f'Precision is {precision}')
    print(f'Recall is {recall}')
    print(f'F1_Score is {f1_score}')

    # 2. Viết function mô phỏng theo 3 activation function.
def is_number ( n ) :
    try :
        float ( n )     # Type - casting the string to ‘float ‘.
                        # If string is not a valid ‘float ‘ ,
                        # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    return True

def Calc_Activ_Func ():

    # Input x and check type data
    while True:
        x = input("Input x: ")
        if is_number(x) == False:
            print("x is not a number")
        else: break
    x = float(x)

    # Choose activation function
    while True:
        print("Activation: \n sigmoid \n relu \n elu ")
        activ_func = input("Choose activation function: ")
        print(type(activ_func))
        if activ_func == "sigmoid" or activ_func == "relu" or activ_func == "elu":
             break
        else: print(f"{activ_func} is not supported")

    # Calculation
    if activ_func == "sigmoid":
        y = 1 / ( 1 + math.e**(-x))
    elif activ_func == 'relu':
        if x <= 0:
            y = 0
        else:
            y = x
    elif activ_func == 'elu':
        if x <= 0:
            alpha = 0.01
            y = alpha * ( math.e**(x) - 1 )
        else:
            y = x
    print(f"{activ_func} f({x}) = {y}")
    return y


# 3. Viết function lựa chọn regression loss function để tính loss:

def regression_loss( num_sample, loss_name ):
    # Check if num_sample is a integer and > 0
    if num_sample.isnumeric() == False and int( num_sample ) > 0:
        print("Number of samples must be an integer numbera and must be greater than zero ")
        return
    num_sample = int( num_sample )

    loss=0
    for i in range(num_sample):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)

        if loss_name == 'MAE': 
            loss = loss + abs( target - predict ) # Mean Absolute Error
        elif loss_name== 'MSE':
            loss = loss + ( target - predict )**2
        else:
            print(f"Unknown loss name: {loss_name}")  # Mean Squared Error
            return

        print(f'Loss name: {loss_name}')
        print(f'Sample: {i + 1}')
        print(f'Prediction: {predict}')
        print(f'Target: {target}')
        print(f'Accumulated loss: {loss}')

    final_loss = loss * (1 / num_sample)
    print(f'final_loss: {final_loss}')

# 4. Viết 4 functions để ước lượng các hàm số sau.
def factorial( n ):
	result = 1
	for i in range( n ):
		result = result * ( i + 1 )
	return result
	
	
def approx_sin( x, n ):
	result = 0
	for i in range( n + 1 ):
		result = result + ( (-1)**i ) * ( x**( 2*i+1 ) ) / factorial( 2 * i + 1 )
	print(f'sin: {result}')
	return result

def approx_cos( x, n ):
	result = 0
	for i in range( n + 1 ):
		result = result + ( (-1)**i ) * ( x**( 2*i ) ) / factorial( 2*i )
	print(f'cos: {result}')
	return result
	
def approx_sinh( x, n ):
	result = 0
	for i in range( n + 1) :
		result = result + ( x**( 2*i+1 ) ) / factorial( 2*i+1 )
	print(f'sinh: {result}')
	return result
	
def approx_cosh( x, n ):
	result = 0
	for i in range( n + 1 ):
		result = result + ( x**(2*i) ) / factorial( 2*i )
	print(f'cosh: {result}')
	return result

# 5. Viết function thực hiện Mean Difference of nth Root Error:
def md_nre_single_sample (y , y_hat , n , p) :
    y_root = y ** (1/ n )
    y_hat_root = y_hat ** (1/ n )
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss
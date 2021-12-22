# ninput
gives options to input integers and floats easier 

# functions

int_input and float_input could be used for getting int or float from user without problems with converting or exceptions. Functions check type of input and if it`s not expected ones there gives message and try to again get number from user until he enter valid data.

le_int_input and le_float_input is int and float input but user have to enter number that is less or equal than 
number that programmer give in argument if user type greater one function will ask again until he enter less or equal to expected number.

lt_int_input and lt_float_input is int and float input but user have to enter number that is less than 
number that programmer give in argument if user type greater or equal one function will ask again until he enter less to expected number.

ge_int_input and ge_float_input is int and float input but user have to enter number that is great or equal than 
number that programmer give in argument if other case program will ask again until user enter great or equal number.

gt_int_input and gt_float_input is int and float input but user have to enter number that is great than 
number that programmer give in argument if other case program will ask again until user enter great number.

be_int_input and be_float_input is int and float input but user have to enter number that is between or equal than 
number that programmer give in argument

bt_int_input and bt_float_input is int and float input but user have to enter number that is between than 
number that programmer give in argument

bet_int_input and bet_float_input is int and float input but user have to enter number that is great or equal than first number and lower than 
second number that programmer gives in argument

bte_int_input and bte_float_input is is int and float input but user have to enter number that is great than first number and lower or equal than 
second number that programmer gives in argument

ne_int_input and ne_float_input is int and float input but user have to enter number that is not equal to number that programmer gives in argument

positive_int_input and positive_float_input is is int and float input but user have to enter positive number

negative_int_input and negative_float_input is is int and float input but user have to enter positive number


# Params
:param than: numbers that input number must be less, great, between or not equal. In not equal param named to. In between case
you should give tuple or list. Doesn`t exist in int_input, float_input, positive_int_input, positive_float_input, 
negative_int_input and negative_float_input

:param text: text that shows on input. default ''

:param error_text: text that show in case if equation is False and error_text_bool is True; In int_input, float_input is the same to error_text_input

:param error_text_format_bool: if True shows formated error text; Doesn`t exist in int_input, float_input

:param error_text_format: formated error text; Doesn`t exist in int_input, float_input

:param pause:if set True pause program until Enter is pressed default True; in int_input, float_input is the same to error_text_input 

:param pause_text_bool:if True shows text in pause; in int_input, float_input is the same to error_text_input 

:param pause_text:What shows on pause; in int_input, float_input is the same to error_text_input 

:param clear: if True clear console; in int_input, float_input is the same to error_text_input 

:param error_text_input:text that shows on error case -> if cant convert into int; Doesn`t exist in int_input, float_input

:param pause_input:same as pause but in inputing; Doesn`t exist in int_input, float_input

:param pause_input_text_bool:same as pause_text_bool but in inputing; Doesn`t exist in int_input, float_input

:param pause_input_text:same as pause_text but in inputing; Doesn`t exist in int_input, float_input

:param clear_input:same as clear but in inputing; Doesn`t exist in int_input, float_input

:param error_text_bool: if true shows error text if equation isnt true; in int_input, float_input is the same to error_text_input 

:param error_text_input_bool: same as error_text_bool but in inputing; Doesn`t exist in int_input, float_input

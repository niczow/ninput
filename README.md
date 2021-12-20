# ninput
gives options to input integers and floats easier 

# functions

int_input and float_input are using to inputs that types of numbers functions if somebody input other type of object 
gives in option to show text informing that it`s not that type then in option gives to pause untill press enter
then in option gives to clear console and again ask to input

le_int_input and le_float_input is int and float input but user have to input number that is less or equal than 
number that programmer give in argument

lt_int_input and lt_float_input is int and float input but user have to input number that is less than 
number that programmer give in argument

ge_int_input and ge_float_input is int and float input but user have to input number that is giger or equal than 
number that programmer give in argument

gt_int_input and gt_float_input is int and float input but user have to input number that is giger than 
number that programmer give in argument

be_int_input and be_float_input is int and float input but user have to input number that is between or equal than 
number that programmer give in argument

bt_int_input and bt_float_input is int and float input but user have to input number that is between than 
number that programmer give in argument

bet_int_input and bet_float_input is int and float input but user have to input number that is giger or equal than first number and lower than 
second number that programmer gives in argument

bte_int_input and bte_float_input is is int and float input but user have to input number that is gigerthan first number and lower or equal than 
second number that programmer gives in argument

ne_int_input and ne_float_input is int and float input but user have to input number that is not equal to number that programmer gives in argument

positive_int_input and positive_float_input is is int and float input but user have to input positive number

negative_int_input and negative_float_input is is int and float input but user have to input positive number


# Params
:param than: numbers that input number must be lower, giger, between or not equal in not equal param named to in between case
you should give tuple or list dont exist in int_input, float_input, positive_int_input, positive_float_input, 
negative_int_input and negative_float_input

:param text: text that shows on input default ''

:param error_text: text that show in case if equation if False and error_text_bool is True; in int_input, float_input is the same to error_text_input

:param error_text_format_bool: if True shows formated error text; dont exist in int_input, float_input

:param error_text_format: formated error text dont exist in int_input, float_input

:param pause:if set True pause program until Enter is pressed default True; in int_input, float_input is the same to error_text_input 

:param pause_text_bool:if True shows text in pause; in int_input, float_input is the same to error_text_input 

:param pause_text:What shows on pause; in int_input, float_input is the same to error_text_input 

:param clear: if True clear console; in int_input, float_input is the same to error_text_input 

:param error_text_input:text that shows on error case -> if cant convert into int; dont exist in int_input, float_input

:param pause_input:same as pause but in inputing; dont exist in int_input, float_input

:param pause_input_text_bool:same as pause_text_bool but in inputing; dont exist in int_input, float_input

:param pause_input_text:same as pause_text but in inputing; dont exist in int_input, float_input

:param clear_input:same as clear but in inputing; dont exist in int_input, float_input

:param error_text_bool: if true shows error text if equation isnt true; in int_input, float_input is the same to error_text_input 

:param error_text_input_bool: same as error_text_bool but in inputing; dont exist in int_input, float_input

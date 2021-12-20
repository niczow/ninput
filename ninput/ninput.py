import os


def _input_num(num_type, text='', error_text_bool=True, pause=True,
               pause_text_bool=True, error_text="",
               pause_text='Press Enter...', clear=True):
    """
        function take an input and convert it to type that user want
        :param num_type: type to input
        :param text: text that shows in input default= ''
        :param error_text_bool: bool to show error text or not
        :param error_text: text that show in case of error bool is true
        :param pause: bool to pause for a while
        :param pause_text_bool: bool to show text op pause
        :param pause_text: text show on pause
        :param clear: bool to clear cmd
        :return: number
        """
    while True:
        try:
            number = num_type(input(text))
        except (Exception,):
            if error_text_bool:
                print(error_text)
            if pause:
                if pause_text_bool:
                    input(pause_text)
            if clear:
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            return number


def _if_error(to, error_text_format_bool, error_text_format,
              error_text, pause, pause_text_bool, pause_text, clear,
              error_text_bool):
    """
    printing errors if isn`t true
    :param error_text_bool: if true the error text will show
    :param to: to what number is equality
    :param error_text_format_bool: bool that want formatted error text
    :param error_text_format: formatted error text
    :param error_text: error text
    :param pause: bool that want a pause
    :param pause_text_bool: bool that want a pause text
    :param pause_text: pause text
    :param clear: bool to clear cmd
    :return: nothing
    """
    if error_text_bool:
        if error_text_format_bool:
            print(error_text_format.format(to))
        else:
            print(error_text)
    if pause:
        if pause_text_bool:
            input(pause_text)
        else:
            input()
    if clear:
        os.system('cls' if os.name == 'nt' else 'clear')


def _ee_num_input(num_type, than, eq, text='', error_text="", error_text_format_bool=True,
                  error_text_format="", pause=True, pause_text_bool=True,
                  pause_text='Press Enter...', clear=True, error_text_input="Enter number!",
                  pause_input=True, pause_input_text_bool=True, pause_input_text=True,
                  clear_input=True, error_text_bool=True, error_text_input_bool=True,
                  func=(_input_num, _if_error)):
    """
        :param func:
        :param eq: type of equality
        :param error_text_format_bool:
        :param error_text_format:
        :param error_text_input_bool:
        :param num_type: type to input
        :param text: text that shows in input default= ''
        :param error_text_bool: bool to show error text or not
        :param error_text: text that show in case of error bool is true
        :param pause: bool to pause for a while
        :param pause_text_bool: bool to show text op pause
        :param pause_text: text show on pause
        :param clear: bool to clear cmd
        :param than: number that input number must be equality
        :param error_text_input: error_text_bool but in input
        :param pause_input: pause but in input
        :param pause_input_text_bool: pause_text_bool but in input
        :param pause_input_text: pause_text but in input
        :param clear_input: bool to clear cmd in input but in input
        :return: number
        """
    while True:
        number = func[0](num_type, text=text, error_text=error_text_input, pause=pause_input,
                         pause_text_bool=pause_input_text_bool, pause_text=pause_input_text,
                         clear=clear_input, error_text_bool=error_text_input_bool)

        if eq == "==":
            if number == than:
                func[1](to=than, error_text_format_bool=error_text_format_bool,
                        error_text_format=error_text_format, error_text=error_text,
                        pause=pause, pause_text_bool=pause_text_bool,
                        pause_text=pause_text, clear=clear, error_text_bool=error_text_bool)
            else:
                return number
        elif eq == "<":
            if number < than:
                func[1](to=than, error_text_format_bool=error_text_format_bool,
                        error_text_format=error_text_format, error_text=error_text,
                        pause=pause, pause_text_bool=pause_text_bool,
                        pause_text=pause_text, clear=clear, error_text_bool=error_text_bool)
            else:
                return number
        elif eq == "<=":
            if number <= than:
                func[1](to=than, error_text_format_bool=error_text_format_bool,
                        error_text_format=error_text_format, error_text=error_text,
                        pause=pause, pause_text_bool=pause_text_bool,
                        pause_text=pause_text, clear=clear, error_text_bool=error_text_bool)
            else:
                return number
        elif eq == ">":
            if number > than:
                func[1](to=than, error_text_format_bool=error_text_format_bool,
                        error_text_format=error_text_format, error_text=error_text,
                        pause=pause, pause_text_bool=pause_text_bool,
                        pause_text=pause_text, clear=clear, error_text_bool=error_text_bool)
            else:
                return number
        elif eq == ">=":
            if number >= than:
                func[1](to=than, error_text_format_bool=error_text_format_bool,
                        error_text_format=error_text_format, error_text=error_text,
                        pause=pause, pause_text_bool=pause_text_bool,
                        pause_text=pause_text, clear=clear, error_text_bool=error_text_bool)
            else:
                return number

        elif eq == "<<":
            if not than[0] < number < than[1]:
                func[1](to=than, error_text_format_bool=error_text_format_bool,
                        error_text_format=error_text_format, error_text=error_text,
                        pause=pause, pause_text_bool=pause_text_bool,
                        pause_text=pause_text, clear=clear, error_text_bool=error_text_bool)
            else:
                return number

        elif eq == "<=<":
            if not than[0] <= number < than[1]:
                func[1](to=than, error_text_format_bool=error_text_format_bool,
                        error_text_format=error_text_format, error_text=error_text,
                        pause=pause, pause_text_bool=pause_text_bool,
                        pause_text=pause_text, clear=clear, error_text_bool=error_text_bool)
            else:
                return number

        elif eq == "<<=":
            if not than[0] < number <= than[1]:
                func[1](to=than, error_text_format_bool=error_text_format_bool,
                        error_text_format=error_text_format, error_text=error_text,
                        pause=pause, pause_text_bool=pause_text_bool,
                        pause_text=pause_text, clear=clear, error_text_bool=error_text_bool)
            else:
                return number

        elif eq == "<=<=":
            if not than[0] <= number <= than[1]:
                func[1](to=than, error_text_format_bool=error_text_format_bool,
                        error_text_format=error_text_format, error_text=error_text,
                        pause=pause, pause_text_bool=pause_text_bool,
                        pause_text=pause_text, clear=clear, error_text_bool=error_text_bool)
            else:
                return number


def _lt_num_input(num_type, than, func=_ee_num_input, text='', error_text="Enter number less than ",
                  error_text_format_bool=True, error_text_format="Enter number less than {}", error_text_bool=True,
                  pause=True, pause_text_bool=True,
                  pause_text='Press Enter...', clear=True, error_text_input="Enter number!",
                  pause_input=True, pause_input_text_bool=True, pause_input_text=True, clear_input=True,
                  error_text_input_bool=True):
    """
    :param func:
    :param error_text_format_bool:
    :param error_text_format:
    :param error_text_input_bool:
    :param num_type: type to input
    :param text: text that shows in input default= ''
    :param error_text_bool: bool to show error text or not
    :param error_text: text that show in case of error bool is true
    :param pause: bool to pause for a while
    :param pause_text_bool: bool to show text op pause
    :param pause_text: text show on pause
    :param clear: bool to clear cmd
    :param than: number that input number must be less
    :param error_text_input: error_text_bool but in input
    :param pause_input: pause but in input
    :param pause_input_text_bool: pause_text_bool but in input
    :param pause_input_text: pause_text but in input
    :param clear_input: bool to clear cmd in input but in input
    :return: number
    """
    return func(num_type=num_type, eq='>=', than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool,
                error_text_format=error_text_format, pause=pause, pause_text_bool=pause_text_bool,
                pause_text=pause_text, clear=clear, error_text_input=error_text_input,
                pause_input=pause_input, pause_input_text_bool=pause_input_text_bool,
                pause_input_text=pause_input_text, clear_input=clear_input,
                error_text_bool=error_text_bool, error_text_input_bool=error_text_input_bool)


def _le_num_input(num_type, than, func=_ee_num_input, text='', error_text="Enter number less or equal than ",
                  error_text_format_bool=True,
                  error_text_format="Enter number less or equal than {}", pause=True, pause_text_bool=True,
                  pause_text='Press Enter...', clear=True, error_text_input="Enter number!",
                  pause_input=True, pause_input_text_bool=True, pause_input_text=True, clear_input=True,
                  error_text_bool=True, error_text_input_bool=True):
    """
        :param func:
        :param error_text_format_bool:
        :param error_text_format:
        :param error_text_input_bool:
        :param num_type: type to input
        :param text: text that shows in input default= ''
        :param error_text_bool: bool to show error text or not
        :param error_text: text that show in case of error bool is true
        :param pause: bool to pause for a while
        :param pause_text_bool: bool to show text op pause
        :param pause_text: text show on pause
        :param clear: bool to clear cmd
        :param than: number that input number must be less or equal
        :param error_text_input: error_text_bool but in input
        :param pause_input: pause but in input
        :param pause_input_text_bool: pause_text_bool but in input
        :param pause_input_text: pause_text but in input
        :param clear_input: bool to clear cmd in input but in input
        :return: number
        """
    return func(num_type=num_type, eq='>', than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool,
                error_text_format=error_text_format, pause=pause, pause_text_bool=pause_text_bool,
                pause_text=pause_text, clear=clear, error_text_input=error_text_input,
                pause_input=pause_input, pause_input_text_bool=pause_input_text_bool,
                pause_input_text=pause_input_text, clear_input=clear_input,
                error_text_bool=error_text_bool, error_text_input_bool=error_text_input_bool)


def _gt_num_input(num_type, than, func=_ee_num_input, text='', error_text="Enter number great than ",
                  error_text_format_bool=True, error_text_format="Enter number great than {}", pause=True,
                  pause_text_bool=True, pause_text='Press Enter...', clear=True, error_text_input="Enter number!",
                  pause_input=True, pause_input_text_bool=True, pause_input_text=True, clear_input=True,
                  error_text_bool=True, error_text_input_bool=True):
    """
        :param func:
        :param error_text_format_bool:
        :param error_text_format:
        :param error_text_input_bool:
        :param num_type: type to input
        :param text: text that shows in input default= ''
        :param error_text_bool: bool to show error text or not
        :param error_text: text that show in case of error bool is true
        :param pause: bool to pause for a while
        :param pause_text_bool: bool to show text op pause
        :param pause_text: text show on pause
        :param clear: bool to clear cmd
        :param than: number that input number must be great
        :param error_text_input: error_text_bool but in input
        :param pause_input: pause but in input
        :param pause_input_text_bool: pause_text_bool but in input
        :param pause_input_text: pause_text but in input
        :param clear_input: bool to clear cmd in input but in input
        :return: number
        """
    return func(num_type=num_type, eq='<=', than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool,
                error_text_format=error_text_format, pause=pause, pause_text_bool=pause_text_bool,
                pause_text=pause_text, clear=clear, error_text_input=error_text_input,
                pause_input=pause_input, pause_input_text_bool=pause_input_text_bool,
                pause_input_text=pause_input_text, clear_input=clear_input,
                error_text_bool=error_text_bool, error_text_input_bool=error_text_input_bool)


def _ge_num_input(num_type, than, func=_ee_num_input, text='', error_text="Enter number great or equal than ",
                  error_text_format_bool=True,
                  error_text_format="Enter number great or equal than {}", pause=True, pause_text_bool=True,
                  pause_text='Press Enter...', clear=True, error_text_input="Enter number!",
                  pause_input=True, pause_input_text_bool=True, pause_input_text=True, clear_input=True,
                  error_text_bool=True, error_text_input_bool=True):
    """
        :param func:
        :param error_text_format_bool:
        :param error_text_format:
        :param error_text_input_bool:
        :param num_type: type to input
        :param text: text that shows in input default= ''
        :param error_text_bool: bool to show error text or not
        :param error_text: text that show in case of error bool is true
        :param pause: bool to pause for a while
        :param pause_text_bool: bool to show text op pause
        :param pause_text: text show on pause
        :param clear: bool to clear cmd
        :param than: number that input number must be great or equal
        :param error_text_input: error_text_bool but in input
        :param pause_input: pause but in input
        :param pause_input_text_bool: pause_text_bool but in input
        :param pause_input_text: pause_text but in input
        :param clear_input: bool to clear cmd in input but in input
        :return: number
        """
    return func(num_type=num_type, eq='<', than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool,
                error_text_format=error_text_format, pause=pause, pause_text_bool=pause_text_bool,
                pause_text=pause_text, clear=clear, error_text_input=error_text_input,
                pause_input=pause_input, pause_input_text_bool=pause_input_text_bool,
                pause_input_text=pause_input_text, clear_input=clear_input,
                error_text_bool=error_text_bool, error_text_input_bool=error_text_input_bool)


def _be_num_input(num_type, than, func=_ee_num_input, text='', error_text="Enter number great or equal than ",
                  error_text_format_bool=True,
                  error_text_format="Enter number great or equal than {}", pause=True, pause_text_bool=True,
                  pause_text='Press Enter...', clear=True, error_text_input="Enter number!",
                  pause_input=True, pause_input_text_bool=True, pause_input_text=True, clear_input=True,
                  error_text_bool=True, error_text_input_bool=True):
    """
        :param func:
        :param error_text_format_bool:
        :param error_text_format:
        :param error_text_input_bool:
        :param num_type: type to input
        :param text: text that shows in input default= ''
        :param error_text_bool: bool to show error text or not
        :param error_text: text that show in case of error bool is true
        :param pause: bool to pause for a while
        :param pause_text_bool: bool to show text op pause
        :param pause_text: text show on pause
        :param clear: bool to clear cmd
        :param than: number that input number must be great or equal
        :param error_text_input: error_text_bool but in input
        :param pause_input: pause but in input
        :param pause_input_text_bool: pause_text_bool but in input
        :param pause_input_text: pause_text but in input
        :param clear_input: bool to clear cmd in input but in input
        :return: number
        """
    return func(num_type=num_type, eq='<=<=', than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool,
                error_text_format=error_text_format, pause=pause, pause_text_bool=pause_text_bool,
                pause_text=pause_text, clear=clear, error_text_input=error_text_input,
                pause_input=pause_input, pause_input_text_bool=pause_input_text_bool,
                pause_input_text=pause_input_text, clear_input=clear_input,
                error_text_bool=error_text_bool, error_text_input_bool=error_text_input_bool)


def _bet_num_input(num_type, than, func=_ee_num_input, text='', error_text="Enter number great or equal than ",
                   error_text_format_bool=True,
                   error_text_format="Enter number great or equal than {}", pause=True, pause_text_bool=True,
                   pause_text='Press Enter...', clear=True, error_text_input="Enter number!",
                   pause_input=True, pause_input_text_bool=True, pause_input_text=True, clear_input=True,
                   error_text_bool=True, error_text_input_bool=True):
    """
        :param func:
        :param error_text_format_bool:
        :param error_text_format:
        :param error_text_input_bool:
        :param num_type: type to input
        :param text: text that shows in input default= ''
        :param error_text_bool: bool to show error text or not
        :param error_text: text that show in case of error bool is true
        :param pause: bool to pause for a while
        :param pause_text_bool: bool to show text op pause
        :param pause_text: text show on pause
        :param clear: bool to clear cmd
        :param than: number that input number must be great or equal
        :param error_text_input: error_text_bool but in input
        :param pause_input: pause but in input
        :param pause_input_text_bool: pause_text_bool but in input
        :param pause_input_text: pause_text but in input
        :param clear_input: bool to clear cmd in input but in input
        :return: number
        """
    return func(num_type=num_type, eq='<=<', than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool,
                error_text_format=error_text_format, pause=pause, pause_text_bool=pause_text_bool,
                pause_text=pause_text, clear=clear, error_text_input=error_text_input,
                pause_input=pause_input, pause_input_text_bool=pause_input_text_bool,
                pause_input_text=pause_input_text, clear_input=clear_input,
                error_text_bool=error_text_bool, error_text_input_bool=error_text_input_bool)


def _bte_num_input(num_type, than, func=_ee_num_input, text='', error_text="Enter number great or equal than ",
                   error_text_format_bool=True,
                   error_text_format="Enter number great or equal than {}", pause=True, pause_text_bool=True,
                   pause_text='Press Enter...', clear=True, error_text_input="Enter number!",
                   pause_input=True, pause_input_text_bool=True, pause_input_text=True, clear_input=True,
                   error_text_bool=True, error_text_input_bool=True):
    """
        :param func:
        :param error_text_format_bool:
        :param error_text_format:
        :param error_text_input_bool:
        :param num_type: type to input
        :param text: text that shows in input default= ''
        :param error_text_bool: bool to show error text or not
        :param error_text: text that show in case of error bool is true
        :param pause: bool to pause for a while
        :param pause_text_bool: bool to show text op pause
        :param pause_text: text show on pause
        :param clear: bool to clear cmd
        :param than: number that input number must be great or equal
        :param error_text_input: error_text_bool but in input
        :param pause_input: pause but in input
        :param pause_input_text_bool: pause_text_bool but in input
        :param pause_input_text: pause_text but in input
        :param clear_input: bool to clear cmd in input but in input
        :return: number
        """
    return func(num_type=num_type, eq='<<=', than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool,
                error_text_format=error_text_format, pause=pause, pause_text_bool=pause_text_bool,
                pause_text=pause_text, clear=clear, error_text_input=error_text_input,
                pause_input=pause_input, pause_input_text_bool=pause_input_text_bool,
                pause_input_text=pause_input_text, clear_input=clear_input,
                error_text_bool=error_text_bool, error_text_input_bool=error_text_input_bool)


def _bt_num_input(num_type, than, func=_ee_num_input, text='', error_text="Enter number great or equal than ",
                  error_text_format_bool=True,
                  error_text_format="Enter number great or equal than {}", pause=True, pause_text_bool=True,
                  pause_text='Press Enter...', clear=True, error_text_input="Enter number!",
                  pause_input=True, pause_input_text_bool=True, pause_input_text=True, clear_input=True,
                  error_text_bool=True, error_text_input_bool=True):
    """
        :param func:
        :param error_text_format_bool:
        :param error_text_format:
        :param error_text_input_bool:
        :param num_type: type to input
        :param text: text that shows in input default= ''
        :param error_text_bool: bool to show error text or not
        :param error_text: text that show in case of error bool is true
        :param pause: bool to pause for a while
        :param pause_text_bool: bool to show text op pause
        :param pause_text: text show on pause
        :param clear: bool to clear cmd
        :param than: number that input number must be great or equal
        :param error_text_input: error_text_bool but in input
        :param pause_input: pause but in input
        :param pause_input_text_bool: pause_text_bool but in input
        :param pause_input_text: pause_text but in input
        :param clear_input: bool to clear cmd in input but in input
        :return: number
        """
    return func(num_type=num_type, eq='<<', than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool,
                error_text_format=error_text_format, pause=pause, pause_text_bool=pause_text_bool,
                pause_text=pause_text, clear=clear, error_text_input=error_text_input,
                pause_input=pause_input, pause_input_text_bool=pause_input_text_bool,
                pause_input_text=pause_input_text, clear_input=clear_input,
                error_text_bool=error_text_bool, error_text_input_bool=error_text_input_bool)


def _ne_num_input(num_type, to, func=_ee_num_input, text='', error_text="Enter integer number negative to ",
                  error_text_format_bool=True,
                  error_text_format="Enter integer number negative to {}", pause=True, pause_text_bool=True,
                  pause_text='Press Enter...', clear=True, error_text_input="Enter number!",
                  pause_input=True, pause_input_text_bool=True, pause_input_text=True, clear_input=True,
                  error_text_bool=True, error_text_input_bool=True):
    """
        :param func:
        :param error_text_format_bool:
        :param error_text_format:
        :param error_text_input_bool:
        :param num_type: type to input
        :param text: text that shows in input default= ''
        :param error_text_bool: bool to show error text or not
        :param error_text: text that show in case of error bool is true
        :param pause: bool to pause for a while
        :param pause_text_bool: bool to show text op pause
        :param pause_text: text show on pause
        :param clear: bool to clear cmd
        :param to: number that input number must be negative
        :param error_text_input: error_text_bool but in input
        :param pause_input: pause but in input
        :param pause_input_text_bool: pause_text_bool but in input
        :param pause_input_text: pause_text but in input
        :param clear_input: bool to clear cmd in input but in input
        :return: number
        """
    return func(num_type=num_type, eq='==', than=to, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool,
                error_text_format=error_text_format, pause=pause, pause_text_bool=pause_text_bool,
                pause_text=pause_text, clear=clear, error_text_input=error_text_input,
                pause_input=pause_input, pause_input_text_bool=pause_input_text_bool,
                pause_input_text=pause_input_text, clear_input=clear_input,
                error_text_bool=error_text_bool, error_text_input_bool=error_text_input_bool)


def int_input(text='', error_text_bool=True, error_text="Input integer number!!", pause=True, pause_text_bool=True,
              pause_text='Press Enter...', clear=True, func=_input_num):
    """
    function get input and safety convert it into int
    :param text: text that shows on input default ''
    :param error_text_bool: if set True shows text if get error default True
    :param error_text: text that shows on error case -> if cant convert into int
    :param pause: if set True pause program until Enter is pressed default True
    :param pause_text_bool: if True shows text in pause
    :param pause_text: What shows on pause
    :param clear: if True clear console
    :return: integer that user write
    """
    return func(int, text=text, error_text_bool=error_text_bool, error_text=error_text,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear)


def float_input(text='', error_text_bool=True, error_text="Input float number!!", pause=True, pause_text_bool=True,
                pause_text='Press Enter...', clear=True, func=_input_num):
    """
        function get input and safety convert it into float
        :param text: text that shows on input default ''
        :param error_text_bool: if set True shows text if get error default True
        :param error_text: text that shows on error case -> if cant convert into int
        :param pause: if set True pause program until Enter is pressed default True
        :param pause_text_bool: if True shows text in pause
        :param pause_text: What shows on pause
        :param clear: if True clear console
        :return: float that user write
        """
    return func(float, text=text, error_text_bool=error_text_bool, error_text=error_text,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear)


def lt_int_input(than, text='', error_text="Enter integer number less than ", error_text_format_bool=True,
                 error_text_format="Enter integer number less than {}", pause=True, pause_text_bool=True,
                 pause_text='Press Enter...', clear=True, error_text_input="Enter integer number!",
                 pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                 error_text_bool=True, error_text_input_bool=True, func=_lt_num_input):
    """
    function get input and safety convert it into int next test that number is lower than 'than' if yes return it
    :param than: number that input number must be lower
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: integer number lower than 'than'
    """
    return func(int, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def lt_float_input(than, text='', error_text="Enter number less than ", error_text_format_bool=True,
                   error_text_format="Enter number less than {}", pause=True, pause_text_bool=True,
                   pause_text='Press Enter...', clear=True, error_text_input="Enter float number!",
                   pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                   error_text_bool=True, error_text_input_bool=True, func=_lt_num_input):
    """
    function get input and safety convert it into float next test that number is lower than 'than' if yes return it
    :param than: number that input number must be lower
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: float number lower than 'than'
    """
    return func(float, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def le_int_input(than, text='', error_text="Enter integer number less or equal than ", error_text_format_bool=True,
                 error_text_format="Enter integer number less or equal than {}", pause=True, pause_text_bool=True,
                 pause_text='Press Enter...', clear=True, error_text_input="Enter integer number!",
                 pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                 error_text_bool=True, error_text_input_bool=True, func=_le_num_input):
    """
    function get input and safety convert it into int
    next test that number is lower or equal than 'than' if yes return it
    :param than: number that input number must be lower or equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: integer number lower or equal than 'than'
    """
    return func(int, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def le_float_input(than, text='', error_text="Enter number less or equal than ", error_text_format_bool=True,
                   error_text_format="Enter number less or equal than {}", pause=True, pause_text_bool=True,
                   pause_text='Press Enter...', clear=True, error_text_input="Enter float number!",
                   pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                   error_text_bool=True, error_text_input_bool=True, func=_le_num_input):
    """
    function get input and safety convert it into float
    next test that number is lower or equal than 'than' if yes return it
    :param than: number that input number must be lower or equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: float number lower or equal than 'than'
    """
    return func(float, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def gt_int_input(than, text='', error_text="Enter integer number great than ", error_text_format_bool=True,
                 error_text_format="Enter integer number great than {}", pause=True, pause_text_bool=True,
                 pause_text='Press Enter...', clear=True, error_text_input="Enter integer number!",
                 pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                 error_text_bool=True, error_text_input_bool=True, func=_gt_num_input):
    """
    function get input and safety convert it into int
    next test that number is giger than 'than' if yes return it
    :param than: number that input number must be giger
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: integer number giger than 'than'
    """
    return func(int, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def gt_float_input(than, text='', error_text="Enter number great than ", error_text_format_bool=True,
                   error_text_format="Enter number great than {}", pause=True, pause_text_bool=True,
                   pause_text='Press Enter...', clear=True, error_text_input="Enter float number!",
                   pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                   error_text_bool=True, error_text_input_bool=True, func=_gt_num_input):
    """
    function get input and safety convert it into float
    next test that number is giger than 'than' if yes return it
    :param than: number that input number must be giger
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: float number giger than 'than'
    """
    return func(float, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def ge_int_input(than, text='', error_text="Enter integer number great or equal than ", error_text_format_bool=True,
                 error_text_format="Enter integer number great or equal than {}", pause=True, pause_text_bool=True,
                 pause_text='Press Enter...', clear=True, error_text_input="Enter integer number!",
                 pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                 error_text_bool=True, error_text_input_bool=True, func=_ge_num_input):
    """
    function get input and safety convert it into int
    next test that number is giger or equal than 'than' if yes return it
    :param than: number that input number must be giger or equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: integer number giger or equal than 'than'
    """
    return func(int, than=than, text=text, error_text=error_text, error_text_format_bool=error_text_format_bool,
                error_text_format=error_text_format, pause=pause, pause_text_bool=pause_text_bool,
                pause_text=pause_text, clear=clear, error_text_input=error_text_input,
                pause_input=pause_input, pause_input_text_bool=pause_input_text_bool,
                pause_input_text=pause_input_text, clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def ge_float_input(than, text='', error_text="Enter number great or equal than ", error_text_format_bool=True,
                   error_text_format="Enter number great or equal than {}", pause=True, pause_text_bool=True,
                   pause_text='Press Enter...', clear=True, error_text_input="Enter float number!",
                   pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                   error_text_bool=True, error_text_input_bool=True, func=_ge_num_input):
    """
    function get input and safety convert it into float
    next test that number is giger or equal than 'than' if yes return it
    :param than: number that input number must be giger or equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: float number giger or equal than 'than'
    """
    return func(float, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def ne_float_input(to, text='', error_text="Enter number negative to ", error_text_format_bool=True,
                   error_text_format="Enter number negative to {}", pause=True, pause_text_bool=True,
                   pause_text='Press Enter...', clear=True, error_text_input="Enter float number!",
                   pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                   error_text_bool=True, error_text_input_bool=True, func=_ne_num_input):
    """
    function get input and safety convert it into float
    next test that number is not equal to 'than' if yes return it
    :param to: number that input number must be not equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: float number not equal to 'to'
    """
    return func(float, to=to, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def ne_int_input(to, text='', error_text="Enter integer number negative to ", error_text_format_bool=True,
                 error_text_format="Enter integer number negative to {}", pause=True, pause_text_bool=True,
                 pause_text='Press Enter...', clear=True, error_text_input="Enter integer number!",
                 pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                 error_text_bool=True, error_text_input_bool=True, func=_ne_num_input):
    """
    function get input and safety convert it into int
    next test that number is not equal to 'than' if yes return it
    :param to: number that input number must be not equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: int number not equal to 'to'
    """
    return func(int, to=to, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def be_float_input(than, text='', error_text="Enter number great or equal than ", error_text_format_bool=True,
                   error_text_format="Enter number great or equal than {}", pause=True, pause_text_bool=True,
                   pause_text='Press Enter...', clear=True, error_text_input="Enter float number!",
                   pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                   error_text_bool=True, error_text_input_bool=True, func=_be_num_input):
    """
    function get input and safety convert it into float
    next test that number is between or equal than 'than' if yes return it
    :param than (list, tuple): numbers that input number must be between or equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: float number between or equal than 'than'
    """
    return func(float, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def bet_float_input(than, text='', error_text="Enter number great or equal than ", error_text_format_bool=True,
                    error_text_format="Enter number great or equal than {}", pause=True, pause_text_bool=True,
                    pause_text='Press Enter...', clear=True, error_text_input="Enter float number!",
                    pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                    error_text_bool=True, error_text_input_bool=True, func=_bet_num_input):
    """
    function get input and safety convert it into float
    next test that number is giger or equal than 'than[0]'
    and lower than 'than[1]' if yes return it
    :param than (list, tuple): numbers that input number must be between or equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: float number giger or equal than 'than[0]' and lower than 'than[1]'
    """
    return func(float, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def bte_float_input(than, text='', error_text="Enter number great or equal than ", error_text_format_bool=True,
                    error_text_format="Enter number great or equal than {}", pause=True, pause_text_bool=True,
                    pause_text='Press Enter...', clear=True, error_text_input="Enter float number!",
                    pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                    error_text_bool=True, error_text_input_bool=True, func=_bte_num_input):
    """
    function get input and safety convert it into float
    next test that number is giger than 'than[0]'
    and lower or equal than 'than[1]' if yes return it
    :param than (list, tuple): numbers that input number must be between or equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: float number gigerthan 'than[0]' and lower or equal  than 'than[1]'
    """
    return func(float, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def bt_float_input(than, text='', error_text="Enter number great or equal than ", error_text_format_bool=True,
                   error_text_format="Enter number great or equal than {}", pause=True, pause_text_bool=True,
                   pause_text='Press Enter...', clear=True, error_text_input="Enter float number!",
                   pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                   error_text_bool=True, error_text_input_bool=True, func=_bt_num_input):
    """
    function get input and safety convert it into float
    next test that number is between than 'than' if yes return it
    :param than (list, tuple): numbers that input number must be between
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: float number between than 'than'
    """
    return func(float, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def be_int_input(than, text='', error_text="Enter number between or equal than ", error_text_format_bool=True,
                 error_text_format="Enter number between or equal than {}", pause=True, pause_text_bool=True,
                 pause_text='Press Enter...', clear=True, error_text_input="Enter integer number!",
                 pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                 error_text_bool=True, error_text_input_bool=True, func=_be_num_input):
    """
    function get input and safety convert it into int
    next test that number is between or equal than 'than' if yes return it
    :param than (list, tuple): numbers that input number must be between or equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: int number between or equal than 'than'
    """
    return func(int, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def bet_int_input(than, text='', error_text="Enter number between or equal than ", error_text_format_bool=True,
                  error_text_format="Enter number between or equal than {}", pause=True, pause_text_bool=True,
                  pause_text='Press Enter...', clear=True, error_text_input="Enter integer number!",
                  pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                  error_text_bool=True, error_text_input_bool=True, func=_bet_num_input):
    """
    function get input and safety convert it into float
    next test that number is giger or equal than 'than[0]'
    and lower than 'than[1]' if yes return it
    :param than (list, tuple): numbers that input number must be between or equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: float number giger or equal than 'than[0]' and lower than 'than[1]'
    """
    return func(int, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def bte_int_input(than, text='', error_text="Enter number between or equal than ", error_text_format_bool=True,
                  error_text_format="Enter number between or equal than {}", pause=True, pause_text_bool=True,
                  pause_text='Press Enter...', clear=True, error_text_input="Enter integer number!",
                  pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                  error_text_bool=True, error_text_input_bool=True, func=_bte_num_input):
    """
    function get input and safety convert it into int
    next test that number is giger than 'than[0]'
    and lower or equal than 'than[1]' if yes return it
    :param than (list, tuple): numbers that input number must be between or equal
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: int number gigerthan 'than[0]' and lower or equal  than 'than[1]'
    """
    return func(int, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def bt_int_input(than, text='', error_text="Enter number between than ", error_text_format_bool=True,
                 error_text_format="Enter number between than {}", pause=True, pause_text_bool=True,
                 pause_text='Press Enter...', clear=True, error_text_input="Enter integer number!",
                 pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...', clear_input=True,
                 error_text_bool=True, error_text_input_bool=True, func=_bt_num_input):
    """
    function get input and safety convert it into int
    next test that number is between than 'than' if yes return it
    :param than (list, tuple): numbers that input number must be between
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: int number between than 'than'
    """
    return func(int, than=than, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def positive_int_input(text='', error_text="Enter positive number", error_text_format_bool=True,
                       error_text_format="Enter positive number", pause=True, pause_text_bool=True,
                       pause_text='Press Enter...', clear=True, error_text_input="Enter integer number!",
                       pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...',
                       clear_input=True,
                       error_text_bool=True, error_text_input_bool=True, func=_ge_num_input):
    """
    function get input and safety convert it into int
    next test that number is positive if yes return it
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: positive integer
    """
    return func(int, than=0, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def positive_float_input(text='', error_text="Enter positive number", error_text_format_bool=True,
                         error_text_format="Enter positive number", pause=True, pause_text_bool=True,
                         pause_text='Press Enter...', clear=True, error_text_input="Enter float number!",
                         pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...',
                         clear_input=True,
                         error_text_bool=True, error_text_input_bool=True, func=_ge_num_input):
    """
    function get input and safety convert it into float
    next test that number is positive if yes return it
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: positive float
    """
    return func(float, than=0, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def negative_int_input(text='', error_text="Enter negative number", error_text_format_bool=True,
                       error_text_format="Enter negative number", pause=True, pause_text_bool=True,
                       pause_text='Press Enter...', clear=True, error_text_input="Enter integer number!",
                       pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...',
                       clear_input=True,
                       error_text_bool=True, error_text_input_bool=True, func=_lt_num_input):
    """
    function get input and safety convert it into int
    next test that number is negative if yes return it
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: negative integer
    """
    return func(int, than=0, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)


def negative_float_input(text='', error_text="Enter negative number", error_text_format_bool=True,
                         error_text_format="Enter negative number", pause=True, pause_text_bool=True,
                         pause_text='Press Enter...', clear=True, error_text_input="Enter float number!",
                         pause_input=True, pause_input_text_bool=True, pause_input_text='Press Enter...',
                         clear_input=True,
                         error_text_bool=True, error_text_input_bool=True, func=_lt_num_input):
    """
    function get input and safety convert it into float
    next test that number is negative if yes return it
    :param text: text that shows on input default ''
    :param error_text: text that show on error
    :param error_text_format_bool: if True shows formated error text
    :param error_text_format: formated error text
    :param pause:if set True pause program until Enter is pressed default True
    :param pause_text_bool:if True shows text in pause
    :param pause_text:What shows on pause
    :param clear: if True clear console
    :param error_text_input:text that shows on error case -> if cant convert into int
    :param pause_input:if set True pause program until Enter is pressed default True
    :param pause_input_text_bool:if True shows text in pause
    :param pause_input_text:What shows on pause
    :param clear_input:if True clear console
    :param error_text_bool: if true shows error text if equation isnt true
    :param error_text_input_bool: if set True shows text if get error default True
    :return: negative float
    """
    return func(float, than=0, text=text, error_text=error_text,
                error_text_format_bool=error_text_format_bool, error_text_format=error_text_format,
                pause=pause, pause_text_bool=pause_text_bool, pause_text=pause_text, clear=clear,
                error_text_input=error_text_input, pause_input=pause_input,
                pause_input_text_bool=pause_input_text_bool, pause_input_text=pause_input_text,
                clear_input=clear_input, error_text_bool=error_text_bool,
                error_text_input_bool=error_text_input_bool)



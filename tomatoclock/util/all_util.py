import os


def is_integer_num(num):
    """ 判斷傳入是否為整數

    Args:
        num (any): 判斷對象

    Returns:
        boolen: 是整數為 Ture，非整數為 False 
    """    
    if isinstance(num, int):
        return True
    if isinstance(num, float):
        return num.is_integer()
    return False


def exit_program(msg: str =None):
    """顯示訊息並結束程式

    Args:
        msg (str, optional): 提示訊息. 預設為 None.
    """    
    if msg is not None: print(msg)
    exit(os.system("pause"))
    

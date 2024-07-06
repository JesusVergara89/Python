def compuebaMail(mail):
    """
    The function check if the mai typed has a valid format for the emails
    >>> compuebaMail('jesus@gmail.com')
    True
    >>> compuebaMail('jesusgmail.com')
    False
    >>> compuebaMail('jesusgmail.com@')
    False
    >>> compuebaMail('@jesusgmail.com')
    False
    >>> compuebaMail('jesus@gmail.c@om')
    False
    """
    arroba=mail.count('@')
    if arroba!=1 or mail.rfind('@')==(len(mail)-1) or mail.find('@')==0:
        return False
    else:
        return True

import doctest 
doctest.testmod() 
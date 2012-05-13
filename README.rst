py_fxxk
========================================

This module is a helper module for making brainfxxk-like language.

========================================
Usage
========================================

Default
****************************************

If you want to run default brainfxxk, you can do it by BrainFxxk class.

::
   
   import sys
   from py_fxxk import BrainFxxk
   
   def main():
       if len(sys.argv) != 2:
           sys.exit(1)
       BrainFxxk().fxxk(sys.argv[1])
   
   if __name__ == '__main__':
       main()   

If you want to debug brainfxxk program, debug option may be your help(Default=False).

:: 

       BrainFxxk(debug=True).fxxk(sys.argv[1])

Custom
****************************************

If you want to assign original marks as brainfxxk operators, please create new class extending Brainfxxk class.

::

   import sys
   from py_fxxk import BrainFxxk
   
   class Ook(BrainFxxk):
       def __init__(self):
           BrainFxxk.__init__(self, ope={
               u'nxt':u'Ook. Ook? ',
               u'prv':u'Ook? Ook. ',
               u'inc':u'Ook. Ook. ',
               u'dec':u'Ook! Ook! ',
               u'put':u'Ook! Ook. ',
               u'get':u'Ook. Ook! ',
               u'opn':u'Ook! Ook? ',
               u'cls':u'Ook? Ook! ',
          })
   
   def main():
       if len(sys.argv) != 2:
           sys.exit(1)
       Ook().fxxk(sys.argv[1])
   
   if __name__ == '__main__':
       main()

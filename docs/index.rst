.. argparser.extra documentation master file, created by
   sphinx-quickstart on Mon Nov 28 13:32:29 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2



Python argparse.ArgumentParser subclass(es)
-------------------------------------------

Quick example of argparser declaration from dictionary::
    
    import sys
    from argparse.extra import DictArgumentParser
    
    def run_testarg_processing(args, argv):
        print 'testarg argument used'

    ARGUMENTS = {'--use-something':{'dest':'use_something',
                                   'action':'store_true',
                                   'default':False},
                 'sub:testarg':{
                     #sub:testarg will create subparser 'testarg'
                     #depth of subargs is unlimited
                     'description':'Test arg subcommand',
                     'help':'Test help'
                     'func':run_testarg_processing,
                     '--use-sub-something':{'dest':'use_sub_something',
                                                   'action':'store_true',
                                                   'default':False},
                 }}

    DEFAULTS_ONLY = ['func',]
    def get_argparser(argsdict=ARGUMENTS):
        #always create get_argparser function for your cli apps
        #this will enable easy integration of subsequent applications
        #with your argparser
        return DictArgumentParser(argsdict, DEFAULTS_ONLY)

    def main(args=sys.argv):
        args, argv = get_argparser().parse_known_args(args[1:])
        args.func(args, argv)

    if __name__ == '__main__':
        main()


Installation
------------

Try one of these::

    python setup.py install

    easy_install argparse.extra

    pip install argparse.extra

Indices and tables
==================


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


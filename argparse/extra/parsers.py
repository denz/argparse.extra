import unittest
import argparse
class DictArgumentParser(argparse.ArgumentParser):
    def from_dict(self, argsdict):
        subparsers = None
        for k,v in argsdict.items():
            add_args = dict(((k,v) for k,v \
                            in v.items() if \
                            not isinstance(v,dict) \
                            and not k in self.defaults_only))
            if isinstance(k, basestring) and k.startswith('sub:'):
                if not subparsers:
                    subparsers = self.add_subparsers()
                
                add_args.update({
                   'argsdict':v, 
                   'defaults_only':self.defaults_only
                })
                parser = subparsers.add_parser(k.split(':')[1], **add_args)
            else:
                if not isinstance(k, (list, tuple)):
                    k = [k,]
                self.add_argument(*k, **add_args)

    def __init__(self, argsdict={}, defaults_only=[], **kwargs):
        super(DictArgumentParser, self).__init__(**kwargs)
        self.defaults_only = defaults_only
        if argsdict:
            self.from_dict(dict(((k,v) for k,v \
                            in argsdict.items() \
                            if isinstance(v,dict))))
            defaults_only = dict(((k,v) for k,v in argsdict.items() \
                                  if k in self.defaults_only))
            if defaults_only:
                self.set_defaults(**defaults_only)

class GetArgparserTestCase(unittest.TestCase):
    def test_simple_argsdict(self):
        argsdict = {'--no-virtualenv':{'dest':'use_virtualenv',
                            'action':'store_false',
                            'default':False},
                     '--no-distutils':{'dest':'use_setuptools',
                            'action':'store_true',
                            'default':False},
                     '--no-requirements':{'dest':'use_requirements',
                                        'action':'store_false',
                                        'default':True},
                     'sub:test':{
                         'description':'aa',
                         'help':'help'
                     }}
        args, argv = DictArgumentParser(argsdict).parse_known_args(['test',])
        self.assert_(args.__dict__  \
            == {'use_virtualenv': False, 
                'use_requirements': True, 
                'use_setuptools': False})
        args, argv = DictArgumentParser(argsdict).parse_known_args(['--no-requirements','test'])
        self.assert_(args.__dict__  \
            == {'use_virtualenv': False, 
                'use_requirements': False, 
                'use_setuptools': False})
    def test_simple_subparsers_argsdict(self):
        argsdict = {'--no-virtualenv':{'dest':'use_virtualenv',
                    'action':'store_false',
                    'default':False},
             '--no-distutils':{'dest':'use_setuptools',
                    'action':'store_true',
                    'default':False},
             '--no-requirements':{'dest':'use_requirements',
                                'action':'store_false',
                                'default':True},
             'sub:test':{
                 'description':'aa',
                 'help':'help'
             }}
        parser = DictArgumentParser(argsdict)
        args, argv = parser.parse_known_args(['test',])
        self.assert_('test' in parser._subparsers._group_actions[0].choices.keys())
    def test_defaults_only(self):
        def test_func0(args, argv):
            pass

        def test_func1(args, argv):
            pass

        argsdict = {'--no-virtualenv':{'dest':'use_virtualenv',
                    'action':'store_false',
                    'default':False},
                    '--no-distutils':{'dest':'use_setuptools',
                    'action':'store_true',
                    'default':False},
                    '--no-requirements':{'dest':'use_requirements',
                                'action':'store_false',
                                'default':True},
             'sub:test0':{
                 'description':'aa',
                 'help':'help',
                 'func':test_func0,
             },
             'sub:test1':{
                 'description':'aa',
                 'help':'help',
                 'func':test_func1,
             },
             }
        parser = DictArgumentParser(argsdict, ['func'])
        args, argv = parser.parse_known_args(['test0',])
        self.assert_(args.func==test_func0)
        args, argv = parser.parse_known_args(['test1',])
        self.assert_(args.func==test_func1)

    def test_sub_sub(self):
        def test_sub_sub(args, argv):
            pass

        argsdict = {'--no-virtualenv':{'dest':'use_virtualenv',
                    'action':'store_false',
                    'default':False},
                    '--no-distutils':{'dest':'use_setuptools',
                    'action':'store_true',
                    'default':False},
                    '--no-requirements':{'dest':'use_requirements',
                                'action':'store_false',
                                'default':True},
             'sub:test0':{
                 'description':'aa',
                 'help':'help',
                 'func':lambda x:x,
                 'sub:sub':{
                        'description':'bb',
                        'help':'cc',
                        'another_func':test_sub_sub,
                 },
             },
             'sub:test1':{
                 'description':'aa',
                 'help':'help',
                 'func':lambda x:x,
             },
             }
        parser = DictArgumentParser(argsdict, ['func', 'another_func'])
        args, argv = parser.parse_known_args(['test0','sub'])
        self.assert_(args.another_func==test_sub_sub)

if __name__ == '__main__':
    unittest.main()
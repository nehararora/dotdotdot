# -*- coding: utf-8 -*-
"""
test_config: Some basic test for the package.
"""
import sys
import pytest

from .context import dotdotdot as dotconf


class TestConfig:
    """
    Test class for the config module
    """
    def test_creation(self):
        with pytest.raises(TypeError) as ei:
            dotconf.load()
        # python 2, 3 have different messaging
        if sys.version_info.major == 2:
            msg = 'load() takes exactly 1 argument (0 given)'
        else:
            msg = "load() missing 1 required positional argument: 'paths'"
        assert msg == str(ei.value)

        with pytest.raises(dotconf.ConfigException) as ei:
            dotconf.load('')
        assert "'No configuration file specified'" == str(ei.value)

        # TODO: how? assert '' == ce.reason

        with pytest.raises(dotconf.ConfigException) as ei:
            dotconf.load(None)
        assert "'No configuration file specified'" == str(ei.value)
        # TODO: how?
        # assert ce.reason is None

        with pytest.raises(dotconf.ConfigException) as ei:
            dotconf.load([])
        assert "'No configuration file specified'" == str(ei.value)
        # assert [] == ce.reason

        with pytest.raises(IOError) as ei:
            dotconf.load(['whatevs'])
        msg = "[Errno 2] No such file or directory: 'whatevs'"
        assert msg == str(ei.value)
        with pytest.raises(IOError) as ei:
            dotconf.load('whatevs')
        msg = "[Errno 2] No such file or directory: 'whatevs'"
        assert msg == str(ei.value)

        # check for specified file being a directory
        if sys.version_info.major == 3:
            msg = ''
            with pytest.raises(IsADirectoryError) as de:
                config = dotconf.load('tests')
                assert msg == str(de.value)
        elif sys.version_info.major == 2:
            msg = "[Errno 21] Is a directory: 'tests'"
            with pytest.raises(IOError) as ie:
                config = dotconf.load('tests')
                assert msg == str(ie.value)

        config = dotconf.load('tests/test_config.yml')
        assert dotconf.Config == type(config)

    def test_yml(self):
        config = dotconf.load('tests/test_config.yml')
        assert type(config) is dotconf.Config
        assert hasattr(config, 'test')
        assert hasattr(config.test, 'nest')
        assert hasattr(config.test.nest, 'inty')
        assert type(config.test.nest.inty) is int
        assert 1 == config.test.nest.inty

        assert hasattr(config.test.nest, 'listy')
        assert type(config.test.nest.listy) is list
        assert [1] == config.test.nest.listy

        assert hasattr(config.test.nest, 'stringy')
        assert type(config.test.nest.stringy) is str
        assert 'string' == config.test.nest.stringy

    def test_ini(self):
        """
        TODO: not supported yet.
        :param self:
        :return:
        """

    def test_indexing(self):
        """
        Test dictionary like access
        :return:
        """
        config = dotconf.load('tests/test_config.yml')

        #  test subscripting
        assert config.test.nest.inty == 1
        assert config['test'].nest.inty == 1
        assert config.test['nest'].inty == 1
        assert config.test.nest['inty'] == 1
        assert config['test']['nest']['inty'] == 1

        # test get()

        assert config.get('test').nest.inty == 1
        assert config.test.get('nest').inty == 1
        assert config.test.nest.get('inty') == 1
        assert config.get('test').get('nest').get('inty') == 1

        # test None default
        assert config.test.nest.get('intys', None) is None

        # test non-None default
        assert config.test.nest.get('intys', 2) == 2

        # test key error
        with pytest.raises(KeyError):
            x = config.test.nest['intys']

    def test_representation(self):
        """
        Test repr, str

        :return:
        """

        config = dotconf.load('tests/test_config.yml')
        assert type(config) is dotconf.Config
        print(str(config))
        string = ('!!python/object:dotdotdot.config.Config\ntest: '
                  '!!python/object:dotdotdot.config.test\n  nest: '
                  '!!python/object:dotdotdot.config.nest\n    inty: 1\n    '
                  'listy:\n    - 1\n    stringy: string\n')
        assert str(config) == string
        el_repr = ('!!python/object:dotdotdot.config.Config\ntest: '
                   '!!python/object:dotdotdot.config.test\n  nest: '
                   '!!python/object:dotdotdot.config.nest\n    inty: 1\n    '
                   'listy: [1]\n    stringy: string\n')
        assert repr(config) == el_repr

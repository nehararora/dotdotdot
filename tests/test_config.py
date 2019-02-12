# -*- coding: utf-8 -*-
"""
test_config: Some basic test for the package.
"""
import pytest

from .context import dotdotdot as dotconf


class TestConfig:
    """
    Test class for the config module
    """
    def test_creation(self):
        with pytest.raises(TypeError) as ei:
            dotconf.load()
        # assert 'xload() takes exactly 1 argument (0 given)' == str(ei.value)
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
        # TODO: how?? assert 'whatevs' == ei.filename
        msg = "[Errno 2] No such file or directory: 'whatevs'"
        assert msg == str(ei.value)
        with pytest.raises(IOError) as ei:
            dotconf.load('whatevs')
        # TODO: how?? assert 'whatevs' == ei.filename
        msg = "[Errno 2] No such file or directory: 'whatevs'"
        assert msg == str(ei.value)

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

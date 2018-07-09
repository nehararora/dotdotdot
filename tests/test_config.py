import unittest

from .context import dotdotdot as dotconf


class TestConfig(unittest.TestCase):
    """
    Test class for the config module
    """
    def test_creation(self):
        with self.assertRaises(TypeError) as context:
            dotconf.load()
        te = context.exception
        print('========')
        print(str(te))
        print('========')
        self.assertEquals('xload() takes exactly 1 argument (0 given)', str(te))

        with self.assertRaises(dotconf.ConfigException) as context:
            dotconf.load('')
        ce = context.exception
        self.assertEquals("'No configuration file specified'", str(ce))
        self.assertEquals('', ce.reason)

        with self.assertRaises(dotconf.ConfigException) as context:
            dotconf.load(None)
        ce = context.exception
        self.assertEquals("'No configuration file specified'", str(ce))
        self.assertEquals(None, ce.reason)

        with self.assertRaises(dotconf.ConfigException) as context:
            dotconf.load([])
        ce = context.exception
        self.assertEquals("'No configuration file specified'", str(ce))
        self.assertEquals([], ce.reason)

        with self.assertRaises(IOError) as context:
            dotconf.load(['whatevs'])
        ioe = context.exception
        self.assertEquals('whatevs', ioe.filename)
        self.assertEquals("[Errno 2] No such file or directory: 'whatevs'", str(ioe))
        with self.assertRaises(IOError) as context:
            dotconf.load('whatevs')
        ioe = context.exception
        self.assertEquals('whatevs', ioe.filename)
        self.assertEquals("[Errno 2] No such file or directory: 'whatevs'", str(ioe))

        config = dotconf.load('tests/test_config.yml')
        self.assertEquals(dotconf.Config, type(config))

    def test_yml(self):
        config = dotconf.load('tests/test_config.yml')
        self.assertEquals(dotconf.Config, type(config))
        self.assertTrue(hasattr(config, 'test'))
        self.assertTrue(hasattr(config.test, 'nest'))
        self.assertTrue(hasattr(config.test.nest, 'inty'))
        self.assertEquals(int, type(config.test.nest.inty))
        self.assertEquals(1, config.test.nest.inty)

        self.assertTrue(hasattr(config.test.nest, 'listy'))
        self.assertEquals(list, type(config.test.nest.listy))
        self.assertEquals([1], config.test.nest.listy)

        self.assertTrue(hasattr(config.test.nest, 'stringy'))
        self.assertEquals(str, type(config.test.nest.stringy))
        self.assertEquals('string', config.test.nest.stringy)

    def test_ini(self):
        """
        TODO: not supported yet.
        :param self:
        :return:
        """


if __name__ == '__main__':
    unittest.main()

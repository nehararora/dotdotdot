dotdotdot
=========

A miniamlist python library to access application configuration using dot notation.

----
Usage
::
   (dot3.6) narora@nararombp ~/s/d/tests 𝓝𝓮𝓱𝓪𝓻 > cat test_config.yml
    test:
      nest:
        inty: 1
        stringy: 'string'
        listy: [1]
    (dot3.6) narora@nararombp ~/s/d/tests 𝓝𝓮𝓱𝓪𝓻 > python
    Python 3.6.4 (default, Dec 21 2017, 20:32:22)
    [GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import dotdotdot as dot
    >>> c = dot.load('test_config.yml')
    >>> type(c)
    <class 'dotdotdot.config.Config'>
    >>> type(c.test)
    <class 'dotdotdot.config.test'>
    >>> type(c.test.nest)
    <class 'dotdotdot.config.nest'>
    >>> type(c.test.nest.inty)
    <class 'int'>
    >>> type(c.test.nest.stringy)
    <class 'str'>
    >>> type(c.test.nest.listy)
    <class 'list'>
    >>> c.test.nest.inty
    1
    >>> c.test.nest.stringy
    'string'
    >>> c.test.nest.listy
    [1]
    >>>

----
Build the wheel:
::
    (3.6) nehar@mac ~/s/dotdotdot 𝓝𝓮𝓱𝓪𝓻 > python setup.py bdist_wheel

----
Install package
::

    (3.6) nehar@mac ~/s/dotdotdot 𝓝𝓮𝓱𝓪𝓻 > pip install dist/dotdotdot-1.0.0-py3-none-any.whl
    Processing ./dist/dist/dotdotdot-1.0.0-py3-none-any.whl 
    Installing collected packages: dotdotdot
    Successfully installed dotdotdot-1.0.0


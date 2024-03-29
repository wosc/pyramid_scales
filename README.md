pyramid\_scales
===============

**ABANDONED** Use https://pypi.org/project/prometheus-client/ instead

The excellent [scales](https://github.com/Cue/scales) library to collect
in-process metrics (see Coda Hale’s CodeConf talk "[Metrics
everywhere](http://codahale.com/codeconf-2011-04-09-metrics-metrics-everywhere.pdf)"
among many others for reasons why you might want use it) comes with a
[flask](http://flask.pocoo.org/)-based HTTP server that allows viewing
the collected measurements and dumping them as JSON. But if you already
are in a web application using
[pyramid](http://docs.pylonsproject.org/en/latest/docs/pyramid.html),
there's no real need to spin up yet another thread, open another port
etc. to do this.

Instead, you can simply include `pyramid_scales` like so:

    import pyramid.config
    config = pyramid.config.Configurator()
    # rest of your configuration goes here
    config.include('pyramid_scales')

This registeres a view below the URL `/scales/` where you can view your
application's metrics. If you need more control, register the
`pyramid_scales.scales_stats` view yourself in whichever way you need.

This package is compatible with Python version 2.7 (scales itself does
not support Python3 yet, so there's no point here).

# assign inputs
_mode_, _level = IN
locationRefMode = None

try:
    from butterfly.refinementRegion import Inside, Outside
except ImportError as e:
    msg = '\nFailed to import butterfly. Did you install butterfly on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/mostaphaRoudsari/Butterfly/tree/master/plugin/dynamo/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/mostaphaRoudsari/Butterfly/issues'
        
    raise ImportError('{}\n{}'.format(msg, e))

if _level:
    if not _mode_:
        locationRefMode = Inside(_level)
    else:
        locationRefMode = Outside(_level)

# assign outputs to OUT
OUT = (locationRefMode,)
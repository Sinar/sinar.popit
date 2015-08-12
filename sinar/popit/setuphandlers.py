from collective.grok import gs
from sinar.popit import MessageFactory as _

@gs.importstep(
    name=u'sinar.popit', 
    title=_('sinar.popit import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinar.popit.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here

"""Behaviours to lookup and fill data from Popit API

Includes a form field and a behaviour adapter that stores the data in
custom popit string fields.

"""

from Products.CMFCore.interfaces import IDublinCore
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from zope.interface import alsoProvides 
from zope import schema
from plone.dexterity.interfaces import IDexterityContent

from sinar.popit import _

@provider(IFormFieldProvider)
class IPopitPerson(model.Schema):
    """Popit Person ID
    """
    popit_personid = schema.TextLine(
            title=_(u'Popit Person ID'),
            description=_(u'Popit Person ID'),
            required=False,
        )

    #adapters popit to description
    #adapters popit to biography field
    #adtpters popit to leadimage

@provider(IFormFieldProvider)
class IPopitPost (model.Schema):
    """Popit Post  
    """
    popit_postid = schema.TextLine(
            title=_(u'Popit Post ID'),
            description=_(u'Popit Post ID'),
            required=False,
        )

    #adapters popit to description
    #adapters popit to biography field
    #adtpters popit to leadimage

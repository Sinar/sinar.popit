# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sinar.popit


class SinarPopitLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=sinar.popit)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.popit:default')


SINAR_POPIT_FIXTURE = SinarPopitLayer()


SINAR_POPIT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_POPIT_FIXTURE,),
    name='SinarPopitLayer:IntegrationTesting',
)


SINAR_POPIT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_POPIT_FIXTURE,),
    name='SinarPopitLayer:FunctionalTesting',
)


SINAR_POPIT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_POPIT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarPopitLayer:AcceptanceTesting',
)

# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from sinar.popit.testing import SINAR_POPIT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that sinar.popit is properly installed."""

    layer = SINAR_POPIT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sinar.popit is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'sinar.popit'))

    def test_browserlayer(self):
        """Test that ISinarPopitLayer is registered."""
        from sinar.popit.interfaces import (
            ISinarPopitLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ISinarPopitLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SINAR_POPIT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['sinar.popit'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if sinar.popit is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'sinar.popit'))

    def test_browserlayer_removed(self):
        """Test that ISinarPopitLayer is removed."""
        from sinar.popit.interfaces import \
            ISinarPopitLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ISinarPopitLayer,
           utils.registered_layers())

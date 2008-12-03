# -*- coding: utf-8 -*-
#!/usr/bin/env python


########################################################################
#
#       Copyright (C) 2005, 2006, 2007 Carabos Coop. V. All rights reserved
#       Copyright (C) 2008 Vicent Mas. All rights reserved
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#       Author:  Vicent Mas - vmas@vitables.org
#
#       $Source$
#       $Id: preferencesGUI.py 1071 2008-10-17 16:49:03Z vmas $
#
########################################################################


"""
Here is defined the PreferencesGUI class.

Classes:

* PreferencesGUI(QtGui.QDialog)

Methods:

* __init__(self)
* __tr(self, source, comment=None)
* makeGeneralPage(self, general_page)
* makeLookAndFeelPage(self, lf_page)

Functions:

Misc variables:

* __docformat__

"""

__docformat__ = 'restructuredtext'

import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore

class PreferencesGUI(QtGui.QDialog):
    """
    Creates the `Preferences` dialog.

    The `Preferences` dialog is a tabbed dialog with 2 pages, ``General``
    and ``Look&Feel``.
    In the ``General`` page the startup behavior can be configured.
    In the ``Look&Feel`` page the configurable settings are:

    - font, foreground and background color of the logger
    - background color of the workspace
    - application style

    The dialog has ``OK``, ``Reset``, ``Apply`` and ``Cancel``
    buttons. They behave as usual.
    """

    def __init__(self):
        """
        Init the preferences dialog and makes the GUI.
        """

        QtGui.QDialog.__init__(self, QtGui.qApp.activeWindow())
        self.setWindowTitle(self.__tr('ViTables configuration dialog',
            'Caption of the preferences dialog'))

        # Make the dialog tabbed
        tab_widget = QtGui.QTabWidget(self)

        # Make pages
        general_page = QtGui.QWidget()
        self.makeGeneralPage(general_page)
        lf_page = QtGui.QWidget()
        self.makeLookAndFeelPage(lf_page)

        # Make buttons
        self.buttons_box = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Reset|
                                            QtGui.QDialogButtonBox.Ok|
                                            QtGui.QDialogButtonBox.Cancel)

        # Add pages to dialog
        tab_widget.addTab(general_page, self.__tr('&General',
            'The title of the first dialog tab'))
        tab_widget.addTab(lf_page, self.__tr('&Look and Feel',
            'The title of the second dialog tab'))

        # The dialog layout
        dlg_layout = QtGui.QVBoxLayout(self)
        dlg_layout.addWidget(tab_widget)
        dlg_layout.addWidget(self.buttons_box)


    def __tr(self, source, comment=None):
        """Translate method."""
        return str(QtGui.qApp.translate('PreferencesGUI', source, comment))


    def makeGeneralPage(self, general_page):
        """
        Add components to the Startup group box of the General page.

        :Parameter general_page: the page being composed.
        """

        # The page contains only a QGroupBox with one check box and two
        # radio buttons
        startup_gb = QtGui.QGroupBox(general_page)
        startup_gb.setTitle( self.__tr('Startup',
            'The name of the groupbox where startup is configured'))

        self.restore_cb = QtGui.QCheckBox()
        self.restore_cb.setText(self.__tr('Restore last session',
            'Label of the restore last session check button'))

        current_dir_rb = QtGui.QRadioButton()
        current_dir_rb.setText(self.__tr('Start in home directory',
            'Label of the startup in home directory radio button'))

        last_dir_rb = QtGui.QRadioButton()
        last_dir_rb.setText(self.__tr('Start in last opened directory',
            'Label of the startup in the last open directory radio button'))

        # An invisible button group is used to make radio buttons exclusive
        self.hiden_bg = QtGui.QButtonGroup()
        self.hiden_bg.setExclusive(1)
        self.hiden_bg.addButton(current_dir_rb, 1)
        self.hiden_bg.addButton(last_dir_rb, 2)

        # The page layout
        vbox = QtGui.QVBoxLayout(startup_gb)
        vbox.addWidget(self.restore_cb)
        vbox.addWidget(current_dir_rb)
        vbox.addWidget(last_dir_rb)
        general_layout = QtGui.QVBoxLayout(general_page)
        general_layout.addWidget(startup_gb)


    def makeLookAndFeelPage(self, lf_page):
        """
        Add components to the Startup group box of the General page.

        :Parameter lf_page: the page being composed.
        """

        # The page contains three groupboxes: Logger,Workspace and Style
        # The Logger groupbox
        logger_gb = QtGui.QGroupBox(lf_page)
        logger_gb.setTitle(self.__tr('Logger',
            'The title of the logger groubox'))
        self.font_pb = QtGui.QPushButton(self.__tr('&Font',
            'The label of the logger font chooser button'))
        self.foreground_pb = QtGui.QPushButton(self.__tr('F&oreground',
            'The label of the logger text color button'))
        self.background_pb = QtGui.QPushButton(self.__tr('&Background',
            'The label of the logger color button'))
        text = """<p>En un lugar de La Mancha,<br>""" \
        """de cuyo nombre no quiero acordarme,<br>""" \
        """no ha mucho tiempo vivia un hidalgo...</p>"""
        self.sample_te = QtGui.QTextEdit(logger_gb)
        self.sample_te.setAcceptRichText(True)
        self.sample_te.setText(text)
        self.sample_te.setReadOnly(1)
        logger_layout = QtGui.QGridLayout(logger_gb)
        logger_layout.addWidget(self.font_pb, 0, 0)
        logger_layout.addWidget(self.foreground_pb, 1, 0)
        logger_layout.addWidget(self.background_pb, 2, 0)
        logger_layout.addWidget(self.sample_te, 0, 1, 3, 1)

        # The Workspace groupbox
        workspace_gb = QtGui.QGroupBox(lf_page)
        workspace_gb.setTitle(self.__tr('Workspace',
            'The title of the workspace groupbox'))
        self.workspace_pb = QtGui.QPushButton(self.__tr('&Background',
            'The label of the logger color button'))
        self.workspace_label = \
            QtGui.QLabel(self.__tr('Background color sample',
                                   'A label for the workspace color sample'))
        self.workspace_label.setAutoFillBackground(True)
        workspace_layout = QtGui.QHBoxLayout(workspace_gb)
        workspace_layout.addWidget(self.workspace_pb)
        workspace_layout.addWidget(self.workspace_label)

        # The Style groupbox
        style_gb = QtGui.QGroupBox(lf_page)
        style_gb.setTitle(self.__tr('Style',
            'The title of the global aspect groupbox'))
        self.styles_cb = QtGui.QComboBox(style_gb)
        # Style names can be retrieved with qt.QStyleFactory.keys()
        # The following map between qt.QStyles and style names applies:
        # 'QtGui.QWindowsStyle': 'Windows',
        # 'QtGui.QMotifStyle': 'Motif',
        # 'QtGui.QCDEStyle': 'CDE'
        # 'QtGui.QPlastiqueStyle': 'Plastique'
        # 'QtGui.QCleanlooksStyle': 'Cleanlooks'
        # 'qt.QMacStyle': 'Macintosh',
        # 'QtGui.QWindowsXPStyle': 'WindowsXP',
        # WindowsXP and Macintosh (Aqua) styles are only implemented in
        # the PyQt for these platforms
        styles = ['default', 'Windows', 'Motif',  'CDE', 'Plastique',
            'Cleanlooks']
        self.styles_cb.insertItems(0, QtCore.QStringList(styles))
        style_layout = QtGui.QHBoxLayout(style_gb)
        style_layout.addWidget(self.styles_cb)

        # The page layout
        lf_layout = QtGui.QVBoxLayout(lf_page)
        lf_layout.addWidget(logger_gb)
        lf_layout.addWidget(workspace_gb)
        lf_layout.addWidget(style_gb)


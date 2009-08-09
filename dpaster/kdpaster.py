#!/usr/bin/python
"""KDE support for dpaste"""
import sys, time
import dcop
import dcopext
from kdecore import KApplication, KCmdLineArgs, KAboutData
from qt import QString, QCString

import StringIO
import dpaster

description = "KDE interface to http://dpaste.com/"
version     = "0.1"
aboutData   = KAboutData ("testdcopext", "testdcopext",\
    version, description, KAboutData.License_GPL,\
    "(C) 2007 Peter Fein")

aboutData.addAuthor ("Peter Fein", "wrote it", "pfein@pobox.com")

KCmdLineArgs.init (sys.argv, aboutData)

app  = KApplication ()
dcop = app.dcopClient ()

d = dcopext.DCOPApp ("klipper", dcop)
res, content = d.klipper.getClipboardContents()
sio=StringIO.StringIO(content)
url=dpaster.paste(sio)
res=d.klipper.setClipboardContents(url)
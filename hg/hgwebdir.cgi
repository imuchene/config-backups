#!/usr/bin/env python
#
from mercurial import demandimport; demandimport.enable()
from mercurial.hgweb.hgwebdir_mod import hgwebdir
import mercurial.hgweb.wsgicgi as wsgicgi
application = hgwebdir('hgweb.config')
wsgicgi.launch(application)


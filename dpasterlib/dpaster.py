"""client for http://dpaste.com/"""
import sys
import StringIO
import os.path

from twill.commands import *

format2ext={"Python":".py", 
            "PythonConsole":None, 
            "Sql":".sql",
            "DjangoTemplate":None, 
            "JScript":".js",
            "Css":".css", 
            "Xml":".xml", 
            "Diff":".diff", 
            "Ruby":".rb", 
            "Rhtml":".rhtml", 
            "Haskell":None, 
            "Apache":None, 
            "Bash":".sh", 
            "Plain":".txt"}

ext2format=dict((v, k) for k, v in format2ext.iteritems() if v is not None)

def paste(infile, format='Plain', browser=None):
    fname=getattr(infile, 'name', None) # StringIOs don't have a name
    if format is None and fname is not None:
        ext=os.path.splitext(fname)[1]
        format=ext2format.get(ext, "Plain")
    
    go('http://dpaste.com/')
    formvalue('pasteform', 'language', format)
    formvalue('pasteform', 'content', infile.read())
    submit()
    if browser:
        import webbrowser
        url = get_browser().get_url()
        webbrowser.open(url)
        return url
    else:
        return get_browser().get_url()

def copy(pasteid, format='plain'):
    url='http://dpaste.com/%d/%s/'%(pasteid, format)
    go(url)
    return get_browser().get_html()

def enable_debug(debug):
    if isinstance(debug, bool) or debug is None:
        if debug:
            twillout=sys.stderr
        else:
            twillout=StringIO.StringIO()        
    elif isinstance(debug, str):
        twillout=file(debug, 'a')
    else:
        raise ValueError, debug

    import twill
    twill.set_output(twillout)
    twill.set_errout(twillout)

enable_debug(False)

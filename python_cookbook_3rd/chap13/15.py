# 13.15 Lanuching a Web Browser

import webbrowser

# Open the page in a new browser window
webbrowser.open_new('http://www.python.org')

# Open the page in a new browser tab
webbrowser.open_new_tab('http://www.python.org')

# Use specific browser
c = webbrowser.get('firefox')
c.open('http://www.python.org')

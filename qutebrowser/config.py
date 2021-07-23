# TODO: Separate sections into different files

c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.grayscale.all = False
c.colors.webpage.preferred_color_scheme = 'dark'

c.content.autoplay = False
c.content.blocking.method = 'adblock'

c.editor.command = ['zsh', 'vim', '{file}']

c.fonts.default_family = 'MesloLGS NF'
c.fonts.default_size = '16pt'
c.fonts.downloads = 'MesloLGS NF'
c.fonts.hints = 'default_size default_family'

c.hints.chars = 'arstneiogmdh'

c.scrolling.bar = 'always'
c.scrolling.smooth = True

c.session.lazy_restore = True

c.tabs.background = True
c.tabs.max_width = -1
c.tabs.new_position.unrelated = 'next'
c.tabs.position = 'left'
c.tabs.select_on_remove = 'next'
c.tabs.show = 'always'
c.tabs.show_switching_delay = 5000

c.url.searchengines = {'DEFAULT': 'https://www.google.com/search?q={}', 'g': 'https://www.google.com/search?q={}', 'd': 'https://www.duckduckgo.com/search?q={}', 'y': 'https://www.youtube.com/results?search_query={}'}

c.window.hide_decoration = False


#########
# Binds #
#########

# scrolling
config.bind('<Ctrl+e>', 'scroll-px 0 100')
config.bind('<Ctrl+y>', 'scroll-px 0 -100')

# tab navigation
config.bind('j', 'tab-next')
config.bind('k', 'tab-prev')
config.bind('J', 'tab-move +')
config.bind('K', 'tab-move -')
config.bind('t', 'set-cmd-text -s :tab-select')

config.load_autoconfig(False)

config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')
config.set('content.desktop_capture', True, 'https://app.chime.aws')
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'qute://*/*')
config.set('content.media.audio_capture', True, 'https://app.chime.aws')
config.set('content.media.audio_video_capture', True, 'https://app.chime.aws')
config.set('content.media.video_capture', True, 'https://app.chime.aws')
config.set('content.register_protocol_handler', True, 'https://mail.google.com?extsrc=mailto&url=%25s')

config.source('qutebrowser-themes/themes/onedark.py')

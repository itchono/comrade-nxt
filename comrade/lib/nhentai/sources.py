from .proxies import (
    # GoogleTranslateProxy,
    NHentaiMirror,
    NHentaiSource,
    NHentaiWebProxy,
)

ORDERED_SOURCES: list[NHentaiSource] = [
    # These work
    NHentaiMirror("nhentai.to Mirror", "https://nhentai.to"),
    NHentaiMirror("nhentai.xxx Mirror", "https://nhentai.xxx"),
    NHentaiMirror("nhentai.uk Mirror", "https://nhentai.uk"),
    NHentaiWebProxy(
        "Yandex Proxy",
        "https://translated.turbopages.org/proxy_u/ru-en.en.63e09291-64c406b5-1259c722-74722d776562/https/nhentai.net",
    ),
    # These two don't work
    # GoogleTranslateProxy(
    #     "Google Translate Proxy",
    #     "http://translate.google.com/translate?sl=ja&tl=en&u=https://nhentai.net",
    # ),
    # NHentaiSource("nhentai.net", "https://nhentai.net"),
]

IMAGE_LINK_BASE = "https://i3.nhentai.net/galleries"

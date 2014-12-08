import urllib, json, i18n

def results(parsed, original_query):
    search_specs = [
          ["English Wikipedia", "~enWiki", "https://en.m.wikipedia.org/w/index.php?search=", "https://en.wikipedia.org/w/index.php?search="],
          ["French Wikipedia", "~frWiki", "https://fr.m.wikipedia.org/w/index.php?search=", "https://fr.wikipedia.org/w/index.php?search="],
          ["Italian Wikipedia", "~itWiki", "https://it.m.wikipedia.org/w/index.php?search=", "https://it.wikipedia.org/w/index.php?search="],
          ["Wikipedia", "~deWiki", "https://de.m.wikipedia.org/w/index.php?search=", "https://de.wikipedia.org/w/index.php?search="],
          ["Nederlandse Wikipedia", "~nlWiki", "https://nl.m.wikipedia.org/w/index.php?search=", "https://nl.wikipedia.org/w/index.php?search="],
          ["Wikipedia", "~deWiki", "https://de.m.wikipedia.org/w/index.php?search=", "https://de.wikipedia.org/w/index.php?search="]
    ]
    for name, key, mobile_url, url in search_specs:
        if key in parsed:
            mobile_search_url = mobile_url + urllib.quote_plus(parsed[key])
            search_url = url + urllib.quote_plus(parsed[key])
            return {
                "title": i18n.localstr("Search {0} for '{1}'").format(name, parsed[key]),
                "run_args": [search_url],
                "html": """
                <script>
                setTimeout(function() {
                    window.location = %s
                }, 500);
                </script>
                """%(json.dumps(mobile_search_url)),
                "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
                "webview_links_open_in_browser": True
            }

def run(url):
    import os
    os.system('open "{0}"'.format(url))

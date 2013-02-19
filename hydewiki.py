from jinja2 import nodes
from jinja2.ext import Extension
from mediawiki import wiki2html
from jinja2 import environmentfilter


@environmentfilter
def mediawiki(env, value):
    output = value
    d = {}

    return wiki2html(output, False)

class MediawikiExtension(Extension):
    # a set of names that trigger the extension.
    tags = set(['mediawiki'])

    def parse(self, parser):

        lineno = parser.stream.next().lineno

        body = parser.parse_statements(['name:endmediawiki'], drop_needle=True)
        print 'a'
        print 'a'

        #args = [parser.parse_expression()]
        return nodes.CallBlock(self.call_method('_render_mediawiki', None),
                               [], [], body).set_lineno(lineno)

    def _render_mediawiki(self, caller=None):
        if not caller:
            return ''
        output = caller().strip()
        print 'b'

        return mediawiki(self.environment, output)



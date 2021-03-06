##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo.report.report_sxw import rml_parse
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Parser(rml_parse):
    def __init__(self, cr, uid, name, context):
        super(Parser, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'myset': self.myset,
            'myget': self.myget,
            'storage': {}
        })

    def myset(self, pair):
        if isinstance(pair, dict):
            self.localcontext['storage'].update(pair)
        return False

    def myget(self, key):
        if key in self.localcontext['storage'] and self.localcontext[
                'storage'][key]:
            return self.localcontext['storage'][key]
        return False

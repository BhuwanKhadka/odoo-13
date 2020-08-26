# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class dynamic_cheque_template(models.AbstractModel):
	_name='report.generate_dynamic_cheque_app.report_dynamic_check_print'

	def _get_report_values(self, docids, data=None):
		wizard  = self.env['dynamic.cheque.wizard'].browse(docids)
		return {
				'doc_model': 'dynamic.cheque',
				'cheque_format' : wizard.cheque_format,
				'payment_id' : wizard.payment_id,
				}

class report_paperformat(models.Model):
	_inherit = "report.paperformat"

	custom_report = fields.Boolean('Temp Formats', default=False)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
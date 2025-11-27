from odoo import models, fields, api

class Certification(models.Model):
    _name = 'certification.management'
    _description = 'Gestion des Certifications'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_audit desc'

    name = fields.Char(string='Référence', required=True, copy=False, 
                       readonly=True, default='New')
    partner_id = fields.Many2one('res.partner', string='Client', 
                                  required=True, tracking=True)
    certification_type = fields.Selection([
        ('iso_9001', 'ISO 9001 - Qualité'),
        ('iso_14001', 'ISO 14001 - Environnement'),
        ('iso_45001', 'ISO 45001 - Santé et Sécurité'),
        ('other', 'Autre')
    ], string='Type de Certification', required=True, tracking=True)
    
    date_request = fields.Date(string='Date de Demande', 
                                default=fields.Date.today, required=True)
    date_audit = fields.Date(string='Date d\'Audit Prévue', tracking=True)
    date_certification = fields.Date(string='Date de Certification')
    
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('requested', 'Demande Reçue'),
        ('audit_scheduled', 'Audit Planifié'),
        ('audit_done', 'Audit Réalisé'),
        ('certified', 'Certifié'),
        ('rejected', 'Rejeté'),
        ('cancelled', 'Annulé')
    ], string='Statut', default='draft', required=True, tracking=True)
    
    auditor_id = fields.Many2one('res.users', string='Auditeur', 
                                  tracking=True)
    notes = fields.Text(string='Notes')
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'certification.management') or 'New'
        return super(Certification, self).create(vals)
    
    def action_request(self):
        self.state = 'requested'
    
    def action_schedule_audit(self):
        self.state = 'audit_scheduled'
    
    def action_audit_done(self):
        self.state = 'audit_done'
    
    def action_certify(self):
        self.state = 'certified'
        self.date_certification = fields.Date.today()
    
    def action_reject(self):
        self.state = 'rejected'
    
    def action_cancel(self):
        self.state = 'cancelled'

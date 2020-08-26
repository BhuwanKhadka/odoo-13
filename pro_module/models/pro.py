from odoo import fields, models

class ProRegistration(models.Model):
    _name = "pro.registration"
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', default='male')
    image = fields.Binary(string="Image")
    dob = fields.Date(string="Date of Birth")
    blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    nationality = fields.Selection([
        ('uae', 'UAE'),
        ('others', 'Others'),
    ], string='Nationality', default='uae')
    eid = fields.Integer(string="Emrates ID")
    maritial_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('others', 'Others'),
    ], string='Maritial Status', default='single')
    passportno = fields.Integer(string="Passport No")
    permanant_address=fields.Text(string="Permanant Address")
    present_address=fields.Text(string="Present Address")
#     permanant_street=fields.Char(string="Street")
#     present_street=fields.Char(string="Street")
    
    
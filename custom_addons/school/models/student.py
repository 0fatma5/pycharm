from odoo import models, fields

class Student(models.Model):
    _name = 'student'
    name = fields.Char(required=True)
    student_grade = fields.Selection(selection=[
        ('g1', 'Grade 1'),
        ('g2', 'Grade 2'),
        ('g3', 'Grade 3'),
        ('g4', 'Grade 4'),
        ('g5', 'Grade 5'),
        ('g6', 'Grade 6'),
        ('g7', 'Grade 7'),
        ('g8', 'Grade 8'),
        ('g9', 'Grade 9'),
        ('g10', 'Grade 10'),
        ('g11', 'Grade 11'),
        ('g12', 'Grade 12')
    ])
    age = fields.Integer(string='Age')
    student_id = fields.Integer("student id",required=True)
    gender = fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female')
    ])
    enrollment_date = fields.Date()
    phone_number = fields.Char()
    address = fields.Char()
    score = fields.Float(digit=10)

    school_id=fields.Many2one('school',required=True)

    _sql_constraints = [
        ('unique_phone_number', 'unique("phone_number")', 'This phone_number is exist'),
        ('unique_id', 'unique("student_id")', 'This student_id is exist')
    ]

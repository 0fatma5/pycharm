
from odoo import models, fields

class School(models.Model):
    _name = 'school'

    name = fields.Char(required=True)
    location = fields.Char()
    school_type = fields.Selection([('primary', 'Primary'), ('secondary', 'Secondary'), ('highschool', 'High School')],string='School Type')
    no_of_students = fields.Integer()
    no_of_teachers = fields.Integer()
    Principal_Name= fields.Char()
    campus_size = fields.Integer()
    school_address = fields.Char()
    students_ids = fields.One2many('student', 'school_id', string='Students')
    teacher_ids = fields.One2many('teacher', 'school_id', string='Teachers')
# ask??????????
#     _sql_constraints = [
#         ('unique_student_school', 'unique(students_ids)', 'This student already exists in this school!'),
#     ]




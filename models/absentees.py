from odoo import models, fields, api


class Absentees(models.Model):
    _name = 'hr.absentees'
    _description = 'Absentees'

    employee_id = fields.Many2one('hr.employee', string="Employee")
    absent_date = fields.Datetime(string="Absent Date",
                                  default=fields.Datetime.today())

    def absentees(self):
        print(self.env.company.id)
        employee_id = self.env['hr.employee'].search([('company_id', '=',
                                                       self.env.company.id)])
        print(employee_id)
        attendance_id = self.env['hr.attendance'].\
            search([('employee_id.company_id', '=', self.env.company.id)]).\
            mapped('employee_id')
        print('att', attendance_id)
        for i in employee_id:
            if i not in attendance_id:
                self.create({
                    'employee_id': i.id
                    })

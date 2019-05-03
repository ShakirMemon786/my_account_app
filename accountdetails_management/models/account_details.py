# -*- coding: utf-8 -*-
from datetime import timedelta
from flectra import api, fields, models
from flectra.exceptions import ValidationError

class AccountDetails(models.Model):

    _name="account.details"


    name = fields.Integer(string="Account Number", required=True)
    account_holder_name = fields.Char(string="Account Holder Name", size=30)
    account_holder_image = fields.Binary(string="Account Holder Image")
    accountopening_date = fields.Date(string="Account Opening Date")
    account_type = fields.Selection([('savings', 'Savings'),
                                 ('current', 'Current')], string="Account Type")
    description = fields.Text(string="Description")
    card_type = fields.Selection([('rupay', 'Rupay'),('master', 'Master')], string="Card Type",)
    total_balance = fields.Float(string="Total Balance")

    bank_id = fields.Many2one("bank.name", required=True, string="Bank")
    account_holder_ids = fields.Many2many("account.holder","account_holder_rel",'accountdetail_id','accountholder_id',string='accounts holder')

    start_date = fields.Date(string="Start date")

    @api.onchange('bank_id')
    def onchage_bank_id(self):
        print("-------Bank Details----", self.name, self.bank_id)
        self.account_type = self.bank_id.account_type

    @api.constrains('description')
    def check_description(self):
        if len(self.description) < 20 or len(self.description) > 50:
            raise ValidationError("Description should be  in between 20 to 50.")

class BankName(models.Model):

    _name = "bank.name"

    name = fields.Char(string="Bank Name", required=True)
    ifsc_code = fields.Char(string="IFSC CODE",size=4)
    account_line = fields.One2many("account.details", 'bank_id', string = "Accounts", readonly="True")
    active = fields.Boolean(string="Active", default=True)
    account_type = fields.Selection([('savings', 'Savings'),
                                     ('current', 'Current')], string="Account Type")
    #total_accounts = fields.Integer(string="Total Accounts in Bank", compute=_compute_total_accounts, store=True)


class AccountHolder(models.Model):
    _name = "account.holder"

    name = fields.Char(string="Account Holder")

    accountdetail_ids = fields.Many2many("account.details","account_holder_rel","accountholder_id","accountdetail_id",string="Account Details")

    total_accounts = fields.Integer(string="Total Accounts in Bank",readonly=True)

    @api.multi
    def count_total_accounts(self):
        print("Total Number Of Accounts-------", len(self))
        self.total_accounts= len(self.accountdetail_ids)
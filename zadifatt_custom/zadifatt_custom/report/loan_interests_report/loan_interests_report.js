// Copyright (c) 2023, Billy Adwar && OdukTech Limited and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Loan Interests Report"] = {
	"filters": [
		{
			fieldname: 'applicant',
			label: __('Applicant'),
			fieldtype: 'Link',
			width: 100,
			options: 'Customer'
		},
		{
			fieldname: 'name',
			label: __('Loan'),
			fieldtype: 'Link',
			width: 100,
			options: 'Loan'
		},
		{
			fieldname: 'status',
			label: __('Status'),
			fieldtype: 'Select',
			options: ['','Disbursed','Loan Closure Requested','Closed','Partially Disbursed'],
			default: "",
			width: 50,
		},
		{
			fieldname: 'from_date',
			label: __('From Date'),
			fieldtype: 'Date',
			default: frappe.datetime.add_months(frappe.datetime.get_today(),-1),
			width: 80
		},
		{
			fieldname: 'to_date',
			label: __('To Date'),
			fieldtype: 'Date',
			default: frappe.datetime.get_today(),
			width: 80
		}
	]
};

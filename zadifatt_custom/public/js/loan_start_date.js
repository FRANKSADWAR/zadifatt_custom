// Changes made on the is_term_loan field to set the date from the next day

frappe.ui.form.on('Loan', {
	is_term_loan: function(frm){
	    frm.set_value("repayment_start_date",frappe.datetime.add_days(frappe.datetime.now_date(),1));
	}
});
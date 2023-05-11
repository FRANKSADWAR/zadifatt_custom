// Custom JS functionality for the Loan.js DocType

frappe.ui.form.on('Loan', {
    // the applicant of a loan cannot be the same as the guarantor of that very loan
    onload: function(frm){
		console.log("This is working well");
        //frm.set_query("customer_name",function(){
		//	return {
		//		"filters":[
		//			["customer_name","!=", frm.doc.applicant]
		//		]
		//	}
		///});

		frm.set_query("customer_name",function(){
			return {
				query: "zadifatt_custom.query_api.filter_defaulted_customers",
				filters: {
					"customer_name" : frm.doc.applicant
				}
			};
		});
    },

    // Changes made on the is_term_loan field to set the date from the next day
	is_term_loan: function(frm){
	    frm.set_value("repayment_start_date",frappe.datetime.add_days(frappe.datetime.now_date(),1));
		console.log("This is working well")
	},

});
Ext.onReady(function() {
	new Ext.Viewport({
		layout : 'border',
		items : [
	        {
	        	region : 'center',
	        	xtype : 'tabpanel',
	        	items : [
        	        {
        	        	xtype : 'form',
        	        	id : 'createOrgFormId',
        	        	items : [
    	        	        {
    	        	        	xtype : 'textfield',
    	        	        	fieldLabel : 'Organization',
    	        	        	name : 'org_name'
    	        	        },
    	        	        {
    	        	        	xtype : 'textfield',
    	        	        	fieldLabel : 'URL',
    	        	        	name : 'url'
    	        	        },
    	        	        {
    	        	        	xtype : 'button',
    	        	        	text : 'Submit',
    	        	        	handler : function() {
    	        	        		var createOrgForm = Ext.getCmp(createOrgFormId);
    	        	        		var formvals = createOrgForm.getForm().getValues();
	    	        	        	Ext.Ajax.request({
	    	        	        		url : './someurl',
	    	        	        		params : formvals,
	    	        	        		callback : function(options, success, response) {
		    	        	        		Ext.Msg.alert("Status", "Submitting form!!");
		    	        	        	}
	    	        	        	});
	    	        	        }
    	        	        }
	        	        ]
        	        }
    	        ]
	        }
		]
	});
});
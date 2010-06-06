Ext.onReady(function() {
	new Ext.Viewport({
		layout : 'border',
		items : [
	        {
	        	region : 'center',
	        	xtype : 'tabpanel',
				activeTab : 0,
	        	items : [
        	        {
        	        	xtype : 'form',
						title: 'Create Organization', 
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
    	        	        	xtype : 'hidden',
								fieldLabel : 'Org Name',
    	        	        	name : 'org_name',
								value :  Ext.urlDecode(window.location.search.substring(1)).org_name
    	        	        },
    	        	        {
    	        	        	xtype : 'button',
    	        	        	text : 'Submit',
    	        	        	handler : function() {
    	        	        		var createOrgForm = Ext.getCmp('createOrgFormId');
    	        	        		var formvals = createOrgForm.getForm().getValues();
	    	        	        	Ext.Ajax.request({
	    	        	        		url : 'http://crisiscorpsapp.appspot.com/fb/Task',
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

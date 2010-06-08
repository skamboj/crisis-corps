/*
 * --------------------------------------------------------------------------
 * CrisisCorps.org
 * Copyright (c) 2010
 *
 * CrisisCorps is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * CrisisCorps is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with CrisisCorps.  If not, see <http://www.gnu.org/licenses/>.
 * --------------------------------------------------------------------------
 * 
 * File:   TaskForm.js
 * Author: Alex Schoof <alex.schoof@gmail.com>
 * Major Revisions:
 *  
 * --------------------------------------------------------------------------
 */

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
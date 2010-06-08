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
 * File:   OrganizationTasks.js
 * Author: Alex Schoof <alex.schoof@gmail.com>
 * Major Revisions:
 *  
 * --------------------------------------------------------------------------
 */

Ext.namespace("CC.Organization");

CC.Organization.Record = Ext.data.Record.create([
	{name : 'id'},
	{name : 'name'},
	{name : 'created'},
	{name : 'url'}
]);

CC.Organization.OrgCombo = Ext.extend(Ext.form.ComboBox, {
	constructor : function(config) {
		config = config || {};
		
		Ext.apply(config, {
			store : new Ext.data.Store({
				url : '/fb/Organization',
				params : {},
				fields : []
			}),
			
		});
		
		CC.Organization.OrgCombo.superclass.constructor.call(this, config);
	}
});

CC.Organization.OrgTaskGrid = Ext.extend(Ext.grid.GridPanel, {
	constructor : function(config) {
		config = config || {};
		
		Ext.apply(config, {
			title : 'Organization Tasks',
			store : new Ext.data.JsonStore({
				url : '',
				params: {},
				fields : CC.Organization.Record
			}),
			columns : [
	           {header : ''}
	        ]
		});
	
		CC.Organization.OrgTaskGrid.superclass.constructor.call(this, config);
	}
});
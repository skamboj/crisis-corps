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
Ext.namespace('CC.Task');

CC.Task.Record = Ext.data.Record.create([
	{name : 'id'},
	{name : 'title'},
	{name : 'description'},
	{name: 'created', type : 'date'},
	{name : 'organization'},
//	{name: ''},
//	{name: ''},
//	{name: ''},
	{name: 'location'}
]);

CC.Task.DisplayTemplate = new Ext.XTemplate(
	'<div class="task">',
		'<div class="taskHeader">',
			'<div class="taskTitle">{[values.taskRecord.title]}',
				'<div class="taskOrg">({[values.taskRecord.organization]})</div>',
			'</div>',
			'<div class="taskLocationSkills">Location & Skills</div>',
			'<div class="taskLinks">',
				'<a class="taskLink" onclick="CC.Task.startTask({[values.taskRecord.id]})">Start</a> | <a class="taskLink" onclick="CC.Task.ignoreTask({[values.taskRecord.id]});">No Thanks</a>',
			'</div>',
		'</div>',
		'<div class="taskDescription">{[values.taskRecord.description]}</div>',
	'</div>'
);

//Pass in a CC.Task.Record instance at
//	config.taskRecord to return a display
CC.Task.Display = Ext.extend(Ext.Container, {
	constructor : function(config) {
		config = config || {};
		
		var tpl = CC.Task.DisplayTemplate;
		
		this.taskRecord = config.taskRecord;
		
		Ext.apply(config, {
			autoEl : 'div',
			html : tpl.applyTemplate({
				taskRecord : config.taskRecord.data
			})
//			items : [
//		        new Ext.Container({
//		        	autoEl : 'div',
//		        	html : '<b>'+this.taskRecord.get('description')+'</b> (' + this.taskRecord.get('id') + ')'
//		        }, this),
//		        new Ext.Button({
//		        	text : 'Help with '+this.taskRecord.get('id'),
//		        	handler : function() {
//			        	//make Ajax call to have the user start working on this task
//		        		Ext.Msg.alert("Status", "Starting to work on Task ID "+this.taskRecord.get('id'));
//			        }.createDelegate(this)
//		        }, this)
//	        ] 
		});
	
		CC.Task.Display.superclass.constructor.call(this, config);
	}
});

//CC.Task.Display = Ext.extend(Ext.Panel, {
//	constructor : function(config) {
//		config = config || {};
//		
//		Ext.apply(config, {
//			title : config.taskRecord.get('description'),
//			collapsible : true,
//			collapsed : true,
//			items : [
//		        new Ext.Button({
//		        	text : 'Start working on Task ID '+config.taskRecord.get('id'),
//		        	handler : function() {
//		        		Ext.Msg.alert("Status", "Started Task!");
//		        	}
//		        })
//	        ]
//		});
//		
//		CC.Task.Display.superclass.constructor.call(this, config);
//	}
//});

CC.Task.TaskList = Ext.extend(Ext.Panel, {
	
	loadTasks : function() {
	
		//Example of how to load task displays
		var task = new CC.Task.Record({
			id : 42,
			description : 'This is my long task description',
			created: new Date(),
			location : 'Somewhere, USA'
		});
		
		var task2 = new CC.Task.Record({
			id : 42,
			description : 'This is my other task description',
			created: new Date(),
			location : 'Somewhere, USA'
		});
		
		this.add(new CC.Task.Display({
			taskRecord : task
		}));
		
		this.add(new CC.Task.Display({
			taskRecord : task2
		}));
		
		this.doLayout();
		
		//TODO (BG) Wait until the backend is available
//		Ext.Ajax.request({
//			url : '/fb/Task',
//			params : {},
//			callback : function(options, success, response) {
//				var jsondata = Ext.decode(response.responseText);
//				if(success && jsondata.success) {
//					Ext.Msg.alert("Status", "Retrieved "+jsondata.data.length+" tasks!");
//					
//					this.taskStore.loadData(jsondata);
//					
//					//refresh the display of tasks within the panel
//				}
//			}
//		});
	},
	
	constructor : function(config) {
		config = config || {};
		
		Ext.apply(config, {
			title : 'Open Tasks',
			autoHeight : true,
			bodyStyle : 'padding:10px;',
//			tools : [{
//				id : 'refresh',
//				handler : function() {
//					this.loadTasks();
//				}.createDelegate(this)
//			}],
			listeners : {
				'render' : function(thisCmp) {
					this.loadTasks();
				}
			},
			items : [
				{
					xtype : 'button',
					text : 'Get Tasks',
					handler : function() {
						Ext.Ajax.request({
							url : '/fb/Task',
							params : {},
							callback : function(options, success, response) {
								Ext.Msg.alert("Status", "Response : "+response.responseText);
							}
						});
					}
				},
				{
					xtype : 'button',
					text : 'Get Organizations',
					handler : function() {
						Ext.Ajax.request({
							url : '/fb/Organization',
							params : {},
							callback : function(options, success, response) {
								Ext.Msg.alert("Status", "Response : "+response.responseText);
							}
						});
					}
				},
			]
		});
		
		CC.Task.TaskList.superclass.constructor.call(this, config);
	}
});

CC.Task.startTask = function(taskId) {
	Ext.Msg.alert("Status", "Starting Task ID: "+taskId);
};

CC.Task.ignoreTask = function(taskId) {
	Ext.Msg.alert("Status", "Ignoring Task ID: "+taskId);
};

CC.Task.TasksByOrg = Ext.extend(Ext.grid.GridPanel, {
	constructor : function(config) {
	config = config || {};
	
	Ext.apply(config, {
		title : 'Organization Tasks',
		store : new Ext.data.JsonStore({
			url : '',
			params: {},
			fields : CC.Task.Record
		}),
		columns : [
           {header : 'ID', dataIndex : 'id'},
           {header : 'Title', dataIndex : 'title'},
           {header : 'Description', dataIndex : 'description'},
           {header : 'Organization', dataIndex : 'organization'},
           {header : 'Created', dataIndex : 'created'}
        ],
        tbar : new Ext.Toolbar({
        	items : [
    	        new Ext.form.ComboBox({
    	        	id : 'orgComboId',
    	        	store : new Ext.data.JsonStore({
    	        		url : '/fb/Organization',
    	        		params : {},
    	        		autoLoad : true,
    	        		fields : ['org_name', 'org_id']
    	        	}),
    	        	displayField : 'org_name',
    	        	valueField : 'org_id'
    	        }),
    	        {
	        		xtype : 'button',
	        		text : 'Get Tasks for Organization',
	        		handler : function() {
	    	        	var orgCombo = Ext.getCmp('orgComboId');
	    	        	var orgId = orgCombo.getValue();
	    	        	Ext.Ajax.request({
	    	        		url : '/fb/Task',
	    	        		params : {
		    	        		org_id : orgId
		    	        	},
		    	        	callback : function(options, success, response) {
		    	        		var json = Ext.decode(response.responseText);
		    	        		if(success) {
		    	        			Ext.Msg.alert("Status", "Retrieved "+json.length+" tasks!");
		    	        		}
		    	        	}
	    	        	});
	    	        }
	        	}
	        ]
        })
	});

	CC.Task.TasksByOrg.superclass.constructor.call(this, config);
}
});